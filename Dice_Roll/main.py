import random
from PIL import Image, ImageTk
import tkinter as tk

dice = ["Dice_Roll/Assets/1.png", "Dice_Roll/Assets/2.png", "Dice_Roll/Assets/3.png", "Dice_Roll/Assets/4.png", "Dice_Roll/Assets/5.png", "Dice_Roll/Assets/6.png"]

def roll_the_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

def check_dices(event):
    

root = tk.Tk()
root.title("Roll the Dice!")
root.geometry("300x600")

btn = tk.Button(root, text="Roll the Dice!", command=roll_the_dice)

count_dices_label = tk.Label(root, text ="How many Dices do you want to roll?")
count_dices_label.pack()
count_dice_entry = tk.Entry(root)
count_dice_entry.pack()

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = tk.Label(root, image=image1)
label1.image = image1

btn.pack()
label1.pack( expand=True)

root.bind('<Return>', check_dices)
root.mainloop()
