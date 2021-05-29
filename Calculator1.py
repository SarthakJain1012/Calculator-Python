from tkinter import*
calculator = Tk()
#calculator.geometry("312x324")
calculator.resizable(0,0)
calculator.title("Calculator")

# Input
c=Entry(calculator,width=30)
c.grid(row=0,column=0,columnspan=3)

def button_click(number):
    num=c.get()
    c.delete(0,END)
    c.insert(0,str(num)+str(number))
    return

def button_c():
    c.delete(0,END)

def button_add():
    global f_num
    global flag
    flag="add"
    first_number=c.get()
    f_num=float(first_number)
    c.delete(0,END)

def button_divi():
    global f_num
    global flag
    first_number=c.get()
    f_num=float(first_number)
    c.delete(0,END)
    flag="div"
    return

def button_multi():
    global f_num
    global flag
    first_number=c.get()
    f_num=float(first_number)
    c.delete(0,END)
    flag="mult"
    return

def button_subt():
    global flag
    first_number=c.get()
    f_num=float(first_number)
    c.delete(0,END)
    flag="sub"
    return

def button_equal():
    #global s_num
    second_number=c.get()
    #s_num=second_number
    c.delete(0,END)
    if flag=='add':
        c.insert(0,f_num + float(second_number))
    if flag=='mult':
        c.insert(0,f_num * float(second_number))
    if flag=='sub':
        c.insert(0,f_num - float(second_number))
    if flag=='div':
        c.insert(0,f_num / float(second_number))

# Buttons
button1=Button(calculator,text="1",padx=40,pady=20,command=lambda: button_click(1))
button2=Button(calculator,text="2",padx=40,pady=20,command=lambda:button_click(2))
button3=Button(calculator,text="3",padx=40,pady=20,command=lambda:button_click(3))
button4=Button(calculator,text="4",padx=40,pady=20,command=lambda:button_click(4))
button5=Button(calculator,text="5",command=lambda:button_click(5),padx=40,pady=20)
button6=Button(calculator,text="6",command=lambda:button_click(6),padx=40,pady=20)
button7=Button(calculator,text="7",command=lambda:button_click(7),padx=40,pady=20)
button8=Button(calculator,text="8",command=lambda:button_click(8),padx=40,pady=20)
button9=Button(calculator,text="9",command=lambda:button_click(9),padx=40,pady=20)
button0=Button(calculator,text="0",command=lambda:button_click(0),padx=40,pady=20)
button_dot=Button(calculator,text=".",command=lambda:button_click("."),padx=41,pady=20)

button_clear=Button(calculator,text="C",padx=38,pady=20,command=button_c)
button_eval=Button(calculator,text="=",padx=85,pady=20,command=button_equal)
button_sum=Button(calculator,text="+",command=button_add,padx=39,pady=20)

button_mult=Button(calculator,text="x",command=button_multi,padx=40,pady=20)
button_div=Button(calculator,text="/",command=button_divi,padx=40,pady=20)
button_sub=Button(calculator,text="-",command=button_subt,padx=40,pady=20)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_clear.grid(row=4,column=2)

#Operations

button_eval.grid(row=5,columnspan=2,column=1)
button_sum.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_mult.grid(row=6,column=1)
button_div.grid(row=6,column=2)

calculator.mainloop()