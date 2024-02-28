# URL shortner using pyshorteners

import pyshorteners as py
from tkinter import *

win=Tk()
win.title('URL Shortener')
win.geometry('400x280')
win.configure(bg='#76EEC6')

def shorturl():
    url=placeholder1.get()
    s=py.Shortener().tinyurl.short(url)

    placeholder2.insert(END,s)
    

Label(win,text='Enter url',font='eurostile 20 bold',bg='#76EEC6',fg='black').pack(fill='x',pady=10)

placeholder1=Entry(win,font='10',bd=3,width=40)
placeholder1.pack(pady=20)

Button(win,text='Click Me',font='eurostile 12 bold',bg='#ABE89F',fg='black',width='6',command=shorturl).pack()

placeholder2=Entry(win,font='eurostile 16 bold',bg='#76EEC6',width='24',bd=0)
placeholder2.pack(pady=25)
win.mainloop()
