from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()
window.geometry("700x700")
window.title("Typing Speed Test")
window.config(background="light blue")
window.resizable(False, False)

 
def type_speed_test():
      j=error=0
      ans=user_input.get("1.0",'end-1c')
      end=timer()
      time_taken=end-start
      for i in range(min(len(words[word]), len(ans))):
        if words[word][i] != ans[i]:
            error += 1

      wpm = (len(ans)- error) / 5 / (time_taken / 60)
      wpm = int(wpm)

      result_label.config(text="Your Score is: {} WPM".format(wpm))
      if not words[word].startswith(ans):
        user_input.config(fg="red")
      else:
        user_input.config(fg="green")
                 

words = ["Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
        "Don’t walk in front of me I may not follow Don’t walk behind me I may not lead Walk beside me… just be my friend",
        "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
        "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that.",
        "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.",
        "I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
        "It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all—in which case, you fail by default."]

word=random.randint(0,(len(words)-1))


title = Label(window, text="Let's test your typing speed!", background="light blue", foreground="black", font=("Arial", 18, "bold"))
title.pack(anchor="center", pady=20)

x1=Label(window,text=words[word],bg="black",fg="white",height=7,width=47,font="Arial",wraplength=500)
x1.place(x=80,y=80)

user_input=Text(window)
user_input.place(x=100,y=260,height=130,width=500)


b1=Button(window,text="Submit!",font="Arial",bg="red",command=type_speed_test)
b1.place(x=280,y=440)

result_label = Label(window, text="", font=("Arial", 16))
result_label.place(x=240, y=550)



start=timer()

window.mainloop()




    
   
