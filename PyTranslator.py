from googletrans import *
import tkinter as tk
import pyttsx3

def trans():
    global speak
    x=txt.get()
    if x=="":
        print("nothing")
    translator=Translator()
    try:
        t=translator.translate(x)
        speak=t.text
        print(speak)
        tk.Label(root, text=speak,font="arial 16",bg='ghost white',padx=10,pady=10).place(x=200,y=150)
    except:
        print("wait for response")
        trans()  

def speech():
    engine=pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()

root=tk.Tk()
root.title("PyTranslator")
root.geometry("600x400")
txt=tk.StringVar()
root.config(bg='ghost white')
tk.Label(root, text = "PyTRANSLATOR", font = "arial 20 bold", bg='ghost white').pack()
tk.Label(root,text="Enter Sentence : ",bg='ghost white',font='arial 12').place(x=40,y=50)
tk.Entry(root,textvariable=txt,font='arial 12').place(x=200,y=50)
tk.Button(root,text = "Translate", command=trans).place(x=215,y=100)
tk.Button(root,text= "Speech" , command=speech).place(x=285,y=100)
tk.Label(root,text ="By Ankit Ram Nag", font = 'arial 11', bg ='ghost white' , width = '20').pack(side = 'bottom')
root.mainloop()