from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES




root=Tk()
root.geometry("1080x400")
language=list(LANGUAGES.values())

label1=Label(root,text="LANGUAGE TRANSLATOR")
label1.place(relx=0.5,rely=0.1,anchor=CENTER)


label2=Label(root,text="Enter Text")
label2.place(relx=0.02,rely=0.2,anchor=W)

a=Text(root,height=11,wrap=WORD)
a.place(relx=0.02,rely=0.5,anchor=W)
    
c1=ttk.Combobox(root,values=language,width=22,state="readonly")
c1.place(relx=0.13,rely=0.2,anchor=W)
c1.set("english")

label3=Label(root,text="Output")
label3.place(relx=0.81,rely=0.2,anchor=E)

c2=ttk.Combobox(root,values=language,width=22,state="readonly")
c2.place(relx=0.98,rely=0.2,anchor=E)
c2.set("choose output language")

a2=Text(root,height=11,wrap=WORD)
a2.place(relx=0.98,rely=0.5,anchor=E)

btn= Button(root,text="Translate",  fg="white",bg="dark blue")
btn.place(relx=0.5,rely=0.85,anchor=CENTER)



root.mainloop()