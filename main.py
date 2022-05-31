from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import button as KB

class main (object):
    def __init__ (self):
        self.window = Tk()
        self.window.title('Katla/ Worlde Solver')
        self.inputList = [False for _ in range(7)]
        self.window.resizable(False,False)
        self.menu()
        self.row = 1

        self.mainFrame = Frame(self.window)
        self.mainFrame.pack(padx=15, pady=(0,10))

        
        self.left(self.mainFrame)
        self.right(self.mainFrame)
        self.confirmButton.config(state=DISABLED)
        self.enterButton.config(state=DISABLED)


        self.window.mainloop()
    
    def menu(self):
        menuLabel = Label(self.window, text='Choose type:', font=("BOLD", 18))
        menuLabel.pack(pady=(10,0))

        self.header = Frame(self.window)
        self.header.pack(pady=(0,20))

        self.katlaButton = Button(self.header, text='Katla', command=lambda: self.pressedMenu(self.katlaButton))
        self.katlaButton.grid(row=1, column=0)

        self.wordleButton = Button(self.header, text='Wordle', command=lambda: self.pressedMenu(self.wordleButton))
        self.wordleButton.grid(row=1, column=1)

        self.resetButton = Button(self.header, text='Reset', command=lambda: self.reset())
        self.resetButton.grid(row=1, column=2)

    def left(self, mainFrame):
        # frame for left part
        frame = Frame(mainFrame)
        frame.grid(row=0, column=0)

        inputLabel = Label(frame, text='Input the word:', font=("NORMAL", 18))
        inputLabel.pack()

        # frame for input label and buttons
        inputFrame = Frame(frame)
        inputFrame.pack()

        self.inputVar = StringVar()
        fileInput = Entry(inputFrame, textvariable=self.inputVar, width=10)
        fileInput.grid(row=0, column=0)

        self.enterButton = Button(inputFrame, text='Enter', command=lambda: self.inputWord())
        self.enterButton.grid(row=0, column=1)

        self.confirmButton = Button(inputFrame, text='Confirm', command=lambda: self.confirmWord())
        self.confirmButton.grid(row=0, column=2)

        self.listButton = KB.textButton(frame)
        self.setButton('D')

    def right(self, mainFrame):
        self.canvas = Canvas(mainFrame, width=400, height=628, relief='ridge', bd = 1)
        self.canvas.grid(row=0, column=1, sticky='S')

        self.canvas.create_text(200,30, text='List of all possible words:', font=('BOLD', 18))

    def inputWord(self):
        word = self.inputVar.get()
        if len(word) != 5 or not word.isalpha():
            messagebox.showerror('Wrong input!', 'Please enter correct word (5 letters alphabet)')
            return
        self.confirmButton.config(state=NORMAL)
        self.enterButton.config(state=DISABLED)
        for i in range(1,7):
            if self.inputList[i] == False:
                for j in range(1,6):
                    index = ((i-1)*5) + j
                    self.listButton[index]['text'] = word[j-1].upper()
                self.inputList[i] = True
                self.setColor(i)
                break
    
    def setColor(self, row):
        for j in range(1,6):
            index = ((row-1)*5) + j
            self.listButton[index].config(state=NORMAL)

    def setButton(self, setting):
        for i in self.listButton:
            if i != 0 and setting=='D':
                i.config(state=DISABLED)
            elif i != 0 and setting=='E':
                i.config(state=NORMAL)

    def confirmWord(self):
        black = []
        green = []
        yellow = []
        
        self.setButton('D')
        for j in range(1,6):
            index = ((self.row-1)*5) + j
            button = self.listButton[index]
            if button['bg'] == 'black':
                black.append((button['text'].lower(), j-1))
            elif button['bg'] == 'yellow':
                yellow.append((button['text'].lower(), j-1))
            elif button['bg'] == 'green':
                green.append((button['text'].lower(), j-1))

        for i in green:
            for j in self.db:
                if j[i[1]] != i[0]:
                    self.possw.discard(j)

        for i in yellow:
            for j in self.db:
                if i[0] == j[i[1]]:
                    self.possw.discard(j)
                elif i[0] not in j:
                    self.possw.discard(j)

        for i in black:
            for j in self.db:
                if i[0] in j:
                    self.possw.discard(j)
    
        self.row += 1        
        self.printPossWord()

        self.confirmButton.config(state=DISABLED)
        self.enterButton.config(state=NORMAL)

    def printPossWord(self):
        self.canvas.delete('all')
        self.canvas.create_text(200,30, text='List of all possible words:', font=('BOLD', 18))
        res1 = ''
        res2 = ''
        res3 = ''
        res4 = ''
        res5 = ''
        j = 0
        for i in self.possw:
            if j <= 32:
                res1 += i + '\n'
            elif j <= 65:
                res2 += i + '\n'
            elif j <= 98:
                res3 += i + '\n'
            elif j <= 131:
                res4 += i + '\n'
            elif j <= 164:
                res5 += i + '\n'
            j += 1
        self.canvas.create_text(20,50, text=res1, font=('NORMAL', 14), anchor=NW)
        self.canvas.create_text(100,50, text=res2, font=('NORMAL', 14), anchor=NW)
        self.canvas.create_text(180,50, text=res3, font=('NORMAL', 14), anchor=NW)
        self.canvas.create_text(260,50, text=res4, font=('NORMAL', 14), anchor=NW)
        self.canvas.create_text(340,50, text=res5, font=('NORMAL', 14), anchor=NW)
    
    def reset(self):
        self.katlaButton.config(state=NORMAL)
        self.wordleButton.config(state=NORMAL)

        self.canvas.delete('all')
        self.canvas.create_text(200,30, text='List of all possible words:', font=('BOLD', 18))
        self.inputList = [False for _ in range(7)]
        self.row = 1

        self.left(self.mainFrame)
        self.right(self.mainFrame)
        self.confirmButton.config(state=DISABLED)
        self.enterButton.config(state=DISABLED)
        
    
    def pressedMenu(self, button):
        mode = button['text'].lower()
        self.setMode(mode)
        self.katlaButton.config(state=DISABLED)
        self.wordleButton.config(state=DISABLED)
    
    def setMode(self, mode):
        if mode == 'katla':
            ifile = open('database/katla.txt', 'r')
            self.db = [i[:5].lower() for i in ifile]
            self.possw = set(self.db[:])
            self.printPossWord()
            self.enterButton.config(state=NORMAL)
        elif mode == 'wordle':
            ifile = open('database/wordle.txt', 'r')
            self.db = [i[:5].lower() for i in ifile]
            self.possw = set(self.db[:])
            self.printPossWord()
            self.enterButton.config(state=NORMAL)
        
if __name__ == '__main__':
    main()
