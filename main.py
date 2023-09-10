from tkinter import *

# UI
window = Tk()
window.title("Secret Notes")
window.config(pady=30, padx=30)


def SaveButton():
    f = open("MyContent.txt", "w")
    title = title_label_entry.get()
    secret = secret_label_text.get("1.0", END)
    f.write(f"{title}\n")
    f.write(f"{secret}\n")


# FONT
FONT = ("Comic Sans MS", 14, "bold")

title_label = Label(text="Enter your title", font=FONT)
title_label.pack()

title_label_entry = Entry(width=30)
title_label_entry.pack()

secret_label = Label(text="Enter your secret", font=FONT)
secret_label.pack()

secret_label_text = Text(width=35, height=20)
secret_label_text.pack()

# ENCRYPT
master_key_label = Label(text="Enter master key", font=FONT)
master_key_label.pack()

master_key_entry = Entry()
master_key_entry.pack()

button_1 = Button(window, text="Save & Encrypt", command=SaveButton)
button_1.pack()

button_2 = Button(text="Decrypt")
button_2.pack()

window.mainloop()
