import tkinter as tk
import random
from turtle import right

words = []
with open("Z:\Programming Stuff\Projects\Python-Exercises\Hangman\worliste.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        words.append(line)
    
word = words[random.randint(0, 239650)]

#Hauptfenster
root = tk.Tk()
root.title("Hangman")
root.geometry("700x800")

#Frames
hangman = tk.Frame(root)
hangman.pack()

used = tk.Frame(root, bg="white")
used.pack(side="right")

#Labels und Entrys
used_label = tk.Label(used, text="benutzte Buchstaben")
used_label.pack(side="top")

hangman_label = tk.Label(hangman, relief="sunken", width=50, height=50)
hangman_label.pack()

word_label = tk.Label(root, text=word)
word_label.pack(side="top")

letter_entry = tk.Entry(root)
letter_entry.pack(side="bottom")

#Run GUI
root.mainloop()