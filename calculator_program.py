from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def cleardisplay():
    global operator
    operator = ""
    text_Input.set("")

def equalsbutton():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

root = Tk()
root.title("Calculator")
operator = "" #???
text_Input = StringVar() #??

txtDisplay = Entry(root, font = ('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth = 4, bg = 'sky blue', justify="right")
txtDisplay.grid(columnspan=4)

button7 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='7', bg = 'powder blue', command = lambda: btnClick(7))
button7.grid(row=1, column = 0)

button8 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='8', bg = 'powder blue', command = lambda: btnClick(8))
button8.grid(row=1, column = 1)

button9 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='9', bg = 'powder blue', command = lambda: btnClick(9))
button9.grid(row=1, column = 2)

buttonadd = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='+', bg = 'powder blue', command = lambda: btnClick('+'))
buttonadd.grid(row=1, column = 3)

#-----------------------------------------------------------------------------------------------------------------

button4 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='4', bg = 'powder blue', command = lambda: btnClick(4))
button4.grid(row=2, column = 0)

button5 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='5', bg = 'powder blue', command = lambda: btnClick(5))
button5.grid(row=2, column = 1)

button6 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='6', bg = 'powder blue', command = lambda: btnClick(6))
button6.grid(row=2, column = 2)

buttonsub = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='-', bg = 'powder blue', command = lambda: btnClick("-"))
buttonsub.grid(row=2, column = 3)

#-----------------------------------------------------------------------------------------------------------------

button1 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='1', bg = 'powder blue', command = lambda: btnClick(1))
button1.grid(row=3, column = 0)

button2 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='2', bg = 'powder blue', command = lambda: btnClick(2))
button2.grid(row=3, column = 1)

button3 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='3', bg = 'powder blue', command = lambda: btnClick(3))
button3.grid(row=3, column = 2)

buttondiv = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='/', bg = 'powder blue', command = lambda: btnClick("/"))
buttondiv.grid(row=3, column = 3)

#-----------------------------------------------------------------------------------------------------------------

button0 = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='0', bg = 'powder blue', command = lambda: btnClick(0))
button0.grid(row=4, column = 0)

buttonclear = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='C', bg = 'powder blue', command = cleardisplay)
buttonclear.grid(row=4, column = 1)

buttondec = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='.', bg = 'powder blue', command =  cleardisplay)
buttondec.grid(row=4, column = 2)

buttonequals = Button(root, padx = 16, pady=16, fg='black', font = ('arial', 20, 'bold'), text='=', bg = 'powder blue', command = equalsbutton)
buttonequals.grid(row=4, column = 3)



root.mainloop()

