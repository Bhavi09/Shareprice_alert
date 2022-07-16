from tkinter import*
from main import alert
import time

root = Tk()
root.geometry('500x500')
root.title("Price Alarm")

label_0 = Label(root, text="SHARE PRICE ALERT", width=20, font=("bold", 20))
label_0.place(x=90, y=53)


label_1 = Label(root, text="Equity name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Price", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Greater or Lesser", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var1 = IntVar()
Radiobutton(root, text="Greater", padx=5, variable=var1, value=1).place(x=225, y=230)
Radiobutton(root, text="Smaller", padx=20, variable=var1, value=2).place(x=290, y=230)

label_3 = Label(root, text="Want to sell or buy", width=20, font=("bold", 10))
label_3.place(x=70, y=260)
var2 = StringVar()
Radiobutton(root, text="Sell", padx=5, variable=var2, value="sell").place(x=235, y=260)
Radiobutton(root, text="Buy", padx=20, variable=var2, value="Buy").place(x=290, y=260)




Button(root, text='Submit', width=20, bg='brown', fg='white', command=root.quit).place(x=180, y=380)

# it is use for display the registration form on the window
root.mainloop()
alert(entry_1.get(), entry_2.get(), var2.get())