import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import json

from modules.chrome import Chrome
from modules.cookies import Cookies
from modules.chatgpt import ChatGPT


def main():
    
    URL = "https://www.messenger.com/"

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    chrome = Chrome(options=options)
    chrome.set_window_size(1600, 1000)

    cookies = Cookies(os.path.abspath("data/cookies.json"))
    chatgpt = ChatGPT(os.path.abspath("data/gptconfig.json"))
    whitelist = json.load(open("data/whitelist.json", encoding="UTF8"))

    # 開啟 messenger 並用 cookie 登入
    chrome.get(URL)
    chrome.delete_all_cookies()
    for cookie in cookies:
        chrome.add_cookie(cookie)
    chrome.get(URL)

    while True:

        # 取得未讀訊息的藍色點點
        try:
            unread_elements = chrome.find_elements_and_wait(By.XPATH, "//*[@aria-label='標示為已讀']")
        except:
            continue
        for element in unread_elements:
            # 聊天室預覽框框
            chatroom_box_element = element.find_element(By.XPATH, "../../../..")
            # 聊天室名稱
            chatroom_name = chatroom_box_element.find_element(By.XPATH, "div[2]/div/div/span/span").text
            # 聊天室最新訊息
            chatroom_message = chatroom_box_element.find_element(By.XPATH, "div[2]/div/div/span/div[2]/span/span").text
            # 進入聊天室
            continue_flag = True
            if chatroom_name in whitelist["person"]:
                continue_flag = False
            if chatroom_name in whitelist["group"]:
                chatroom_message = chatroom_message[chatroom_message.find(": ") + 2:]
                continue_flag = False
            if chatroom_message.find("對你的訊息") > -1:
                continue_flag = True
            if continue_flag:
                continue
            chatroom_box_element.click()
            # 訊息輸入框
            message_textbar_element = chrome.find_element_and_wait(By.XPATH, "//*[@aria-label='訊息']")
            message_textbar_element.click()
            message_textbar_element.send_keys(chatgpt.post(chatroom_message))
            message_textbar_element.send_keys(Keys.RETURN)
            time.sleep(1)

            chrome.get(URL)
            # chrome.back()
            break

    time.sleep(1000)


if __name__ == "__main__":
    main()