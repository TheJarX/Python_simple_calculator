from tkinter import *

class Calculator():
    def __init__(self, master):
        master.title('Simple calculator')
        master.resizable(False, False)
        self.error = False
        self.userEntry = Entry(master, width=30,borderwidth=1, font=(24))
        self.userEntry.grid(row=0, column=0,columnspan=4, padx=1, pady=10)

        # Define buttons
        self.btn_1 = Button(master, text='1', padx=40, pady=20, command=lambda: self.num_handler(1))
        self.btn_2 = Button(master, text='2', padx=40, pady=20, command=lambda: self.num_handler(2))
        self.btn_3 = Button(master, text='3', padx=40, pady=20, command=lambda: self.num_handler(3))
        self.btn_4 = Button(master, text='4', padx=40, pady=20, command=lambda: self.num_handler(4))
        self.btn_5 = Button(master, text='5', padx=40, pady=20, command=lambda: self.num_handler(5))
        self.btn_6 = Button(master, text='6', padx=40, pady=20, command=lambda: self.num_handler(6))
        self.btn_7 = Button(master, text='7', padx=40, pady=20, command=lambda: self.num_handler(7))
        self.btn_8 = Button(master, text='8', padx=40, pady=20, command=lambda: self.num_handler(8))
        self.btn_9 = Button(master, text='9', padx=40, pady=20, command=lambda: self.num_handler(9))
        self.btn_0 = Button(master, text='0', padx=40, pady=20, command=lambda: self.num_handler(0))

        self.btn_add = Button(master, text='+', padx=39, pady=20,  command=lambda: self.handler('add'))
        self.btn_subs = Button(master, text='- ', padx=39, pady=20,  command=lambda: self.handler('substract'))
        
        self.btn_clear = Button(master, text='C', padx=40, pady=20,  command=lambda: self.handler('clear'))
        self.btn_equal = Button(master, text='=', padx=39, pady=51.5,  command=lambda: self.handler('equal'))

        #Render buttons
        self.btn_1.grid(row=3, column=0)
        self.btn_2.grid(row=3, column=1)
        self.btn_3.grid(row=3, column=2)

        self.btn_4.grid(row=2, column=0)
        self.btn_5.grid(row=2, column=1)
        self.btn_6.grid(row=2, column=2)

        self.btn_7.grid(row=1, column=0)
        self.btn_8.grid(row=1, column=1)
        self.btn_9.grid(row=1, column=2)

        self.btn_0.grid(row=4, column=0)
        self.btn_add.grid(row=4, column=1)
        self.btn_equal.grid(row=4, column=2, rowspan=2)

        self.btn_clear.grid(row=5, column=0)
        self.btn_subs.grid(row=5, column=1)

    def num_handler(self, number):
        if self.error:
            self.clear()
            self.error = False

        current = str(self.userEntry.get())
        self.userEntry.delete(0, END)
        self.userEntry.insert(0, current + str(number) )

    def handler(self, opt):
        if opt == 'add':
            self.num_handler('+')
        elif opt == 'substract':
            self.num_handler('-')
        elif opt == 'clear':
            self.clear()
        elif opt == 'equal':
            self.showAnswer()

    def clear(self):
        self.userEntry.delete(0, END)
    
    def showAnswer(self):
        current = str(self.userEntry.get())
        self.clear()
        try:
            self.userEntry.insert(0, eval(current))
        except SyntaxError:
            self.error = True
            self.userEntry.insert(0, 'Syntax Error!')
