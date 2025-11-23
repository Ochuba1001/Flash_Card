from tkinter import *
import pandas
import random

COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("new_word.csv")
except FileNotFoundError:
    raw_file = pandas.read_csv("french_word.csv")
    to_learn = raw_file.to_dict(orient="records")
else:
    to_learn = data.to_dict('records')


def next_card():
    """returns the next card in the list"""
    global current_word
    global flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "French",fill="black")
    canvas.itemconfig(card_word, text=current_word['French'],fill="black")
    canvas.itemconfig(front_img,image = card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """changes the card to show the english word """
    canvas.itemconfig(card_title,text = "English",fill = "Blue")
    canvas.itemconfig(card_word, text=current_word['English'],fill = "Blue")
    canvas.itemconfig(front_img,image = card_back)

def is_known():
    """Remove the list of words the user knows"""
    to_learn.remove(current_word)
    pandas.DataFrame(to_learn).to_csv("new_word.csv",index = False)
    next_card()

window = Tk()
window.title("Flash Card")
window.minsize(350, 350)
window.config(padx=50, pady=50, bg=COLOR)
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526,bg=COLOR)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
front_img = canvas.create_image(400, 263,image=card_front)
card_title = canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic") , fill="black")
card_word = canvas.create_text(400,264,text="Word",font=("Ariel", 60, "bold") , fill="black")
canvas.config(bg=COLOR,highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)

# --------------------------- BUTTONS -------------- #

cross_img = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="right.png")
known_button = Button(image=check_img,highlightthickness=0,  command= is_known)
known_button.grid(column=1, row=1)

next_card()


window.mainloop()