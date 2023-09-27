from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.onelink.me/9K8a/3d4abb81')
        sleep(2)
        
        fb_btn = self.driver.find_element(by=By.XPATH, value='//button//div[contains(text(), "Entrar com Facebook")]')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element(by=By.XPATH, value='//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element(by=By.XPATH, value='//input[@value="Entrar"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)
        
        cookies_btn = self.driver.find_element(by=By.XPATH, value='//button//div[contains(text(), "Recusar")]')
        # Clique no botão "Recusar"
        cookies_btn.click()  
        
        sleep(6)
        permitir_btn = self.driver.find_element(by=By.CSS_SELECTOR, value='button[data-testid="allow"]')
        # Clique no botão "Permitir"
        permitir_btn.click() 
        
        sleep(1)
        ativar_btn = self.driver.find_element(by=By.CSS_SELECTOR, value='button[data-testid="allow"]')
        # Clique no botão "Ativar"
        ativar_btn.click() 


    def like(self):
        like_btn = self.driver.find_element(by='xpath', value='//button//span[text()="Curti"]')
        self.driver.execute_script("arguments[0].click();", like_btn)


    def dislike(self):
        dislike_btn = self.driver.find_element(by='xpath', value='//button//span[text()="Não"]')
        self.driver.execute_script("arguments[0].click();", dislike_btn)


    def auto_swipe(self):   
        from random import random
        while True:
            sleep(0.5)
            rand = random()
            if rand < 1:
                self.like()
            else:
                self.dislike()            

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
print("Login realizado com sucesso")
sleep(3)
bot.auto_swipe()