from tkinter import *
import random

counter = 0
lastComplaining = 0

prewordFirst = ["newest ", "prettiest ", "most efficient ", "most intruiging ", "Fastest "]

objectsFirstClass = ["samsung galaxy s20", "samsung TV 3060",
           "newest iphone 10", "gaming laptop HP 5900",
           "Desktop Omen 7400"]

prewordSecond = ["most conftable ", "most colorfull ", "best quality ", "most qualified "]

objectsSecondClass = ["headphones Corsair 20", "Bed", "Gaming chair",
                      "keyboard", "backpack"]

prewordThirth = ["tastiest ", "best textured ", "best tasting ", "most expensive "]

objectsThirthClass = ["ramen", "chocolate bar", "pasta pack", "spaghetti's", "steak"]

prewordFourth = ["stupidest ", "wierdest ", "stinkiest ", "most overused ", "most valueless "]

objectsFourthClass = ["coin", "plug", "tech support joke", "waterbottle", "usb cable"]


end = ["TAKE IT DAMNIT", "no more", "for fuck sake", "i remove you from my scamming list!",
       "okay im done you annoy me!", "bye im gonna annoy someone else"]

allClasses = [prewordFirst, prewordSecond, prewordThirth, prewordFourth]
allObjects = [objectsFirstClass, objectsSecondClass, objectsThirthClass, objectsFourthClass]

sillyStartText = "CONGRATS, you have won the "

error = """
A problem has been detected and Windows has been shut down to prevent damage
to your computer.

PROCESS_INITIALIZATION_FAILED

If this is the first time you've seen this stop error screen, restart your computer. if this screen appears again, follow these steps:

Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for and Windows updates you might need.

If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing.
If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.

Technical information:

*** STOP: 0x000000FE (0x00000008, 0x000000006, 0x00000009, 0x847075cc)

***            4FQ.sys - Adress FWTV2022 base at 4s4M5000, Datestamp 4d5dd88c

Beginning morbing of physical memory
Physical memory morbing complete
Contact your system administrator or technical support for further
assistance
"""

def createInterface():
    global window
    global midLabel
    window = Tk()

    midLabel = Label(window, text="CONGRATS!!!\nYou have won the contest of python!!!", font = ("Arial", 20))
    midLabel.grid(row = 2, column = 1, columnspan = 5)

    rejectGiftButt = Button(window, text="reject", command=rejectGift, height = 10, width = 20, bg="red")
    rejectGiftButt.grid(row = 10, column = 1)

    acceptGiftButt = Button(window, text="accept", command=acceptGift, height = 10, width = 20, bg = "green")
    acceptGiftButt.grid(row = 10, column = 5, columnspan = 2)
    
    window.geometry("650x300")
    window.mainloop()

def rejectGift():
    global midLabel
    global counter
    global lastComplaining
    global window
    counter += 1
    textToBeSet = ""
    if counter < 5:
        textToBeSet = "You have Won the " + random.choice(allClasses[0]) + random.choice(allObjects[0])
    elif counter < 10:
        textToBeSet = "You have Won the " + random.choice(allClasses[1]) + random.choice(allObjects[1])
    elif counter < 15:
        textToBeSet = "You have Won the " + random.choice(allClasses[2]) + random.choice(allObjects[2])
    elif counter < 20:
        textToBeSet = "You have Won the " + random.choice(allClasses[3]) + random.choice(allObjects[3])
    else:
        textToBeSet = end[lastComplaining]
        lastComplaining += 1
        if len(end) == lastComplaining:
            window.destroy()
        
    
    midLabel.configure(text=textToBeSet)

def acceptGift():
    global window
    global Virus
    window.destroy()
    Virus = Tk()

    hiddenClose = Button(Virus, text=error, fg = "White", command=freePC, font=("calibri", 15), bg = "Blue",
                         borderwidth=0, justify= LEFT)
    hiddenClose.grid()

    Virus.configure(bg = "Blue")
    Virus.attributes('-topmost',True)
    Virus.attributes('-fullscreen',True)
    Virus.geometry("500x500")
    Virus.mainloop()

def freePC():
    global Virus
    Virus.destroy()

createInterface()







