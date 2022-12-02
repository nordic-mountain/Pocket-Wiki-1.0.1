#
from tkinter import *
import wikipedia
from tkinter.ttk import Entry
from tkinter.ttk import Button

#window
window_root = Tk()
text_varible = StringVar()
logo = PhotoImage(file="C:\\Users\\Gianclarence Solas\\Desktop\\Mini Wikipedia\\images\\Wikipedia-Logo-PNG3.png")

#setup
window_root.title("Mini Wiki")
window_root.geometry("1100x800")
window_root.iconphoto(False, logo)

#main
def logo():
    lbl_logo = Label(text="Mini Wiki", font=("Arial", 30))
    lbl_logo.pack()
    
def Search_bind():
    def clicked():
        get_text_varible = text_varible.get()
        Tex.pack(fill=BOTH)
        window_root.configure(Tex.delete('1.0', END))
        window_root.configure(Tex.insert(END, wikipedia.summary(get_text_varible)))
    ent_search = Entry(textvariable=text_varible, font=("Arial", 27), width=20)
    btn_search = Button(text="🔍", width=27, command=clicked)
    ent_search.pack()
    btn_search.pack()
    Tex = Text(window_root, height = 40, width = 200)

def text_words(text):
    text = Label(text=text, font=("Quicksand Bold", 10), bg=None, fg="#4fc3f7")
    text.pack()

def change_set(emotion, x, y):
    window_root.config(text_words(emotion, x, y))
        
#bindings
logo()
Search_bind()

#mainloop
window_root.mainloop()