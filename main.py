import random
import tkinter
import pandas
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

#------------------------access-data----------------------------
choice= {}
words_to_learn={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origin_data = pandas.read_csv("data/french_words.csv")
    words_to_learn =origin_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")

# ------------------------right-button-------------------------------
def right_button():
    global choice
    words_to_learn.remove(choice)
    write_data=pandas.DataFrame(words_to_learn)
    write_data.to_csv("data/words_to_learn.csv")
    wrong_button()

# ------------------------wrong-button-------------------------------
def wrong_button():
    global choice
    choice = random.choice(words_to_learn)
    canvas.itemconfig(text1, text="French")
    canvas.itemconfig(text2, text=choice["French"])
    canvas.itemconfig(image, image=old_img)
    window.after(3000, func=flip)

#-------------------------flip-card---------------------------------
def flip():
    canvas.itemconfig(image, image=new_img)
    canvas.itemconfig(text1, text="English")
    canvas.itemconfig(text2, text=choice["English"])

# ------------------------make-the-window---------------------------
window=tkinter.Tk()
window.title("Flashy")
window.config(pady=50,padx=50, bg=BACKGROUND_COLOR)

canvas=tkinter.Canvas(width=800,height=526, bg=BACKGROUND_COLOR)

new_img= PhotoImage(file="images/card_front.png")
old_img= PhotoImage(file="images/card_back.png")
image=canvas.create_image(400,263,image=old_img)
text1=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
text2=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

right=PhotoImage(file="images/right.png")
button_right=tkinter.Button(image=right,command=right_button, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
button_right.grid(column=1,row=1)

wrong=PhotoImage(file="images/wrong.png")
button_wrong=tkinter.Button(image=wrong,command=wrong_button, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
button_wrong.grid(column=0,row=1)

wrong_button()

window.mainloop()