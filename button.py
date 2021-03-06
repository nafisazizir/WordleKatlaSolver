from tkinter import *

def textButton(mainFrame):
    listButton = [0]

    frame = Frame(mainFrame)
    frame.pack()

    b1 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b1))
    b1.grid(row=0, column=0)
    listButton.append(b1)
    b2 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b2))
    b2.grid(row=0, column=1)
    listButton.append(b2)
    b3 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b3))
    b3.grid(row=0, column=2)
    listButton.append(b3)
    b4 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b4))
    b4.grid(row=0, column=3)
    listButton.append(b4)
    b5 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b5))
    b5.grid(row=0, column=4)
    listButton.append(b5)

    b6 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b6))
    b6.grid(row=1, column=0)
    listButton.append(b6)
    b7 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b7))
    b7.grid(row=1, column=1)
    listButton.append(b7)
    b8 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b8))
    b8.grid(row=1, column=2)
    listButton.append(b8)
    b9 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b9))
    b9.grid(row=1, column=3)
    listButton.append(b9)
    b10 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b10))
    b10.grid(row=1, column=4)
    listButton.append(b10)

    b11 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b11))
    b11.grid(row=2, column=0)
    listButton.append(b11)
    b12 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b12))
    b12.grid(row=2, column=1)
    listButton.append(b12)
    b13 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b13))
    b13.grid(row=2, column=2)
    listButton.append(b13)
    b14 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b14))
    b14.grid(row=2, column=3)
    listButton.append(b14)
    b15 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b15))
    b15.grid(row=2, column=4)
    listButton.append(b15)

    b16 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b16))
    b16.grid(row=3, column=0)
    listButton.append(b16)
    b17 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b17))
    b17.grid(row=3, column=1)
    listButton.append(b17)
    b18 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b18))
    b18.grid(row=3, column=2)
    listButton.append(b18)
    b19 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b19))
    b19.grid(row=3, column=3)
    listButton.append(b19)
    b20 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b20))
    b20.grid(row=3, column=4)
    listButton.append(b20)

    b21 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b21))
    b21.grid(row=4, column=0)
    listButton.append(b21)
    b22 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b22))
    b22.grid(row=4, column=1)
    listButton.append(b22)
    b23 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b23))
    b23.grid(row=4, column=2)
    listButton.append(b23)
    b24 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b24))
    b24.grid(row=4, column=3)
    listButton.append(b24)
    b25 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b25))
    b25.grid(row=4, column=4)
    listButton.append(b25)

    b26 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b26))
    b26.grid(row=5, column=0)
    listButton.append(b26)
    b27 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b27))
    b27.grid(row=5, column=1)
    listButton.append(b27)
    b28 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b28))
    b28.grid(row=5, column=2)
    listButton.append(b28)
    b29 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b29))
    b29.grid(row=5, column=3)
    listButton.append(b29)
    b30 = Button(frame, width=3, height=2, font=('NORMAL',40), command=lambda: buttonPressed(b30))
    b30.grid(row=5, column=4)
    listButton.append(b30)
    
    return listButton

def buttonPressed(button):
    if not (button['bg'] == 'yellow' or button['bg'] == 'green' or button['bg'] == 'black'):
        button.config(bg='green')
    elif button['bg'] == 'green':
        button.config(bg='yellow')
    elif button['bg'] == 'yellow':
        button.config(bg='black')
        button.config(fg='white')
    elif button['bg'] == 'black':
        button.config(bg='green')
        button.config(fg='black')