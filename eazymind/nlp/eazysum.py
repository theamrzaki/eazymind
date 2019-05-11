import requests

class Summarizer(object):
    def __init__(self,key):
        self.key = key
        self.url = "http://eazymind.herokuapp.com/arabic_sum/eazysum"

    def run(self, sentence):
        payload = "key="+self.key +"&sentence="+sentence+""
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            }
        response = requests.request("POST", self.url, data=payload, headers=headers)
        return response.text
   