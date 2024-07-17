import time
import urllib
from random import randint
from typing import Dict, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WhatsappManager:
    def __init__(self, actions: "List[Dict[str, str] | None]"):
        self.driver = webdriver.Chrome()
        self.wait_login()
        self.send_messages(actions)
        self.close()
    
    def wait_login(self):
        self.driver.get("https://web.whatsapp.com/")
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'selectable-text'))
        )
    
    @staticmethod
    def encrypt_url_safe(text):
        # Codifica o texto para URL
        encrypted_string = urllib.parse.quote(text)
        return encrypted_string

    def send_messages(self, actions):
        base_url = "https://web.whatsapp.com/send?phone={}&text={}"
        for action in actions:
            message = self.encrypt_url_safe(action.get('message'))
            phone = action.get('phone')
            self.driver.get(base_url.format(phone, message))
            time.sleep(randint(10, 20))
            self.driver.find_element(
                By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
            ).click()
    
    def close(self):
        self.driver.close()
