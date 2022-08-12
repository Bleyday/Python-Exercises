import tkinter as tk
import random
from turtle import right

words = []
with open("Hangman\worliste.txt", "r") as f:
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

used = tk.Frame(root, bg="white", highlightbackground="black", highlightthickness=1, height=800)
used.pack(side="right")

word_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
word_frame.pack()

strich_frame = tk.Frame(word_frame, highlightbackground="red", highlightthickness=1)
strich_frame.pack(side="bottom")

#Labels und Entrys
used_label = tk.Label(used, text="benutzte Buchstaben")
used_label.pack(side="top")

#Hangman Canvas
hangman_label = tk.Canvas(hangman, bd=2, relief="sunken",width=400, height=300)
hangman_label.pack(pady=50)

hangman_label.create_line(0, 0, 50, 20, fill="#476042", width=3)

word_label = tk.Label(root, text=word)
word_label.pack(side="top")

letters = list(word)

for i in range(len(letters)-1):
    globals()['letter%s' % i] = tk.Label(word_frame, text="h")
    globals()['letter%s' % i].pack(side="left")
    tk.Label(strich_frame, text="_").pack(side="left")

letter_entry = tk.Entry(root, width=10)
letter_entry.pack(side="bottom", pady=25)

def show():
    if "e" in letters:
        for i in range(len(letters)):
            if letters[i] == "e":
                globals()["letter%s" %i].configure(text="e")

btn = tk.Button(root, text="Test", command=show)
btn.pack()

#Run GUI
root.mainloop()