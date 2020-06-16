import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import smtplib
import pyttsx3
import winsound
import engineio
import string
from random import randint
engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    
engineio.setProperty('voice',voices[0].id)
frequency=4500
duration=150
def speak(text):
    engineio.say(text)
    engineio.runAndWait()

#speak("hello world")


# creating root object
root = Tk()

# defining size of window
root.geometry("1350x680")
C = Canvas(root, bg="blue", height=175, width=300)
filename = PhotoImage(file = "C://Users//Personal//Pictures//hhhh.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# setting up the title of window
root.title("MED:A NEW MODEL FOR MESSAGE ENCRIPTION AND DECRIPTER USING ALIEN KEY")
Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)
f1 = Frame(root, width = 800, height = 700,relief = SUNKEN)
f1.pack(side = LEFT)

# ==============================================
# TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font = ('helvetica', 30, 'bold'),
text = "MED: Message Encrypter and Decripter using ALIEN KEY",
fg = "Black", bd = 10, anchor='w')

lblInfo.grid(row = 0, column = 0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
text = localtime, fg = "Steel Blue",
bd = 10, anchor = 'w')

lblInfo.grid(row = 1, column = 0)


speak("MED A NEW MODEL FOR MESSAGE ENCRIPTION AND DECRIPTER USING ALIEN KEY")

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
enc= StringVar()
kdec=StringVar()
# exit function
def qExit():
    speak("Are you sure you want to exit?")
    x=messagebox.askquestion("Confirm","Are you sure you want to exit?")
    if(x=='yes'):
        root.destroy()

# Function to reset the window
def Reset():
    rs=messagebox.askokcancel("RESET ???","Are you sure?")
    if rs==True:
        rand.set("")
        Msg.set("")
        key.set("")
        mode.set("")
        Result.set("")
        enc.set("")
        kdec.set("")
        z=0

lblMail= Label(f1, font = ('arial', 16, 'bold'),
text = "Enter destination(mail id)",bd = 16,anchor = "w")

lblMail.grid(row = 1, column = 1)

txtMail= Entry(f1, font = ('arial', 16, 'bold'),
textvariable = rand, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtMail.grid(row = 1, column = 2)
# labels
lblMsg = Label(f1, font = ('arial', 16, 'bold'),
text = "enter plaintext", bd = 16, anchor = "w")

lblMsg.grid(row = 2, column = 1)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
textvariable = Msg, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtMsg.grid(row = 2, column = 2)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
text = "KEY", bd = 16, anchor = "w")

lblkey.grid(row = 3, column = 1)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),
textvariable = key, show='*',bd=10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtkey.grid(row = 3, column = 2)


lblenc = Label(f1, font = ('arial', 16, 'bold'),
text = "Enter cipertext ",
bd = 16, anchor = "w")

lblenc.grid(row = 1, column = 4)

txtenc = Entry(f1, font = ('arial', 16, 'bold'),
textvariable = enc, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtenc.grid(row = 1, column = 5)

lblkdec= Label(f1, font = ('arial', 16, 'bold'),
text = "Enter the key for decryption",
bd = 16, anchor = "w")

lblkdec.grid(row = 2, column = 4)

txtkdec= Entry(f1, font = ('arial', 16, 'bold'),
textvariable = kdec, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtkdec.grid(row =2, column = 5)

lblService = Label(f1, font = ('arial', 16, 'bold'),
text = "message", bd = 8, anchor = "w")

lblService.grid(row = 3, column = 4)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
textvariable = Result, bd = 10, insertwidth = 4,
bg = "LightSkyBlue1", justify = 'right')

txtService.grid(row = 3, column = 5)
import base64
# Function to encode
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i])+ord(key_c)) % 256)
        enc.append(enc_c)
        r=base64.urlsafe_b64encode("".join(enc).encode()).decode()
    return r

# Function to decode
def decode(kdec, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = kdec[i % len(kdec)]
        dec_c = chr((256 + ord(enc[i])-ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
z=0
def dummy():
    z=1
    if(z):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            winsound.Beep(frequency,duration)
            print("Speak:")
            audio = r.listen(source)
        try:
            print("You said:" + r.recognize_google(audio))
        except sr.UnknownValueError:
            speak("Pardon me, I could'nt understand you..!")
        except sr.RequestError as e:
            return r.recognize_google(audio)
    else: return Msg.get()

       
def Ref():
       # print("Message= ", (Msg.get()))
        clear = dummy()
        v = rand.get()
        k = key.get()
        m = mode.get
        i=randint(1,1000000000000)
        c=str(i)+random.choice(string.ascii_letters)
        k=k+c
        if(v.find('@gmail.com')!=-1 or v.find('yahoo.com')!=-1) or (v.find('@outlook.com')!=-1) or (v.find('@hotmail.com')!=-1):
            msg=encode(k, clear)+"       key="+k
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("cse2aliet@gmail.com", "CSE2ALIET")
            server.sendmail("cse2aliet@gmail.com", v, msg)
            server.quit()
        #messagebox.showwarning("warning","Warning")
            speak("mail sent")
            messagebox.showinfo("server status","message sent")
        else:
            speak("warning  incorrect destination adress")
            messagebox.showwarning("warning","incorrect destination adress")        
def dcode():
    s=decode(kdec.get(), enc.get())
    speak(s)
    Result.set(decode(kdec.get(), enc.get()))
#if(lblMail==NONE and lblMsg==NONE and lblkey==NONE):
   
 #   messagebox.showwarning("warning","Warning")
#encrypt and mail sending button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
font = ('arial', 16, 'bold'), width = 10,
text = "send message", bg = "SteelBlue3",
command = Ref).grid(row = 7, column = 2)

#voice button
btnmic= Button(f1, padx = 8, pady = 4, bd = 8,fg = "black", font = ('arial', 8, 'bold'),
width = 5, bg = "light cyan", text="MIC",
command = dummy).grid(row = 2, column = 3)


#Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
font = ('arial', 16, 'bold'), width = 10,
text = "Show Message", bg = "SteelBlue3",
command = dcode).grid(row = 7, column = 5)

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
fg = "black", font = ('arial', 16, 'bold'),
width = 10, text = "Reset", bg = "green",
command = Reset).grid(row = 8, column = 3)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
fg = "black", font = ('arial', 16, 'bold'),
width = 10, text = "Exit", bg = "red",
command = qExit).grid(row = 8, column = 4)

# keeps window alive
root.mainloop()
