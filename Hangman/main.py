import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

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

strich_frame = tk.Frame(word_frame)
strich_frame.pack(side="bottom")

#Labels und Entrys
used_label = tk.Label(used, text="benutzte Buchstaben")
used_label.pack(side="top")

#Hangman Canvas
hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman.png"))
hangman_label = tk.Label(hangman, image = hangman_start)
hangman_label.pack(pady=50)

word_label = tk.Label(root, text=word)
word_label.pack(side="top")

letters = list(word)

for i in range(len(letters)-1):
    globals()['letter%s' % i] = tk.Label(word_frame, text=" ", font="Consolas")
    globals()['letter%s' % i].pack(side="left")
    tk.Label(strich_frame, text="_", font="Consolas").pack(side="left")

def check_entry_error(event):
    try:
        var = letter_entry.get()
        if len(var) > 1 or isinstance(int(var), int):
            messagebox.showerror('Entry Error','Pls only one character and no nmbrs')
    except:
        print("allowed")
        show()
 
def show():
    eingabe = letter_entry.get()
    if eingabe.lower() in letters:
        if eingabe.upper() in letters:
            letter0.configure(text=letters[0])
        for i in range(len(letters)):
            if letters[i] == eingabe:
                globals()["letter%s" %i].configure(text=eingabe)
    else:
        draw_hangman()
    letter_entry.delete(0)
fails = 11
def draw_hangman():
    global fails
    if fails == 11:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_1.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 10:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_2.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 9:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_3.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 8:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_4.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 7:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_5.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 6:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_6.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 5:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_7.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 4:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_8.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 3:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_9.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 2:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_10.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        fails = fails -1
    elif fails == 1:
        hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman_11.png"))
        hangman_label.configure(image=hangman_start)
        hangman_label.image = hangman_start
        print("verloren")
def new_word():
    for widget in word_frame.winfo_children():
        widget.destroy()

    word = words[random.randint(0, 239650)]
    letters = list(word)

    for i in range(len(letters)-1):
        globals()['letter%s' % i] = tk.Label(word_frame, text=" ", font="Consolas")
        globals()['letter%s' % i].pack(side="left")
        tk.Label(strich_frame, text="_", font="Consolas").pack(side="left")
    word_label.configure(text=word)

letter_entry = tk.Entry(root, width=10)
letter_entry.pack(side="bottom", pady=25)
root.bind('<Return>', check_entry_error)

btn = tk.Button(root, text="Test", command=new_word)
btn.pack()

#Run GUI
root.mainloop()