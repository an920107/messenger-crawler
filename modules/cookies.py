import json
import pickle

class Cookies:

    '''
    The json file should be like this: `[{"name":"abc", "value":"123"}, {...}]`
    '''
    def __init__(self, filename: str) -> None:
        self.__filename = filename
        
        with open(filename, "r") as file:
            self.__cookies = json.load(file)

        if type(self.__cookies) != list:
            raise Exception("Json file format error")
        if type(self.__cookies[0]) != dict:
            raise Exception("Json file format error")

        for cookie in self.__cookies:
            if 'sameSite' in cookie:
                if cookie['sameSite'] not in ["Strict", "Lax"]:
                    cookie['sameSite'] = 'Strict'
                    
        self.__curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__curr >= len(self.__cookies):
            raise StopIteration()
        curr, self.__curr = self[self.__curr], self.__curr + 1
        return curr

    def __getitem__(self, key):
        return self.__cookies[key].copy()
