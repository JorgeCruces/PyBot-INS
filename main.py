from selenium import webdriver
from header.login import login_manager
from header.hashtags import hashtags_manager
from header.liker_comment import likerCommentManager

import getpass
import time


class InstagramBot:

    hrefs_in_view = []
    thechosenone = ""

    def __init__(self,username = None,password = None,hashtags = [],comments = [],id =None):
        self.id = id
        self.comments = comments
        self.hashtags = hashtags
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()


    def pass_stringvar(self,str_like,str_follow,str_comment):
        self.str_like = str_like
        self.str_follow = str_follow
        self.str_comment = str_comment
    def pass_limits(self,limits_likes,limits_follow,limits_comment):
        self.limits_likes = int(limits_likes)
        self.limits_follow = int(limits_follow)
        self.limits_comment = int(limits_comment)



    def closeBrowser(self):
        self.todobien = False
        self.driver.close()

    def login(self):
        log = login_manager(self.driver,self.username,self.password)
        login_manager.enter_ins(self)


    def find_hashtags_page(self):

                    #FIND THE HASHTAGS PAGES


        manager_hashtags = hashtags_manager(self.driver,self.hashtags)
        self.thechosenone = manager_hashtags.search_web()

                    #CODE FOR THE POSSIBLE ENDS OF HASHTAGS
        if self.thechosenone == "FALTAN":
            pass




    def find_photos_tolike(self):
            liker_comment = likerCommentManager(self.driver,self.thechosenone,self.comments,self.id)
            liker_comment.ready = False
            liker_comment.pass_strvar(self.str_like,self.str_follow,self.str_comment)
            liker_comment.pass_limits(self.limits_likes,self.limits_comment,self.limits_follow)
            liker_comment.like_photos()










comments = ["Good post!","Awesome","Nice Photo","Buena foto, Saludos desde Chile","Good photo, Greetings from Chile",
            "Nice post!","Amazing","Wonderful","Beautiful","That's Great","Wow","Nice one!"]





