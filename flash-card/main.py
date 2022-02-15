from tkinter import *

import pandas
import random
data=pandas.read_csv("data/french_words.csv")
new_d=data.to_dict(orient="record")
BACKGROUND_COLOR = "#B1DDC6"
r_choice={}
def next_card():
    global r_choice,t_f
    window.after_cancel(t_f)
    r_choice=random.choice(new_d)

    canva.itemconfig(c_title,text="French",fill="black")
    canva.itemconfig(c_word,text=r_choice["French"],fill="black")
    t_f=window.after(3000, func=flip_card)

def flip_card():
    canva.itemconfig(c_title,text="English",fill="white")
    canva.itemconfig(c_word,text=r_choice["English"],fill="white")
    canva.itemconfig(car_back,image=car_b_img)

def unknown_c():
    new_d.remove(r_choice)
    next_card()
    data=pandas.DataFrame(new_d)
    data.to_csv("data/word_to_learn.csv")



window=Tk()
window.title("flash-Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
t_f=window.after(3000,func=flip_card)

canva=Canvas(width=800,height=526)
front_img=PhotoImage(file="images/card_front.png")
car_b_img=PhotoImage(file="images/card_back.png")
car_back=canva.create_image(400,263,image=front_img)
c_title=canva.create_text(400,150,text="Title",font=("Arial",40,"italic"))
c_word=canva.create_text(400,263,text="word",font=("Arial",40,"bold"))
canva.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canva.grid(row=0,column=0,columnspan=2)
bu=PhotoImage(file="images/wrong.png")
unknown_b=Button(image=bu,highlightthickness=0,command=next_card)
unknown_b.grid(row=1,column=0)

corr=PhotoImage(file="images/right.png")
check_b=Button(image=corr,highlightthickness=0,command=unknown_c)
check_b.grid(row=1,column=1)



window.mainloop()
