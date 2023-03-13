import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

from modules.chrome import Chrome
from modules.cookies import Cookies


def main():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    chrome = Chrome(options=options)
    chrome.set_window_size(1600, 1000)

    url = "https://www.messenger.com/"
    cookies = Cookies(os.path.abspath("data/cookies.json"))

    # 開啟 messenger 並用 cookie 登入
    chrome.get(url)
    chrome.delete_all_cookies()
    for cookie in cookies:
        chrome.add_cookie(cookie)
    chrome.get(url)

    # 取得未讀訊息的藍色點點
    unread_elements = chrome.find_elements_and_wait(By.XPATH, "//*[@aria-label='標示為已讀']")
    for element in unread_elements:
        # 聊天室預覽框框
        chatroom_box_element = element.find_element(By.XPATH, "../../../..")
        # 聊天室名稱
        chatroom_name = chatroom_box_element.find_element(By.XPATH, "div[2]/div/div/span/span").text
        # 聊天室最新訊息
        chatroom_message = chatroom_box_element.find_element(By.XPATH, "div[2]/div/div/span/div[2]/span/span").text

        chatroom_box_element.click()

        # 訊息輸入框
        message_textbar_element = chrome.find_element_and_wait(By.XPATH, "//*[@aria-label='訊息']")
        message_textbar_element.click()
        message_textbar_element.send_keys("test")
        message_textbar_element.send_keys(Keys.RETURN)
        continue
        


    # time.sleep(5)
    # unreads = 
    # for element in unreads:
    #     print(element)

    
    time.sleep(1000)


if __name__ == "__main__":
    main()