# Simulator by Niraj Mali
#credits
'Music:'
'Fire Emblem Awakeing: Music 62'
'Youtube, Jojikiba: Walking on grass (sound effect)'
'MGQ Battle Sequence'

    

# Initiation
import os
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import random



# Window creation
root = Tk()
w = Label(root, text="Dialog Practice")
w.pack()

# Weapons
#dagger = 5
#sword = 10
#claws = 7

# Battle formulas
#dmg =
#pdmg =
#dmg


# Stats
hp = 20
attack = 0
defense = 0
spdef = 0
spd = 0

# Partner stats
php = 15
patk = 0
pdef = 0
psp = 0
pspd = 0

# Intro
os.startfile('wind.mp3')
messagebox.showinfo("...", "...Hey...")
messagebox.showinfo("...", "...Get up...")
os.startfile('opening.mp3')
messagebox.showinfo("", "Hey, you're up! I was starting to get worried there."
                    "What happened? You were all passed out.")

# Name
name = simpledialog.askstring("...""..." , "What's your name?")

# Intro2
choice1 = simpledialog.askstring("", "Well, nice to meet you " + name + ". "
                    "Let me take you to the town. I can get you help there."
                    "       "
                    "(A)Yeah, sure. I'm so tired. "
                    "(B)No I don't think so. I don't even know you.")
if choice1 != "A" or choice1 != "a":
    while choice1 != "A" or choice1 != "a":
        if choice1 == "b" or choice1 == "B":
            choice1 = simpledialog.askstring("", "Oh come on. Don't be like that. Come on "
                               "to the town with me."
                               "(A)Yeah, sure. I'm so tired."
                               "(B)No I don't think so. I don't even know you.")
        elif choice1 == "A" or choice1 == "a":
            break
        else:
            choice1 = simpledialog.askstring("", "What was that? I know you're tired "
                                        "but speak more clearly. "
                                        "       "
                                        "(A)I'll go with you."
                                        "(B)Um, how bout no.")

else:
    messagebox.showinfo("", "Good choice friend. Let's head on out.")
    os.startfile('walk1.mp3')
    messagebox.showinfo("", "Oh, I didn't get to introduce myself. My name is...")
    name2 = simpledialog.askstring("Partner's name", "")


messagebox.showinfo("", "Good choice friend. Let's head on out.")
os.startfile('walk1.mp3')
messagebox.showinfo("", "...")
messagebox.showinfo("", "Oh, I didn't get to introduce myself. My name is...")
name2 = simpledialog.askstring("Partner's name", "")
messagebox.showinfo(""+ name2 + "", "-" + name2 + ", pleased to meet you. Anyways, we"
                    "'re almost there. Just about-")
os.startfile('fall.mp3')
messagebox.showinfo(""+ name2 + "","Oh, sorry. I didn't see you there. Let "
                    "me-")
os.startfile('battle.mp3')
messagebox.showinfo("???", "Give your goods, now!")
messagebox.showinfo(""+ name2 +"", "Wha-what? I don't have anything I swear!")
messagebox.showinfo("???", "A shame. I'm not really taking no for an answer.")
messagebox.showinfo("" + name2 +"", "Oh shoot. Hey " + name + " I could really use "
                    "your help here. Look in my bag!")
messagebox.showinfo("Weapon", "Which weapon shall you choose?")

# Weapon choice
while attack == 0:
    weapon = simpledialog.askstring("Weapon", "(A) Dagger-Strike quick and find"
                                " the enemy's weak spot; Careful though you are more fragile; "
                                "(B) Sword-Take a strike and "
                                "kill the enemy; Be weary of your quick rivals(C) Claws-Speed is key, strike twice and "
                                "take the kill; you're very balanced which could be good or bad.")
    if weapon == "a" or weapon == "A":
        attack += 15
        defense += 10
        spdef +=15
        spd += 20
        crit = random.randint(1, 5)
        miss = random.randint(1, 6)
        messagebox.showinfo(""+ name2 +"", "Ah! the dagger, good choice. Hand"
                            " me a weapon too!")
        partner = simpledialog.askstring("Partner's Weapon", "(1) Sword (2)Claws")
        while patk == 0:                
            if ((partner == "1" and weapon == "a" or weapon == "A") or (partner == "2" and weapon == "C" or weapon == "c")):
                partner = "sword"
                patk += 18
                pdef += 15
                psp += 15
                pspd += 8
                pcrit = random.randint(1, 15)
                pmiss = random.randint(1, 20)                                                  
            elif ( partner == "2" and ((weapon == "a" or weapon == "A") or (weapon == "b" or weapon == "B"))):
                partner = "claws"
                patk += 15
                pdef += 15
                psp += 15
                pspd += 15
                ptwice = random.randint(1, 1)
                pcrit = random.randint(1, 10)
                pmiss = random.randint(1, 30)
            else:
                simpledialog.askstring("" + name2 + "", "What? Don't leave me hanging!")
                continue
        weapon = "dagger"


    elif weapon == "b" or weapon == "B":
        attack += 20
        defense += 17
        spdef += 17
        spd += 10
        crit = random.randint(1, 15)
        miss = random.randint(1, 20)
        messagebox.showinfo(""+ name2 +"", "Ah! the sword, good choice. Hand"
                            " me a weapon too!")
        partner = simpledialog.askstring("Partner's Weapon", "(1) Dagger (2)Claws")
        while patk == 0:
            if (partner == "1" and ((weapon == "b" or weapon == "B") or (weapon == "C" or weapon == "c"))):
                parner = "dagger"
                patk += 13
                pdef += 8
                psp += 13
                pspd += 18
                pcrit = random.randint(1, 5)
                pmiss = random.randint(1, 6)                                                                  
            elif ( partner == "2" and ((weapon == "a" or weapon == "A") or (weapon == "b" or weapon == "B"))):
                parner = "dagger"
                patk += 15
                pdef += 15
                psp += 15
                pspd += 15
                ptwice = random.randint(1, 1)
                pcrit = random.randint(1, 10)
                pmiss = random.randint(1, 30)
            else:
                simpledialog.askstring("" + name2 + "", "What? Don't leave me hanging!")
                continue
        weapon = "sword"
    elif weapon == "c" or weapon == "C":
        attack += 17
        defense += 17
        spdef += 17
        spd += 17
        twice = random.randint(1, 1)
        crit = random.randint(1, 10)
        miss = random.randint(1, 30)
        messagebox.showinfo(""+ name2 +"", "Ah! the claws, good choice. Hand"
                            " me a weapon too!")
        partner = simpledialog.askstring("Partner's Weapon", "(1) Dagger (2)Sword")
        while patk == 0:
            if (partner == "1" and ((weapon == "b" or weapon == "B") or (weapon == "C" or weapon == "c"))):
                partner = "dagger"
                patk += 13
                pdef += 8
                psp += 13
                pspd += 18
                pcrit = random.randint(1, 5)
                pmiss = random.randint(1, 6)                                                                  
            elif ( partner == "2" and ((weapon == "a" or weapon == "A"))):
                partner = "sword"
                patk += 15
                pdef += 15
                psp += 15
                pspd += 15
                ptwice = random.randint(1, 1)
                pcrit = random.randint(1, 10)
                pmiss = random.randint(1, 30)
            else:
                continue
                simpledialog.askstring("" + name2 + "", "What? Don't leave me hanging!")
        weapon = "claws"
    else:
        continue
# Enemy Stats, copy paste for each enemy to change stats, maybe weapons
ehp = 10
eatk =
edef =
esp =
espd =

                           
    






    

    

        
    

