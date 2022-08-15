import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

words = []
with open("Hangman\worliste.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        words.append(line)
    
word = words[random.randint(0, 239653)]

#Hauptfenster
root = tk.Tk()
root.title("Hangman")
root.geometry("700x800")

#Frames
hangman = tk.Frame(root)
hangman.pack()

used = tk.Frame(root, highlightbackground="black", highlightthickness=1, height=800)
used.pack(side="right")

word_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
word_frame.pack()

strich_frame = tk.Frame(word_frame)
strich_frame.pack(side="bottom")

#Labels und Entrys
used_label = tk.Label(used, text="benutzte Buchstaben")
used_label.pack(side="top")
used_letters_list = tk.Label(used, text="")
used_letters_list.pack()

#Hangman Canvas
hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman.png"))
hangman_label = tk.Label(hangman, image = hangman_start)
hangman_label.pack(pady=50)

#word_label = tk.Label(root, text=word)
#word_label.pack(side="top")
print(word)

letters = list(word)
word = word.lower()
count_letters = list(word)
del count_letters[-1]

print("buchstaben anzahl:" +str(count_letters))

for i in range(len(letters)-1):
    globals()['letter%s' % i] = tk.Label(word_frame, text=" ", font="Consolas")
    globals()['letter%s' % i].pack(side="left")
    tk.Label(strich_frame, text="_", font="Consolas").pack(side="left")

def check_entry_error(event):
    try:
        var = letter_entry.get()
        if len(var) == 0:
            messagebox.showerror('Entry Error','At least one character')
        elif len(var) > 1 or isinstance(int(var), int):
            messagebox.showerror('Entry Error','Pls only one character and no nmbrs')
    except:
        show()

def iswin():
    for letter in count_letters:
        if letter == letter_entry.get():
            count_letters.remove(letter)
            print(count_letters)
    if len(count_letters) == 0:
        messagebox.showinfo("Win", "you win!")
        letter_entry.configure(state="disabled")
    else :
        print(len(count_letters))
        
used_letters = []
def show():
    eingabe = letter_entry.get()
    
    if eingabe in letters:
        for i in range(len(letters)):
            if letters[i] == eingabe:
                globals()["letter%s" %i].configure(text=eingabe)
                iswin()
        if eingabe.upper() in letters:
            letter0.configure(text=letters[0])
            iswin()
    elif eingabe.upper() in letters:
            letter0.configure(text=letters[0])
            iswin()
    else:
        if eingabe in used_letters:
                print("exists")
        else:
            used_letters.append(eingabe)
            used_letters_list.configure(text=used_letters)
            
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
        messagebox.showinfo("Verloren", "Du hast verloren!")
        letter_entry.delete(0)
        new_word()
        clear_used_letters()

def new_word():
    #Clear Frames
    for widget in word_frame.winfo_children():
        widget.destroy()
    clear_used_letters()

    #generate new words and list
    word = words[random.randint(0, 239653)]
    global letters
    letters = list(word)
    word = word.lower()
    global count_letters
    count_letters = list(word)
    del count_letters[-1]

    #generate new empty lists
    strich_frame = tk.Frame(word_frame)
    strich_frame.pack(side="bottom")

    for i in range(len(letters)-1):
        globals()['letter%s' % i] = tk.Label(word_frame, text=" ", font="Consolas")
        globals()['letter%s' % i].pack(side="left")
        tk.Label(strich_frame, text="_", font="Consolas").pack(side="left")
    
    print(word)
    #reset hangman pics
    hangman_start = ImageTk.PhotoImage(Image.open("Hangman\Assets\hangman.png"))
    hangman_label.configure(image=hangman_start)
    hangman_label.image = hangman_start
    global fails 
    fails = 11
 
    letter_entry.configure(state="normal")
    letter_entry.delete(0)

def clear_used_letters():
    used_letters_list.configure(text="")
    used_letters.clear()
    
letter_entry = tk.Entry(root, width=10)
letter_entry.pack(side="bottom", pady=25)
root.bind('<Return>', check_entry_error)

btn = tk.Button(root, text="Neues Wort", command=new_word)
btn.pack()

#Run GUI
root.mainloop()