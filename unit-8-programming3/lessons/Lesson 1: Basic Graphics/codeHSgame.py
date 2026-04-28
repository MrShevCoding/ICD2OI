# This isn't my code, but instead pre-created from codeHS when you create a Python 3 Graphics (Tkinter) in the CodeHS website, 
# I thought doing an honerable mention would be nice!

import tkinter as tk
import random

words = [
    'function', 'variable', 'python', 'snake', 'codehs', 'karel', 'dog',
    'turtle', 'tracy'
]
word = random.choice(words)

root = tk.Tk()
root.geometry('300x300')
frame = tk.Frame(root)
frame.pack()

instruction_label = tk.Label(root, bg='white', text="Type the word below!")
instruction_label.pack()

word_label_stringvar = tk.StringVar()
word_label_stringvar.set(word)
word_label = tk.Label(root, bg='white', textvariable=word_label_stringvar)
word_label.pack()


sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: input_changed(sv))
e = tk.Entry(root, textvariable=sv)
e.pack()

def input_changed(sv):
    global word
    entry_input = sv.get()
    if entry_input == word:
        word = random.choice(words)
        word_label_stringvar.set(word)
        sv.set('')

root.mainloop()
