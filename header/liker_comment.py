#Liker and commment manager omg
import time
import random
from selenium.webdriver.common.keys import Keys

class likerCommentManager():


    comment_available = True
    LIMITS_COMMENTS = 0
    LIMITS_LIKE = 0
    LIMITS_FOLLOW = 0

    L_COMMENT = 0
    L_LIKE = 0
    L_FOLLOW = 0

    Retard_comment = 0
    test_like = 'Ya no me gusta'

    def __init__(self,driver,thechosenone,comments,id):
        self.id = id
        self.comments = comments
        self.driver = driver
        self.thechosenone = thechosenone

    def pass_strvar(self,likes_var,follow_var,comment_var):
        self.likes_var = likes_var
        self.follow_var = follow_var
        self.comment_var = comment_var

    def pass_limits(self,limits_like,limits_follow,limits_comment):
        self.LIMITS_LIKE = limits_like
        self.LIMITS_FOLLOW = limits_follow
        self.LIMITS_COMMENTS = limits_comment


    def like_f(self):
        driver = self.driver
        btn_pro = driver.find_element_by_xpath(
            "/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button")
        likes_btn = driver.find_elements_by_tag_name('span')
        likes_btn = list(set([elem.get_attribute('aria-label') for elem in likes_btn]))

        if self.test_like not in likes_btn:
            btn_pro.click()
            self.L_LIKE += 1
            self.likes_var.set(str(self.L_LIKE))
        else:
            return





    def comment_f(self):

        driver = self.driver
        if self.comment_available:
            try:
                btn_comment = driver.find_element_by_xpath("//span[@aria-label='Comentar']")
                btn_comment.click()

                comment_box_elem = driver.find_element_by_xpath("//textarea[@aria-label='Añade un comentario...']")
                comment_box_elem.clear()
                comment = random.choice(self.comments)

                for x in comment:
                    comment_box_elem.send_keys(x)
                    time.sleep(0.2)

                comment_box_elem.send_keys(Keys.RETURN)
                self.L_COMMENT += 1
                self.comment_var.set(str(self.L_COMMENT))


                #Comprobar si la wea se envio correctamente
                time.sleep(2)

                user_comments = driver.find_elements_by_tag_name('a')
                user_comments = list(set([elem.get_attribute('title') for elem in user_comments]))
                if not self.id in user_comments:
                    self.comment_available = False


            except:
                pass
        else:
            self.Retard_comment += 1
            time.sleep(2)
            if self.Retard_comment % 4 == 0:
                self.comment_available = True


    def check_end(self):
        if self.L_COMMENT >= self.LIMITS_COMMENTS and self.L_LIKE >= self.LIMITS_LIKE and self.L_FOLLOW >= self.LIMITS_FOLLOW:
            self.driver.close()
            return
        return

    def like_photos(self):

        driver = self.driver
        hrefs_in_view = driver.find_elements_by_tag_name('a')
        hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                         if '.com/p/' in elem.get_attribute('href')]
        time.sleep(2)


        # THIS FOR LOOP IS GOING TO LIKE EVERY PHOTO IN THE #HASHTAGS

        for x in hrefs_in_view:
            self.check_end()
            driver.get(x)
            btn_follow = driver.find_element_by_xpath("//button[@type='button']")

            if btn_follow.text == 'Siguiendo':
                try:
                    # COMMENT THE PHOTO
                    if self.L_COMMENT <= self.LIMITS_COMMENTS:

                        self.comment_f()


                    time.sleep(0.5)

                except:
                    continue
            else:
                #Follow that guy
                if self.L_FOLLOW <= self.LIMITS_FOLLOW:
                    btn_follow.click()
                    self.L_FOLLOW += 1
                    self.follow_var.set(str(self.L_FOLLOW))

                try:

                    # COMMENT THE PHOTO
                    if self.L_COMMENT <= self.LIMITS_COMMENTS:
                        self.comment_f()

                        if self.L_LIKE <= self.LIMITS_LIKE:
                            self.like_f()





                    time.sleep(0.5)

                except:
                    continue



