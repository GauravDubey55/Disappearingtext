from tkinter import *
from time import perf_counter

time_last_typed = perf_counter()

def text_entered(event):
    global time_last_typed
    time_last_typed = perf_counter()

def check_time():
    global time_last_typed
    if perf_counter() - time_last_typed >= 5:
        my_text.delete(1.0, END)
    my_text.after(100, check_time)

window = Tk()
window.title('The Disappearing Text App')
window.geometry("1000x400")

label = Label(window, text='Type anything below. If you stop typing for more than 5 secs, your text will disappear.', font=('Helvetica', 15))
label.pack()

my_frame = Frame(window)
my_frame.pack(pady=5)

my_text = Text(my_frame, width=100, font=("Helvetica",15))
my_text.pack()
my_text.bind("<Key>", text_entered)
my_text.after(100, check_time)

window.mainloop()