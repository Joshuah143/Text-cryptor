from tkinter import *
from tkinter import messagebox
import encrypt


def encrypt_from_tk(e):
    ret = encrypt.encrypt(e['PASSWORD'].get(), e['TOKEN'].get(), True)
    addmessage(ret[1])


def decrypt_from_tk(e):
    ret = encrypt.decrypt(e['PASSWORD'].get(), e['TOKEN'].get(), True)
    addmessage(ret[1])


def addmessage(message):
    messagebox.showinfo("TOKEN", message)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    window = Tk()
    window.title('Cryptor')  # todo: chnage name
    window.geometry("800x150+300+300")
    ents = makeform(window, ['TOKEN', 'PASSWORD'])
    b1 = Button(window, text='ENCRYPT',
                command=(lambda e=ents: encrypt_from_tk(e)))
    b1.pack(side=BOTTOM, padx=5, pady=5)
    b1 = Button(window, text='DECRYPT',
                command=(lambda e=ents: decrypt_from_tk(e)))
    b1.pack(side=BOTTOM, padx=5, pady=5)
    window.mainloop()
