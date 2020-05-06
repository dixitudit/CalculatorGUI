from tkinter import *
from math import sqrt
root = Tk()
index = 0
root.title('Calculator')
show = str
operator_count = 0
operator = 0


def equals(f_operator):  # Runs when equals is pressed on calculator
    global show
    global operator_count
    digit2 = show.split(button_num[f_operator])
    operator_count = 0
    try:
        if operator == 0:
            digit = float(show[1:])
            show = str(sqrt(digit))
    except ValueError:
        show = 'Error!'
    if operator in [3, 7, 11, 15, 16]:
        try:
            if f_operator == 3:
                show = str(float(digit2[0]) / float(digit2[1]))
            elif f_operator == 7:
                show = str(float(digit2[0]) * float(digit2[1]))
            elif f_operator == 11:
                show = str(float(digit2[0]) - float(digit2[1]))
            elif f_operator == 15:
                show = str(float(digit2[0]) + float(digit2[1]))
            elif f_operator == 16:
                show = str(float(digit2[0]) ** float(digit2[1]))
            else:
                show = 'Error!'
        except Exception:
            show = 'Error!'


def b_click(button_clicked):
    global index
    global show
    global operator
    global operator_count
    for button in buttons:
        if button_clicked == button:
            index = buttons.index(button_clicked)
            show = t.get()
            if index not in [0, 1, 2, 3, 7, 11, 15, 16, 19]:  # for taking only one operator at a time
                show = t.get() + str(button_num[index])
            if (index in [0, 3, 7, 11, 15, 16]) and operator_count == 0:
                operator_count = 1
                operator = index
                show = t.get() + str(button_num[index])
            if index == 1:
                operator_count = 0
                show = ''
            if index == 2:
                try:
                    if show[len(show)-1] in ['√', '/', '*', '-', '+', '^']:
                        operator_count = 0
                except IndexError:
                    operator_count = 0
                show = show[:-1]
            if index == 19 and operator_count == 1:
                equals(operator)
            t.delete(0, END)
            t.insert(0, show)


t = Entry(root, width=13, font=('Times New Roman', 39))
t.grid(row=0, column=0, columnspan=4)
button_num = ['√', 'C', '⤆', '/', 7, 8, 9, '*', 4, 5, 6, '-', 1, 2, 3, '+', '^', 0, '.', '=']
              # 0 ,  1 ,   2 ,  3 , 4, 5, 6,  7 , 8, 9,10, 11 ,12,13,14, 15 , 16 ,17, 18 , 19
root.resizable(0, 0)
buttons = []
r = 0
for i in range(len(button_num)):
    if i % 4 == 0:
        r += 1
    buttons.append(Button(root, font=('Times New Roman', 13, 'bold'), relief=FLAT,
                          text=button_num[i], width=7, height=3))
    buttons[i].configure(command=lambda button=buttons[i]: b_click(button))
    buttons[i].grid(row=r, column=i % 4)

root.mainloop()
