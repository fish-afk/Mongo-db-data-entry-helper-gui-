import tkinter as tk
from tkinter import *
from dotenv import load_dotenv
import os
from api_request import post_record
from tkinter import messagebox

root = tk.Tk()
root.title("Data entry application")
root.geometry("900x700")
root.configure(bg="black")

labels = ["Enter teamname:", "Enter name", "Enter price", "Enter description:", "Enter imagesrc",
          "Is customizable?", 'Enter qty:']

load_dotenv(".env")
SECRET_KEY = os.environ.get("API_KEY")


def add_labels(labels_arr, count):
    for i in range(len(labels_arr)):
        Label(root, text=labels_arr[i], font=("Arial", 25), bg="black", fg="light yellow").grid(column=5, row=count)
        count += 1


textbox1 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")
textbox2 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")
textbox3 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")
textbox4 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")
textbox5 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")
textbox6 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")
textbox7 = Text(root, height=3, width=39, font=("Arial", 12), bg="light blue")

textbox1.grid(column=6, row=0)
textbox2.grid(column=6, row=1)
textbox3.grid(column=6, row=2)
textbox4.grid(column=6, row=3)
textbox5.grid(column=6, row=4)
textbox6.grid(column=6, row=5)
textbox7.grid(column=6, row=6)


def get_input():
    value1 = textbox1.get("1.0", "end-1c")
    value2 = textbox2.get("1.0", "end-1c")
    value3 = textbox3.get("1.0", "end-1c")
    value4 = textbox4.get("1.0", "end-1c")
    value5 = textbox5.get("1.0", "end-1c")
    value6 = textbox6.get("1.0", "end-1c")
    value7 = textbox7.get("1.0", "end-1c")

    arr = [value1, value2, value3, value4, value5, value6, value7]

    return arr


def post_records():
    arr = get_input()
    value = post_record(arr)
    if value > 300:
        messagebox.showerror("Error", "An error occured!")
    else:
        messagebox.showinfo("Info", "Record posted successfully!")


add_labels(labels, 0)

Button(root, text="Post record", width=20, height=2, font=("Arial", 12), bg="light yellow",
       command=lambda: post_records()).grid(column=6, row=8)

print(SECRET_KEY)
root.mainloop()
