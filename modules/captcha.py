import json, time, os, json, base64
import numpy as np
from . import hcaptcha

from .console import Console
from .utf_decoder import unicode_Coversion
import requests

from pathlib import Path

#ChatGPT Part Starts here:
from .ai_text.get_answer import find_answer

class CaptchaSolver:
    @staticmethod
    def get_captcha_by_ai(siteky, host ,proxy: str):
        
        if "http://" not in host:
            host = "http://"+host
        
        Console.debug("[*] SOLVING...")
        ch = hcaptcha.Challenge(
            sitekey=siteky,
            page_url=host,
            http_proxy=proxy
        )
        count = 0
        answers = []
        for tile in ch.tasks:
            question = tile.url['en']
            count +=1

            result = ''

            answers_file = open('./data/answers.txt', 'r')
            answers_lines_array = answers_file.readlines()
            for line in answers_lines_array:
                modified_question = question.replace('?','')
                if modified_question.lower() in line.lower():
                    if 'no' in line.lower():
                        result = 'no'
                        break
                    elif 'yes' in line.lower():     
                        result = 'yes'
                        break               
            answers_file.close()

            if result == '':
                Console.debug("[+] Asking AI....")            
                result = find_answer(question)




            if result != None:                
                Console.debug(f"[+] {count}, {question} {result}")

            if result == 'yes':
                answers.append(tile)
        try:
            Console.debug(f"[+] Providing Answers to the challenge!")
            token = ch.solve(answers)
            return token
        except hcaptcha.ApiError as e:

            #This is where the captcha fails. means its solved but wrong text-answers are chosen
            Console.debug(f"[-] Captcha solved but wrong, Retrying...")
