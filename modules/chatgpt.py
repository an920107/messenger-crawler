import requests
from requests.auth import HTTPBasicAuth
import json
import re


class ChatGPT:


    '''
    The json file should be like: `{"key": "abc123", ...}`
    '''
    def __init__(self, filename: str) -> None:
        self._filename = filename
        
        with open(filename, "r", encoding="UTF8") as file:
            self._config_dict = json.load(file)

        self._auth = HTTPBasicAuth("Bearer", self._config_dict["key"])
        
        

    def post(self, text: str) -> str:

        URL = "https://api.openai.com/v1/chat/completions"

        self._config_dict["config"]["messages"][0]["content"] = \
            self._config_dict["prefix"] + "\n" + text
        response = requests.post(URL, json=self._config_dict["config"], auth=self._auth)
        
        print(response.text)
        
        response_text = re.search(r"\"content\":\".*?\"", response.text).group()
        response_text = response_text[11:-1]
        # while response_text.find("\\\\n") > -1:
        #     response_text = response_text.replace("\\\\n", "\n")
        response_text = re.sub(r"(\\n)+", "\n", response_text)
        response_text = re.sub(r"(\\\\n)+", "\n", response_text)

        if response_text[0] in ["，", "。", "！", "？"]:
            response_text = response_text[1:]

        return response_text