from tkinter import *
from tkinter import messagebox as MessageBox
from main import InstagramBot
import threading
import datetime

#Ahora label para mostrar texto
root = Tk()
root.resizable(0,0)
root.title("BoTINS")
root.iconbitmap("Ico.ico")
root.config(bd=15)






imagen = PhotoImage(file="new.png")
user = StringVar()
password = StringVar()
limit_likes = StringVar()
limit_follow = StringVar()
limit_comment = StringVar()
hashtags = StringVar()
current_like = StringVar()
current_follow = StringVar()
current_comment = StringVar()

current_time = StringVar()




current_like.set("0")
current_follow.set("0")
current_comment.set("0")


class close:
   close = False
   thread = 0

close_manager = close()



def stop():
   MessageBox.showerror("STOP", "STOPPING THE BOT")
   btn_send.config(text='Ready!!')
   btn_send.config(command=start)


def start():

      if hashtags.get() == '':
         MessageBox.showerror("Nothing", "Fill all the fields")
         return

      if not limit_follow.get().isdigit() or not limit_follow.get().isdigit() or not limit_comment.get().isdigit():
         MessageBox.showerror("Limits", "Not valid Limits,try again")
         return
      c = datetime.datetime.now()
      c = c.strftime("20%y/%m/%d  %I:%M:%S  ")

      current_time.set(c)

      MessageBox.showinfo("Ready","THE BOT IS RUNNING")
      btn_send.config(text='Stop!')
      btn_send.config(command=stop)
      send()





def send():


      comments = ["Good post!", "Awesome", "Nice Photo", "U look so good",
                  "Good photo, Greetings from California",
                  "Nice post!", "Amazing", "Wonderful", "Beautiful", "That's Great", "Wow", "Nice one!"]

      username = user.get()
      email_pass = password.get()
      list_hashtags = hashtags.get().split(',')

      newbot = InstagramBot(username,email_pass,list_hashtags,comments,username)
      newbot.pass_stringvar(current_like,current_follow,current_comment)
      newbot.pass_limits(limit_likes.get(),limit_comment.get(),limit_follow.get())

      while True:
            newbot.login()
            newbot.find_hashtags_page()
            newbot.find_photos_tolike()

      newbot.closeBrowser()




title_label = Label(root,text="INSTAGRAM BOT",font="Verdana")
title_label.grid(row=0,column=2,sticky='w',padx=5,pady=5)
img_label = Label(root,image=imagen)
img_label.grid(row=0,column=1,sticky='w',padx=5,pady=5)

               #USERNAME
username_label = Label(root,text="Username (NOT EMAIL)")
username_label.grid(row=1,column=1,sticky='w',padx=5,pady=5)

username_entry = Entry(root,textvariable=user)
username_entry.grid(row=1,column=2,padx=5,pady=5)
username_entry.config(justify='center',width=30)
               #PASSWORD
password_label = Label(root,text="Password")
password_label.grid(row=2,column=1,sticky='w',padx=5,pady=4)

password_entry = Entry(root,textvariable=password)
password_entry.grid(row=2,column=2,padx=5,pady=4)
password_entry.config(justify='center',show='*',width=30)

             #LIKE LIMITS
limitlike_label = Label(root,text="Like Limits")
limitlike_label.grid(row=3,column=1,sticky='w',padx=5,pady=4)

limitlike_label_suggest = Label(root,text="      Suggest( <100 )",justify="center")
limitlike_label_suggest.grid(row=3,column=2,sticky='e',padx=3,pady=4)

limitlike_label = Entry(root,textvariable=limit_likes)
limitlike_label.grid(row=3,column=2,padx=5,pady=4,sticky='w')
limitlike_label.config(justify='center',width=14)
             #FOLLOW LIMITS
limitfollow_label = Label(root,text="Follow Limits")
limitfollow_label.grid(row=4,column=1,sticky='w',padx=5,pady=4)

limitfollow_label_suggest = Label(root,text=" Suggest( <200 )",justify="center")
limitfollow_label_suggest.grid(row=4,column=2,sticky='e',padx=3,pady=4)

limitfollow_label = Entry(root,textvariable=limit_follow)
limitfollow_label.grid(row=4,column=2,padx=5,pady=4,sticky='w')
limitfollow_label.config(justify='center',width=14)
             #COMMENT LIMITS

limitcomment_label = Label(root,text="Comment Limits")
limitcomment_label.grid(row=5,column=1,sticky='w',padx=5,pady=4)

limitcomment_label_suggest = Label(root,text="Suggest(   <50 )",justify="center")
limitcomment_label_suggest.grid(row=5,column=2,sticky='e',padx=3,pady=4)

limitcomment_label = Entry(root,textvariable=limit_comment)
limitcomment_label.grid(row=5,column=2,padx=5,pady=4,sticky='w')
limitcomment_label.config(justify='center',width=14)
               #HASHTAGS

Hashtags_label = Label(root,text="Hashtags (separated by comma):")
Hashtags_label.grid(row=6,column=1,sticky='w',padx=5,pady=4)

Hashtags_label = Entry(root,textvariable=hashtags)
Hashtags_label.grid(row=6,column=2,padx=5,pady=4,sticky='w')
Hashtags_label.config(justify='center',width=30)

               #LIKE MADES
likemade_label = Label(root,text="Likes mades: ")
likemade_label.grid(row=7,column=1,sticky='w',padx=5,pady=4)

likemade_entry = Entry(root,textvariable = current_like,state='readonly')
likemade_entry.grid(row=7,column=2,padx=5,pady=4)
likemade_entry.config(justify='center',width=20)


               #FOLLOW MADES
followmade_label = Label(root,text="Follow mades: ")
followmade_label.grid(row=8,column=1,sticky='w',padx=5,pady=4)

followmade_entry = Entry(root,textvariable=current_follow,state='readonly')
followmade_entry.grid(row=8,column=2,padx=5,pady=4)
followmade_entry.config(justify='center',width=20)

                #COMMENT MADES
commentmade_label = Label(root,text="Comment mades: ")
commentmade_label.grid(row=9,column=1,sticky='w',padx=5,pady=4)

commentmade_entry = Entry(root,textvariable=current_comment,state='readonly')
commentmade_entry.grid(row=9,column=2,padx=5,pady=4)
commentmade_entry.config(justify='center',width=20)

                #BOT START AT
commentmade_label = Label(root,text="BOT START AT: ")
commentmade_label.grid(row=6,column=3,padx=5,pady=4)

commentmade_entry = Entry(root,textvariable=current_time,state='readonly')
commentmade_entry.grid(row=7,column=3,padx=6,pady=4,sticky='w')
commentmade_entry.config(justify='center',width=30)
   #BOT ENDS AT
commentmade_label = Label(root,text="BOT ENDS AT: ")
commentmade_label.grid(row=8,column=3,padx=5,pady=4)

commentmade_entry = Entry(root,state='readonly')
commentmade_entry.grid(row=9,column=3,padx=6,pady=4,sticky='w')
commentmade_entry.config(justify='center',width=30)







btn_send = Button(root,text="Ready!",command=start)
btn_send.grid(row=10,column=2)






#Abajo del todo
root.mainloop()

