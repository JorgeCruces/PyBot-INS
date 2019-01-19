#Hashtags Finder Py Class
import random
import time


class hashtags_manager():

    def __init__(self,driver,list_h):
        self.driver = driver
        self.list_h = list_h

    def search_web(self):
        list = self.list_h
        if list != []:
            thehastag = random.choice(list)
            list.remove(thehastag)
            web = "https://www.instagram.com/explore/tags/" + thehastag
            self.driver.get(web)
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            return thehastag
        else:
            return "FALTAN"








