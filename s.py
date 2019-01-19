from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import random
import time

class InstagramBot:
    
    def __init__(self,username = None,password = None):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome();

    def closeBrowser(self):
        self.driver.close()

    def login(self):
            #"//a[@href'accounts/login']"
            #"//input[@name='username']"
            #"//input[@name='password']"
            driver = self.driver
            driver.get("https://www.instagram.com/")
            time.sleep(2)
            lgbutton = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            lgbutton.click()
            time.sleep(2)
            user = driver.find_element_by_xpath("//input[@name='username']")
            user.clear()
            user.send_keys(self.username)
            password = driver.find_element_by_xpath("//input[@name='password']")
            password.clear()
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(2)

    def ctn(self, lista,comments):
        self.lista = lista
        self.comments = comments

        driver = self.driver
        for x in lista:
            driver.get(x)
            time.sleep(2)
            btn_comment = driver.find_element_by_xpath("//span[@aria-label='Comentar']")
            btn_comment.click()

            comment_box_elem = driver.find_element_by_xpath("//textarea[@aria-label='Añade un comentario...']")
            comment_box_elem.clear()
            comment_box_elem.send_keys(random.choice(comments));
            time.sleep(2)
            comment_box_elem.send_keys(Keys.RETURN);







jorgito = InstagramBot("beatifullife.company@gmail.com","88020361")

lista = input("Porfavor introduzca los links separados por coma: ")
comments = ["Good post bro, i really like it","Nice pic, i love it","You should check out our online store it's like this photo, beautiful","Love yourself bro, that pic it's so pretty <3", "Nice one akdlas good job"]

lista = lista.split(",")
print("Sus links: ",lista)

jorgito.login()


jorgito.ctn(lista,comments)

