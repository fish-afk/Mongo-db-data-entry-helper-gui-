import tkinter as tk
from tkinter import *
import json
import requests

from api_request import post_record
from tkinter import messagebox

root = tk.Tk()
root.title("Data entry application")
root.geometry("900x700")
root.configure(bg="black")

labels = ["Enter teamname:", " Enter name", "  Enter price", " Enter description:",
          " Enter imagesrc", " Is customizable?", '    Enter qty:']

collection_chosen = StringVar(root, "other_kits")

values = {"other_kits": "other_kits",
          "F1_kits": "F1_kits",
          "balr_kits": "balr_kits",
          "promo_kits": "promo_kits"
          }


def printing():
    print(collection_chosen.get() + "Chosen !")


def add_radio_btns():
    count = 5
    for (text, value) in values.items():
        Radiobutton(root, text=text, variable=collection_chosen, width=10, height=1,
                    value=value, indicator=0,
                    background="light blue", command=printing).grid(column=count, row=10)
        count += 1


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


def get_length(query, by="collections"):
    result = requests.get(f"https://data.mongodb-api.com/app/kitzone-functions-wqhlr/endpoint/return_len?{by}={query}")
    print(result)
    return json.dumps(result)


def post_records():
    arr = get_input()
    value = post_record(arr, collection_chosen.get(), get_length(collection_chosen.get()))

    if int(value) > 300 or value is None:
        messagebox.showerror("Error", "An error occured!")
    else:
        messagebox.showinfo("Info", "Record posted successfully!")
        textbox5.delete("1.0", "end")


add_labels(labels, 0)
add_radio_btns()

Button(root, text="Post record", width=20, height=2, font=("Arial", 12), bg="light yellow",
       command=lambda: post_records()).grid(column=6, row=8)

root.mainloop()
