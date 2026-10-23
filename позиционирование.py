from tkinter import*
from tkinter import Tk

root = Tk()
root.title("Позиционирование")
root.geometry("1000x600")
root.resizable(True,False)


def finish():
    root.destroy()
    print("Он испарился....")

root.protocol("WM_DELETE_WINDOW", finish)

btn = Button(root, text="123456", state=["disabled"])
btn.pack(expand=True, ipady=20, ipadx=35, padx=30, pady=25)

btn1 = Button(root, text="789")
btn1.pack(expand=True, fill=Y, padx=20)

btn2 = Button(root, text="ffdf")
btn2.pack(side = LEFT, pady=100, ipadx=10)

root.mainloop()