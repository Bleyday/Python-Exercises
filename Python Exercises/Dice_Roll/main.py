import random
from PIL import Image, ImageTk
import tkinter as tk

dice = ["Dice_Roll/Assets/1.png", "Dice_Roll/Assets/2.png", "Dice_Roll/Assets/3.png", "Dice_Roll/Assets/4.png", "Dice_Roll/Assets/5.png", "Dice_Roll/Assets/6.png"]

def roll_the_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

root = tk.Tk()
root.title("Roll the Dice!")
root.geometry("300x600")

info = tk.Label(root, text ="What number will you get?")
btn = tk.Button(root, text="Roll the Dice!", command=roll_the_dice)

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tk.Label(root, image=image1)
label1.image = image1

info.pack()
btn.pack()
label1.pack( expand=True)


root.mainloop()
