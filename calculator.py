 

from tkinter import *
from numpy import number
#the mainframe of the Tk library
root = Tk()
root.title('Calculator')
root.geometry('300x350')
''' img = PhotoImage(file='icon.png')
tk.call('wm', 'iconphoto', w, img) '''
# the entry widget where the user is going to input
User_input = Entry(root, width = 30)
User_input.pack()
bg = 'grey'
#test
# defining the button_responce which will give the responce back when the buttons are clicked in the entry widget, here we first define the button_responce and set a parameter called number then we make a new variable called current_button which is = User_input and we used the .get() feature to bring the value, then we delete the extra number that comes and then we insert the number that gets put in the widget i.e we do User_input.insert to insert, and bring them as string and add them.

def button_responce(number):
    current_button= User_input.get()
    User_input.delete(0, END)
    User_input.insert(0, str(current_button)+str(number))
def clear_button(number):
    User_input.delete(0, END)

def calculation(operator):
    first_num = User_input.get()
    global f_num
    global op
    op = operator
    f_num = int(first_num)
    User_input.delete(0, END)




button_1 = Button(root, text="1", padx = 40, pady = 15 , command=lambda: button_responce(1))
button_2 = Button(root, text="2", padx = 60, pady = 15 , command=lambda: button_responce(2))
button_3 = Button(root, text="3", padx = 40, pady = 15 , command=lambda: button_responce(3))
button_4 = Button(root, text="4", padx = 40, pady = 15 , command=lambda: button_responce(4))
button_5 = Button(root, text="5", padx = 60, pady = 15 , command=lambda: button_responce(5))
button_6 = Button(root, text="6", padx = 40, pady = 15 , command=lambda: button_responce(6))
button_7 = Button(root, text="7", padx = 40, pady = 15 , command=lambda: button_responce(7))
button_8 = Button(root, text="8", padx = 60, pady = 15 , command=lambda: button_responce(8))
button_9 = Button(root, text="9", padx = 40, pady = 15 , command=lambda: button_responce(9))
button_0 = Button(root, text="0", padx = 40, pady = 15 , command=lambda: button_responce(0))
button_plus = Button(root, text="+", padx = 60, pady = 15 ,bg = 'blue',fg ="white", command=lambda: calculation('+'))
button_minus = Button(root, text='-', padx = 40, pady = 15,fg ="white",bg = 'blue',  command = lambda: calculation('-'))
button_multiply = Button(root, text="×", padx = 40, pady = 15 ,fg ="white",bg = 'blue', command=lambda: calculation('*'))
button_divide = Button(root, text="÷", padx = 60, pady = 15 ,fg ="white",bg = 'blue', command=lambda: calculation('/'))
def equal_to():
    second_number = User_input.get()
    User_input.delete(0, END)
    match op:
        case '+':
            return User_input.insert(0, f_num+int(second_number))
            # do addition stuff
        case '-':
            return User_input.insert(0, f_num-int(second_number))
            # do subtraction stuff
        case '*':
            return User_input.insert(0, f_num*int(second_number))
            # do multiplication stuff
        case '/':
            return User_input.insert(0, f_num/int(second_number))
            # do division stuff

button_equal_to = Button(root, text="=", padx = 40, pady = 15 ,bg = 'green', command=lambda: equal_to())
button_clear = Button(root, text="c", padx = 160, pady = 15 , fg ="white", bg = 'red', command=lambda: clear_button(number))
button_1.place(relx = 0.28, rely = 0.2, anchor = E)
button_2.place(relx = 0.49, rely = 0.2, anchor = CENTER)
button_3.place(relx = 0.70, rely = 0.2, anchor = W)
button_4.place(relx = 0.28, rely = 0.35, anchor = E)
button_5.place(relx = 0.49, rely = 0.35, anchor = CENTER)
button_6.place(relx = 0.70, rely = 0.35, anchor = W)
button_7.place(relx = 0.28, rely = 0.50, anchor = E)
button_8.place(relx = 0.49, rely = 0.5, anchor = CENTER)
button_9.place(relx = 0.70, rely = 0.5, anchor = W)
button_0.place(relx = 0.28, rely = 0.65, anchor = E)
button_plus.place(relx = 0.49, rely =0.65, anchor = CENTER)
button_minus.place(relx = 0.70, rely = 0.65, anchor = W)
button_multiply.place(relx = 0.28, rely = 0.8, anchor = E)
button_divide.place(relx = 0.49, rely = 0.8, anchor = CENTER)
button_equal_to.place(relx = 0.70, rely = 0.8, anchor = W)
button_clear.place(relx = 0.49, rely = 0.95, anchor = CENTER)


root.mainloop()
