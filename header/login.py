#Basic configurations of the bot
import time
from selenium.webdriver.common.keys import Keys

class login_manager():

    def __init__(self,driver,username,password):
        self.driver = driver
        self.username = username
        self.password = password

    def enter_ins(self):
        #Enter to instagram

        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        #Button to login
        lgbutton = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        lgbutton.click()
        time.sleep(2)

        #Put the username
        user = driver.find_element_by_xpath("//input[@name='username']")
        user.clear()
        user.send_keys(self.username)

        #Put the Password and finally press enter
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)