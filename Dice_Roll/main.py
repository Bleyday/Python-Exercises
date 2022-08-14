from email.mime import image
import random
from PIL import Image, ImageTk
import tkinter as tk

dice = ["Dice_Roll/Assets/1.png", "Dice_Roll/Assets/2.png", "Dice_Roll/Assets/3.png", "Dice_Roll/Assets/4.png", "Dice_Roll/Assets/5.png", "Dice_Roll/Assets/6.png"]

def roll_the_dice():
    for labels in count_labels:
        globals()["image%s" %labels] = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        globals()["dice%s" %labels].configure(image=globals()["image%s" %labels])

count_labels = []
def count_dices(event):
    count = int(count_dice_entry.get())
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    for i in range(count):
        globals()['dice%s' % i] = tk.Label(root, image= image1)
        globals()['dice%s' % i].pack(expand= "true", padx=10, side="left" )
        globals()['dice%s' % i].image = image1

        global count_labels
        count_labels.append(i)

root = tk.Tk()
root.title("Roll the Dice!")

btn = tk.Button(root, text="Roll the Dice!", command=roll_the_dice)

count_dices_label = tk.Label(root, text ="How many Dices do you want to roll?")
count_dices_label.pack()
count_dice_entry = tk.Entry(root)
count_dice_entry.pack()

btn.pack()
root.bind('<Return>', count_dices)
root.mainloop()
