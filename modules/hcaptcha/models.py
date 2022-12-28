from .utils import cache_forever
class Task:
    def __init__(self, task_obj, challenge=None):
        self.challenge = challenge
        self.key = task_obj["task_key"]
        self.url = task_obj["datapoint_text"]
    
    def _request(self, url, method="GET", http_client=None):
        http_client = http_client if http_client is not None \
                      else self.challenge.http_client
        return http_client.request(
            method,
            url,
            headers={"Accept-Encoding": "gzip, deflate, br"}
        )
    
    #@cache_forever()
    def content(self, **kw) -> bytes:
        resp = self._request(self.url, **kw)
        return resp.content
    


