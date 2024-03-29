import undetected_chromedriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from typing import List

    
class Chrome(webdriver.Chrome):

    def find_elements_and_wait(self, by: By, value: str, millisecond: float = 10000) -> List[webdriver.WebElement]:
        elements = WebDriverWait(self, millisecond / 1000).until(
            expected_conditions.presence_of_all_elements_located((by, value))
        )
        return elements

    def find_element_and_wait(self, by: By, value: str, millisecond: float = 10000) -> webdriver.WebElement:
        return self.find_elements_and_wait(by, value, millisecond)[0]