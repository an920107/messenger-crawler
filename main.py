import undetected_chromedriver as uc
import os
import time

from modules.cookies import Cookies


def main():
    
    chrome = uc.Chrome()
    url = "https://www.messenger.com/"

    cookies = Cookies(os.path.abspath("data/cookies.json"))

    chrome.get(url)
    chrome.delete_all_cookies()
    for cookie in cookies:
        chrome.add_cookie(cookie)
    chrome.get(url)
        



    time.sleep(10)


if __name__ == "__main__":
    main()