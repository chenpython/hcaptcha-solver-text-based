# 🔥 Captcha Solver 🔥 

A simple yet powerful Python project to solve captcha of type **TEXT-Challenge**. 💪
Some Proofs are shown in below images:
***With proxies:***
![Proxy](https://github.com/kokiez/hcaptcha-solver-text-based/blob/main/1.png)
![Proxy](https://github.com/kokiez/hcaptcha-solver-text-based/blob/main/2.png)
***Without proxies:***
![No Proxy](https://github.com/kokiez/hcaptcha-solver-text-based/blob/main/3-withoutproxy.png)

## ❗ Important Note 
This project only supports a sitekey which does provide a ***TEXT-Challenge***.
It might not work on all types of Challenges.

# 📥 Installating Requirements
1. Run the file named **install_requirements.bat**.
2. You will be required an open ai api key:
   - Worry not, the api key on first time provides 18 USD of credits. Which will take long to end. 
   - You can get api key by going [here](https://chat.openai.com/chat)
   - Ask the AI 'how to obtain an open ai key'
   - It will guide from A to Z.
   - Once key is obtained, go to data>api-secret.txt in this project and paste the open ai key in txt file. Then save it.

# 💻 Usage 💻
Using the CAPTCHA Solver is simple. 
1. Copy all the files from this repository to your project.
2. Use the following lines of code in your project:
    ```python
    from modules.console import Console
    from duplicates import remove_duplicate_lines
    from modules.captcha import CaptchaSolver
    
    proxypath = "./data/proxies.txt"
    proxy = open(proxypath,"r").read().split("\n")
        
    try:

        # site key
        website_key_captcha="4c672d35-0701-42b2-88c3-78380b0db560"
        
        # site url. Please add http:// with the url. such as abc.com so write http://abc.com
        website_URL_captcha="http://discord.com"

        if open(proxypath,"r").read() == '':
                    proxys = ""
        else:
            proxys = random.choice(proxy)
    
        token = CaptchaSolver.get_captcha_by_ai(website_key_captcha, website_URL_captcha ,proxys)
        
        if token == None:
            Console.printe("Captcha Error, Retrying...")
        else:
            Console.info("Token: "+token[:20])
        
        remove_duplicate_lines("./data/answers.txt")
        Console.debug("Deleted Duplicates from answers.txt!")
        
    except Exception as e:
        if "Max retries exceeded" in str(e):
            Console.printe("Max Retries reached, Changing proxy...")
            
# 🔒 Use at your own risk
I will not be responsible if my repository was used for illegal purposes. 

# 🙌 Contributing
We welcome contributions to the project. If you have any ideas or suggestions, feel free to open an issue or create a pull request.

# 📜 License
This project is licensed under the MIT License - see the **[LICENSE](https://github.com/kokiez/hcaptcha-solver-text-based/blob/main/LICENSE)**  file for details.

# 🙏 Thank you for using our CAPTCHA Solver! 
We hope this tool helps make your life a little bit easier. If you have any issues or suggestions, please don't hesitate to open an issue on our GitHub repository.
