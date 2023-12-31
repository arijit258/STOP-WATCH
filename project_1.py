from tkinter import *
from datetime import datetime

counter=0
running=False

def Start():
    global running
    running=True
    count()
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def count():
    if running:
        global counter
        if counter==0:
            display='Ready!'
        else:
            tt=datetime.utcfromtimestamp(counter)
            display=tt.strftime('%H:%M:%S')
        label['text']=display
        label.after(1000,count)
        counter+=1


def Stop():
    global running
    running=False
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'

def Reset():
    global counter
    counter=0
    if not running:
        reset['state']='disabled'
    label['text']='00:00:00'

app=Tk()
app.minsize(width=250,height=70)
app.title('Stop Watch')

label=Label(app,text='Ready!', fg='black', font='Veradana 30 bold')
label.pack()
f=Frame(app)
start=Button(f,text='Start',width=6,command=Start)
stop=Button(f,text='Stop',width=6,command=Stop)
reset=Button(f,text='Reset',width=6,command=Reset)
f.pack(anchor='center',pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

app.mainloop()