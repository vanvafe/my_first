from random import randint
from tkinter import *
from tkinter import messagebox

def random_ege():
    pr=(height_tf.get())
    a=randint(1,10)
    b=randint(1,10)

    if a > b:
        messagebox.showinfo('random_ege', 'порог перейдешь')
    elif a < b:
        messagebox.showinfo('random_ege', 'не сдашь')
    elif a == b:
        messagebox.showinfo('random_ege', 'сдашь на 100 баллов')
    if a == 10:
        messagebox.showinfo('random_ege', 'поступишь без экзаменов')




window=Tk()
window.title('показатель успешности сдачи егэ')
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb=Label(
    frame,
    text='введите предмет для сдачи ЕГЭ'
)
height_lb.grid(row=3, column=1)

height_tf = Entry(
   frame,
)
height_tf.grid(row=3, column=2, pady=5)

cal_btn=Button(
    frame,
    text='расчитать шансы',
    command=random_ege
)
cal_btn.grid(row=5, column=2)

window.mainloop()