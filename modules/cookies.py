import json

class Cookies:

    '''
    The json file should be like: `[{"name": "123", "value": "abc", ...}, {...}]`
    '''
    def __init__(self, filename: str) -> None:
        self._filename = filename
        
        with open(filename, "r") as file:
            self._cookies = json.load(file)

        if type(self._cookies) != list:
            raise Exception("Json file format error")
        if type(self._cookies[0]) != dict:
            raise Exception("Json file format error")

        for cookie in self._cookies:
            if 'sameSite' in cookie:
                if cookie['sameSite'] not in ["Strict", "Lax"]:
                    cookie['sameSite'] = 'Strict'
                    
        self._curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr >= len(self._cookies):
            raise StopIteration()
        curr, self._curr = self[self._curr], self._curr + 1
        return curr

    def __getitem__(self, key):
        return self._cookies[key].copy()
