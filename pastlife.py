import random
from random import choice
import tkinter as tk


rel = ["Brother","wife","Mother","Father","son","Husband","dauhter","grandpa","grandma","nephew","niece","Boyfriend","Girlfriend"]

def cal():
    choice = random.choice(rel)
    a.configure(text = f"Your friend was your {choice}")

font = ("verdana",15,"bold")

root = tk.Tk()
root.geometry("400x300")
root.title("Past Life Relation")
name1 = tk.StringVar
root.configure(bg="black")
e1 = tk.Entry(root,textvariable=name1())
e1.place(x=20,y=40)
e2 = tk.Entry(root)
e2.place(x=220,y=40)

a = tk.Label(root,text = 'Find relation b/w you & your friend or any person you know from the past life :)',font=font,fg="white",bg="black")
a.place(x=10,y=80)

b = tk.Button(root,text ="Find Relation",fg="black",bg="yellow",command=cal)
b.place(x=150,y=250)

root.mainloop()