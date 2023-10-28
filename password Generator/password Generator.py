import string,random
from tkinter import *


Screen= Tk()

Screen.geometry("500x300")
Screen.title("PASSWORD GENERATOR")

Title = StringVar()
TitleLabel = Label(Screen, textvariable=Title).pack()
Title.set("Strength of Password")

def SelectionOptions():
    SelectionOptions = Choice.get()

Choice= IntVar()
RadioButton1 = Radiobutton(Screen,text="POOR",variable=Choice,value=1,command=SelectionOptions).pack(anchor=CENTER)
RadioButton2 = Radiobutton(Screen,text="AVERAGE",variable=Choice,value=2,command=SelectionOptions).pack(anchor=CENTER)
RadioButton3 = Radiobutton(Screen,text="STRONG",variable=Choice,value=3,command=SelectionOptions).pack(anchor=CENTER)

LabelChoice = Label(Screen)
LabelChoice.pack()

LengthLabel = StringVar()
LengthLabel.set("Password Length")
LengthTitle = Label(Screen,textvariable=LengthLabel).pack()


Value = IntVar()
SpinLength = Spinbox(Screen, from_=9, to_=25 ,textvariable=Value,width=14).pack()



Poor = string.ascii_uppercase+string.ascii_lowercase
Average = string.ascii_uppercase+string.ascii_lowercase+string.digits
Symbols="""~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/ """
Advance= Poor+Average+Symbols

def PassGen():
    if Choice.get()==1:
        return "".join(random.sample(Poor,Value.get()))
    if Choice.get()==2:
        return "".join(random.sample(Average,Value.get()))
    if Choice.get()==3:
        return "".join(random.sample(Advance,Value.get()))


Lsum=Label(Screen,text="")
Lsum.pack(side=BOTTOM)
def CallBack():
    Lsum.config(text=PassGen())
Password=str(CallBack())
PassGenButton = Button(Screen,text="Generate Password",bd=5, height=2 ,command=CallBack,pady=3)
PassGenButton.pack()

Screen.mainloop()