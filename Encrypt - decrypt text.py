# The encryption / decryption code was taken on GitHub:
# https://github.com/ramzi87/Encrypt_text/blob/master/crypt_text.py

# We generally get an error when we try giving value which are not possible.

from tkinter import *
from tkinter import ttk
import pyperclip


def encrypt():
    key = entry_key.get()
    mylst = []    
    mytext = input_win.get('1.0', END)
    try:
        for x in range(0, len(mytext)):
            n_letter = ord(mytext[x]) + int(key)
            c_item = chr(n_letter)
            mylst.append(c_item)
        new_text = ''.join(mylst)
        output_win.delete(1.0, END)
        output_win.insert(1.0, new_text)
        statusbar.config(text='Done!', fg='black')
    except ValueError:
        statusbar.config(text='Encription / decryption key mast be an integer!',
                         fg='red')


def decrypt():
    key = entry_key.get()
    mylst = []    
    mytext = input_win.get('1.0', END)
    try:
        for x in range(0, len(mytext)):
            n_letter = ord(mytext[x])-int(key)
            ch = chr(n_letter)
            mylst.append(ch)
        new_text = ''.join(mylst)
        output_win.delete(1.0, END)
        output_win.insert(1.0, new_text)
        statusbar.config(text='Done!', fg='black')
    except ValueError:
        statusbar.config(text='Encription / decryption key mast be an integer!',
                         fg='red')        


# Pop-up for the 'paste' / 'copy' menu for input window
def do_popup_in(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()
        menu.entryconfigure('Paste',
                            command=lambda: input_win.event_generate('<<Paste>>'))
        menu.entryconfigure('Copy',
                            command=lambda: input_win.event_generate('<<Copy>>'))


# Pop-up for the 'paste' / 'copy' menu for output window
def do_popup_out(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()
        menu.entryconfigure('Paste',
                            command=lambda: output_win.event_generate('<<Paste>>'))
        menu.entryconfigure('Copy',
                            command=lambda: output_win.event_generate('<<Copy>>'))


def clear_all():
    entry_key.delete(0, END)
    input_win.delete(1.0, END)
    output_win.delete(1.0, END)
    statusbar.config(text='^ Type a text in the input window ^', fg='black')


def copy_to_clipboard(event):
    new_text = output_win.get('1.0', END)
    pyperclip.copy(new_text)


root = Tk()
root.title('Text Encryption')
# root.iconbitmap('translate.ico')
root.resizable(width=0, height=0)

# 'Paste' / 'Copy' menu
menu = Menu(root, tearoff = 0)
menu.add_command(label='Paste')
menu.add_command(label='Copy')

frame = Frame(root)
frame.grid(row = 0, column = 0, padx = 10, pady = 3)

lbl = Label(frame, text='Type encryption / decryptione key (integer):')
lbl.grid(row = 0, column = 0, padx = 10, pady = 10)

entry_key = Entry(frame, bd=3, width=30)
entry_key.grid(row = 0, column = 1, padx = 10, pady = 10)

input_win = Text(frame, bd=3, height=15, width=61, wrap=WORD)
input_win.grid(row = 1, column = 0, columnspan=2, sticky='ew', pady = 5)
scrollbar1 = ttk.Scrollbar(frame, orient='vertical', command=input_win.yview)
scrollbar1.grid(row=1, column=2, sticky='ns')
input_win['yscrollcommand'] = scrollbar1.set
input_win.bind('<Button-3>', do_popup_in)

encrypt_button = Button(frame, text = 'Encrypt', width=20, command=encrypt)
encrypt_button.grid(row = 2, column = 0, padx = 5, pady = 5)
decrypt_button = Button(frame, text = 'Decrypt', width=20, command=decrypt)
decrypt_button.grid(row = 2, column = 1, padx = 5, pady = 5)

output_win = Text(frame, bd=3, height=15, width=61, wrap=WORD)
output_win.grid(row = 3, column = 0, columnspan=2, sticky='ew', pady = 5)
scrollbar2 = ttk.Scrollbar(frame, orient='vertical', command=output_win.yview)
scrollbar2.grid(row=3, column=2, sticky='ns')
output_win['yscrollcommand'] = scrollbar2.set
output_win.bind('<Button-3>', do_popup_out)

clear_all_button = Button(frame, text = 'Clear all', width=73, command=clear_all)
clear_all_button.grid(row = 4, column = 0, columnspan=2, padx = 5, pady = 5)

statusbar = Label(root, text='^ Type a text in the input window ^',
                  bd=1, relief=SUNKEN, anchor='center', fg='black')
statusbar.grid(row=1, column=0, sticky=W+E)

frame.bind_all('<Control-c>', copy_to_clipboard)

root.mainloop()
