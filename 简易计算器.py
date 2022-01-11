
import tkinter as tk


root = tk.Tk()
label_var = tk.StringVar()
label_var.set('0')

root.geometry("295x280+150+150")
root.title('计算器')


root["background"] = "#ffffff"

def clear():
    label_var.set('0')

def back():
    label_var.set(label_var.get()[0:-1])

def division():
    label_var.set(label_var.get() + '/')

def multiplication():
    label_var.set(label_var.get() + '*')

def subtraction():
    label_var.set(label_var.get() + '-')

def addition():
    label_var.set(label_var.get() + '+')

def equal():
    result = str(eval(label_var.get()))

    if '/' in label_var.get():
        if result[-2] + result[-1] == '.0':
            label_var.set(str(result).replace('.0',''))
    else:
        label_var.set(result)
def nine():
    label_var.set(label_var.get() + '9') if label_var.get() != '0' else label_var.set('9')
def eight():
    label_var.set(label_var.get() + '8') if label_var.get() != '0' else label_var.set('8')
def seven():
    label_var.set(label_var.get() + '7') if label_var.get() != '0' else label_var.set('7')
def six():
    label_var.set(label_var.get() + '6') if label_var.get() != '0' else label_var.set('6')
def five():
    label_var.set(label_var.get() + '5') if label_var.get() != '0' else label_var.set('5')
def four():
    label_var.set(label_var.get() + '4') if label_var.get() != '0' else label_var.set('4')
def three():
    label_var.set(label_var.get() + '3') if label_var.get() != '0' else label_var.set('3')
def two():
    label_var.set(label_var.get() + '2') if label_var.get() != '0' else label_var.set('2')
def one():
    label_var.set(label_var.get() + '1') if label_var.get() != '0' else label_var.set('1')
def zero():
    label_var.set(label_var.get() + '0')  if label_var.get() != '0' else label_var.set('0')
def decimal():
    label_var.set(label_var.get() + '.')




lable1 = tk.Label(root,
                  width=20, height=2,
                  font=('宋体', 20), justify='left',
                  background='#ffffff', anchor='se',textvariable=label_var)

lable1.grid(padx=4, pady=4, row=0, column=0, columnspan=4)



button_clear = tk.Button(root, text='C', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0',command=clear)
button_back = tk.Button(root, text='←', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0',command=back)
button_division = tk.Button(root, text='/', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0',command=division)
button_multiplication = tk.Button(root, text='x', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0',command=multiplication)

button_clear.grid(padx=4, pady=2, row=1, column=0)
button_back.grid(padx=4, pady=2, row=1, column=1)
button_division.grid(padx=4, pady=2, row=1, column=2)
button_multiplication.grid(padx=4, pady=2, row=1, column=3)

button_seven = tk.Button(root, text='7', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=seven)
button_eight = tk.Button(root, text='8', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=eight)
button_nine = tk.Button(root, text='9', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=nine)
button_subtraction = tk.Button(root, text='—', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0',command=subtraction)

button_seven.grid(padx=4, pady=2, row=2, column=0)
button_eight.grid(padx=4, pady=2, row=2, column=1)
button_nine.grid(padx=4, pady=2, row=2, column=2)
button_subtraction.grid(padx=4, pady=2, row=2, column=3)

button_four = tk.Button(root, text='4', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=four)
button_five = tk.Button(root, text='5', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=five)
button_six = tk.Button(root, text='6', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=six)
button_addition = tk.Button(root, text='+', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0',command=addition)

button_four.grid(padx=4, pady=2, row=3, column=0)
button_five.grid(padx=4, pady=2, row=3, column=1)
button_six.grid(padx=4, pady=2, row=3, column=2)
button_addition.grid(padx=4, pady=2, row=3, column=3)


button_one = tk.Button(root, text='1', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=one)
button_two = tk.Button(root, text='2', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=two)
button_three = tk.Button(root, text='3', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=three)
button_equal = tk.Button(root, text='=', width=5, height=3, font=('宋体', 16), relief='flat', background='#C0C0C0',command=equal)


button_one.grid(padx=4, pady=2, row=4, column=0)
button_two.grid(padx=4, pady=2, row=4, column=1)
button_three.grid(padx=4, pady=2, row=4, column=2)

button_equal.grid(padx=4, pady=2, row=4, rowspan=2, column=3)


button_zero = tk.Button(root, text='0', width=12, font=('宋体', 16), relief='flat', background='#FFDEAD',command=zero)
button_decimal = tk.Button(root, text='.', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD',command=decimal)

button_zero.grid(padx=4, pady=4, row=5, column=0, columnspan=2)
button_decimal.grid(padx=4, row=5, column=2)

root.mainloop()
