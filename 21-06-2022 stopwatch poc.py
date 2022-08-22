import tkinter as tink
count= -1
run=False
def var_name(mark):
    def value():
        if run:
            global count
            if count== -1:
                show='starting'
            else:
                show=str(count)
            mark['text']=show

            mark.after(1000,value)
            count+= 1
    value()

def Start(mark):
    global run
    run=True
    var_name(mark)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'


def Stop():
    global run
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    run=False

def Reset(label):
    global count
    count= -1
    if run==False:
        reset['state']='disabled'
        mark['text']='welcome'
    else:
        mark['text']='start'

base=tink.Tk()
base.title("stop watch")
base.geometry("300x300")
base.configure(bg="pink")
        

mark= tink.Label(base,text="welcome",fg='blue',font='time 25 bold',bg='white')#.place(x=170,y=20)
mark.pack()

start= tink.Button(base, text='Start',width=25,command=lambda:Start(mark))
stop=tink.Button(base, text='Stop',width=25,state='disabled',command=Stop)
reset=tink.Button(base, text='Reset',width=25,state='disabled',command=lambda:Reset(mark))

start.pack()
stop.pack()
reset.pack()



base.mainloop()
