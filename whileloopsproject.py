# Simulator by Niraj Mali
#credits
'Music:'
'Fire Emblem Awakening: Music 62'
'Fire Emblem Awakening: And what if I cant?'
'Fire Emblem Awakening: Conquest (Ablaze)'
'Youtube, Jojikiba: Walking on grass (sound effect)'
'MGQ Battle Sequence'
'Pokemon: Aquacorde Town'
'Pokemon: Unwavering Emotions'
'Pokemon: Team Aqua/Magma Hideout'
'Pokemon: Drought'
'Pokemon: Pallet Town Piano Cover'
'Pokmeon: vs Zinnia'
'Hajime no Ippo: Weight of my pride'

    

# Initiation
import os
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import random
import math
from turtle import *


# Window creation
root = Tk()
w = Label(root, text="Dialog Practice")
w.pack()

# Weapons
dag = 5
swd = 10
claw = 7

# Battle formulas
#dmg =
#pdmg =
#dmg

# Enemy Stats
ehp = 10
eatk = 10
edef = 10
esp = 10
espd = 10

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
exp = 0
global exp
# Define exp gain
def exp():
    global attack
    global defense
    global spd
    global patk
    global pdef
    global pspd
    global spdef
    global psp
    global hp
    global php
    lvl = 1
    exp = 0
    exp += eexp
    global lvl
    global exp
    while exp > 15:
        lvl += 1
        exp -= 15
        attack += 3
        defense += 2
        spdef += 3
        spd += 3
        hp += 3
    
        messagebox.showinfo("Level up!", "" + name + " grew to level "
                            "" + str(lvl) + ".")
        
    else:
        pass
    plvl = 1
    pexp = 0
    pexp += eexp
    global plvl
    global pexp
    while pexp > 18:
        patk += 3
        pdef += 3
        psp += 3
        pspd += 3
        plvl += 1
        exp -= 18
        messagebox.showinfo("Level up!", "" + name2 + " grew to level "
                            "" + str(plvl) + ".")
# Intro
os.startfile('wind.mp3')
messagebox.showinfo("RPG", "Welcome to the RPG game. No specifics. A tutorial"
                    " will be given. The game will take both strategy and luck"
                    " but is easy enough to play and is a basic program. Enjoy"
                    " and good luck!")
messagebox.showinfo("...", "...Hey...")
messagebox.showinfo("...", "...Get up...")
os.startfile('opening.mp3')
messagebox.showinfo("", "Hey, you're up! I was starting to get worried there."
                    " What happened? You were all passed out.")

# Name
name = simpledialog.askstring("...""..." , "What's your name?")

# Intro2
choice1 = simpledialog.askstring("...", """Well, nice to meet you """  + name +
                                 """. Let me take you to the town. I can get you help there.
                                 (A)Yeah, sure. I'm so tired.
                                 (B)No I don't think so. I don't even know you.""")
if choice1 != "A" or choice1 != "a":
    while choice1 != "A" or choice1 != "a":
        if choice1 == "b" or choice1 == "B":
            choice1 = simpledialog.askstring("", """Oh come on. Don't be like that. Come on to the town with me.
                                             (A)Yeah, sure. I'm so tired. 
                                             (B)No I don't think so. I don't even know you.""")
        elif choice1 == "A" or choice1 == "a":
            break
        else:
            choice1 = simpledialog.askstring("", """What was that? I know you're tired but speak more clearly. 
                                        (A)I'll go with you.
                                        (B)Um, how bout no.""")

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
    weapon = simpledialog.askstring("Weapon", """             (A) Dagger-Strike quick and find the enemy's weak spot; Careful though you are more fragile; 
                            (B) Sword-Take a strike and kill the enemy; Be weary of your quick rivals
                            (C) Claws-A balanced weapon. You've got the speed, the attack, and defense. Just don't let that get to your head""")
    if weapon == "a" or weapon == "A":
        attack += 22
        defense += 13
        spdef +=15
        spd += 20
        def crit():
            cr = random.randint(1, 5)
            if cr == 1:
                messagebox.showinfo("Critical!", "A critical hit!")
            else:
                pass
        miss = random.randint(1, 6)
        messagebox.showinfo(""+ name2 +"", "Ah! the dagger, good choice. Hand"
                            " me a weapon too!")
        
        while patk == 0:
            partner = simpledialog.askstring("Partner's Weapon", "(1) Sword (2)Claws")
            if ((partner == "1" and weapon == "a" or weapon == "A") or (partner == "2" and weapon == "C" or weapon == "c")):
                partner = swd
                patk += 16
                pdef += 16
                psp += 15
                pspd += 10
                def pcrit():
                    pcr = random.randint(1, 15)
                    if pcr == 1 or pcr == 15:
                        messagebox.showinfo("Crit!", ""+ name2 +"Critical hit!")
                    else:
                        pass
                pmiss = random.randint(1, 20)                                                  
            elif ( partner == "2" and ((weapon == "a" or weapon == "A") or (weapon == "b" or weapon == "B"))):
                partner = claw
                patk += 15
                pdef += 15
                psp += 15
                pspd += 15
                ptwice = random.randint(1, 1)
                def pcrit():
                    pcr = random.randint(1, 10)
                    if pcr == 1:
                        messagebox.showinfo("Crit!", ""+ name2 +"Critical hit!")
                    else:
                        pass
                pmiss = random.randint(1, 30)
            else:
                simpledialog.askstring("" + name2 + "", "What? Don't leave me hanging!")
                continue
        weapon = dag


    elif weapon == "b" or weapon == "B":
        attack += 18
        defense += 18
        spdef += 17
        spd += 12
        def crit():
            cr = random.randint(1, 15)
            if cr == 1:
                messagebox.showinfo("Critical!", "A critical hit!")
            else:
                pass
        miss = random.randint(1, 20)
        messagebox.showinfo(""+ name2 +"", "Ah! the sword, good choice. Hand"
                            " me a weapon too!")
        
        while patk == 0:
            partner = simpledialog.askstring("Partner's Weapon", "(1) Dagger (2)Claws")
            if (partner == "1" and ((weapon == "b" or weapon == "B") or (weapon == "C" or weapon == "c"))):
                partner = dag
                patk += 19
                pdef += 12
                psp += 13
                pspd += 18
                def pcrit():
                    pcr = random.randint(1, 5)
                    if pcr == 1:
                        messagebox.showinfo("Crit!", "Critical hit!")
                    else:
                        pass
                pmiss = random.randint(1, 6)                                                                  
            elif (partner == "2" and ((weapon == "a" or weapon == "A") or (weapon == "b" or weapon == "B"))):
                partner = claw
                patk += 15
                pdef += 15
                psp += 15
                pspd += 15
                ptwice = random.randint(1, 1)
                def pcrit():
                    pcr = random.randint(1, 10)
                    if cr == 1:
                        messagebox.showinfo("Crit!", "Critical hit!")
                    else:
                        pass
                pmiss = random.randint(1, 30)
            else:
                simpledialog.askstring("" + name2 + "", "What? Don't leave me hanging!")
                continue
        weapon = swd
    elif weapon == "c" or weapon == "C":
        attack += 17
        defense += 17
        spdef += 17
        spd += 17
        twice = random.randint(1, 1)
        def crit():
            cr = random.randint(1, 10)
            if cr == 1:
                messagebox.showinfo("Critical!", "A critical hit")
            else:
                pass
        miss = random.randint(1, 30)
        messagebox.showinfo(""+ name2 +"", "Ah! the claws, good choice. Hand"
                            " me a weapon too!")
        
        while patk == 0:
            partner = simpledialog.askstring("Partner's Weapon", "(1) Dagger (2)Sword")
            if (partner == "1" and ((weapon == "b" or weapon == "B") or (weapon == "C" or weapon == "c"))):
                partner = dag
                patk += 17
                pdef += 11
                psp += 13
                pspd += 18
                def pcrit():
                    pcr = random.randint(1, 5)
                    if pcr == 1:
                        messagebox.showinfo("Crit!", "A critical hit!")
                    else:
                        pass
                pmiss = random.randint(1, 6)                                                                  
            elif (partner == "2" and (weapon == "C" or weapon == "c")):
                partner = swd
                patk += 19
                pdef += 17
                psp += 15
                pspd += 12
                # How will the player attack twice as well as display the info
                """def ptwice():
                    two = random.randint(1, 1)
                    if two == 1:"""
                        
                def pcrit():
                    pcr = random.randint(1, 10)
                    if pcr == 1:
                        messagebox.showinfo("Crit!", "A critical hit!")
                    else:
                        pass
                pmiss = random.randint(1, 30)
                break
            else:
                messagebox.showinfo("" + name2 + "", "What? Don't leave me hanging!")
                continue
        weapon = claw
    else:
        continue
php = 17
# Enemy Stats, copy paste for each enemy to change stats, maybe weapons
ehp = 20
eatk = 12
edef = 13
esp = 10
espd = 10
eweap = 7
eexp = 10

#Additional damage random functions
add = random.randint(2, 6)

# Battle formulas
# Defining Twice and Miss functions for player
def mis():
    global battle
    misss = random.randint(1, 20)
    misss
    if (battle == "guard" or battle == "Guard"):
        global misss
        misss = random.randint(1, 7)
        if misss == 1:
            global damt
            damt = 0
            messagebox.showinfo("Dodge!", "" + name + " dodged the attack!")
        else:
            pass
    elif misss == 1:
        global damt
        damt = 0
        messagebox.showinfo("Miss!", "The enemy missed the attack!")
    
    else:
        pass



# Player
def dmg():
    if weapon == "c" or weapon == "C":
        twice
        if twice == 1:
            global ehp
            damg = (attack + weapon) - (edef)
            ehp -= damg
            messagebox.showinfo("Battle", "You dealed " + str(damg) + " damage.")
            damg /= 2
            ehp -= damg
            messagebox.showinfo("Battle", "You dealed an additional " + str(damg) + "/n"
                                "damage! Double hit!")
        else:
            global ehp
            damg = (attack + weapon) - (edef)
            ehp -= damg
            messagebox.showinfo("Battle", "You dealed " + str(damg) + " damage.")
            damg /= 2
    else:
        global ehp
        damg = (attack + weapon) - (edef)
        ehp -= damg
        messagebox.showinfo("Battle", "You dealed " + str(damg) + " damage.")
        
            
def dmt():
    global battle
    if battle == "attack" or battle == "Attack" or battle == "item" or battle == "Item":
        global hp
        damt = (eatk + eweap) - (defense + spd/2) + add
        hp -= damt
        mis()
        messagebox.showinfo("Battle", "You took " + str(damt) + " damage.")

    elif battle == "guard" or battle == "Guard":
        global hp
        damt = (eatk + eweap) - (defense + spd/2) + add
        global damt
        mis()
        damt /= 2
        hp -= damt
        messagebox.showinfo("Battle", "You took a reduced " + str(damt) + " damage.")

# Partner
def pdmg():
    global php
    global ptwice
    while php > 0:
        if partner == 2 and (weapon != "c" or weapon != "C"): 
            ptwice
            if ptwice == 1:
                global ehp
                pdamg = (patk + partner) - (edef)
                ehp -= pdamg
                messagebox.showinfo("Battle", "" + name2 + " dealed " + str(pdamg) + " damage.")
                pdamg /= 2
                ehp -= pdamg
                messagebox.showinfo("Battle", "" + name2 + " dealed an additional"
                                    " " + str(pdamg) + " damage! Double hit!")
                break
            else:
                global ehp
                pdamg = ((patk + partner)/2) - (edef/2)
                ehp -= pdamg
                messagebox.showinfo("Battle", "" + name2 + " dealed " + str(pdamg) + " damage.")
                break
        else:
            global ehp
            pdamg = ((patk + partner)/2) - (edef/2)
            ehp -= pdamg
            messagebox.showinfo("Battle", "" + name2 + " dealed " + str(pdamg) + " damage.")
            break
    if php <= 0:
        php = 0
        messagebox.showinfo("Battle", "" + name2 + " can't go on!")
    else:
        pass
def pdmt():
    if php > 0:
        global php
        padamt = ((eweap + eatk)) - (pdef + pspd/2) + add
        php -= padamt
        messagebox.showinfo("Battle", "" + name2 + " took " + str(padamt) + " damage.")
    else:
        global php
        php = 0
        messagebox.showinfo("Battle", "" + name2 + " can't go on!")
        
# Damaging partner or damaging player
def victim():
    if php <= 0:
        vic = random.randint(1, 1)
        if vic == 1:
            dmt()
        else:
            dmt()
    else:
        vic = random.randint(1, 2)
        if vic == 1:
            dmt()
        else:
            pdmt()
        

# Exp
exp = 0
pexp = 0
lvl = 1
plvl = 1

# HP Resetter Variables
bhp = 20 + (lvl * 5) -5
bphp = 15 + (plvl * 5) -5

# Battle Choices
def battleseq():
    global hp
    global php
    global ehp
    global exp
    global pexp
    global pspd
    global spd
    global espd
    global attack
    global defense
    global patk
    global pdef
    hp
    while ehp > 0:
        if hp <= 0:
            root.destroy()
            os._exit
            os.startfile('death.mp3')
            messagebox.showinfo("" + name2 + "", "Stay with me! No, you can't!"
                            " Don't-")
            messagebox.showinfo(". . .", "" + name + " took too much "
                                "damage and failed to complete his journey."
                                " Thus, ended " + name + " and " + name2 + "'s journey.")
            messagebox.showinfo("TIPS", "When given the opportunity to train, get the"
                                " experience to be stronger. Also, some pairs of wea"
                                "pons are better than others.")
            messagebox.showinfo("You Lost", "You lost")
            root.destroy()
            os._exit
            
            
        else:
            battle = simpledialog.askstring("Battle",
                                            "\n       HP: " + str(hp) + "" + \
                                            "\n"
                                            "\n       Partner HP: " + str(php) + ""
                                            "\n"
                                            "\n       " + ename + ": " + str(ehp) + ""
                                            "\n" 
                                            "\nChoose: Attack, Guard, Item")
            global battle
            if battle == "Attack" or battle == "attack":
                if spd >= espd and spd >= pspd:
                    dmg()
                    if pspd >= espd:
                        pdmg()
                        victim()
                    else:
                        victim()
                        pdmg()
                                
                                
                elif spd >= espd and spd <= pspd:
                    pdmg()
                    dmg()
                    victim()

                elif spd <= espd and spd >= pspd:
                    victim()
                    dmg()
                    pdmg()
                            
                            
                else:
                    if pspd >= espd:
                        pdmg()
                        victim()
                        dmg()
                    else:
                        victim()
                        pdmg()
                        dmg()
            elif battle == "guard" or battle == "Guard":
                messagebox.showinfo("Battle", "" + name + " took a defensive stance.")
                if spd >= espd and spd >= pspd:
                    if pspd >= espd:
                        pdmg()
                        victim()
                    else:
                        victim()
                        pdmg()
                                
                                
                elif spd >= espd and spd <= pspd:
                    pdmg()
                    victim()

                elif spd <= espd and spd >= pspd:
                    victim()
                    pdmg()
                            
                            
                else:
                    if pspd >= espd:
                        pdmg()
                        victim()
                    else:
                        victim()
                        pdmg()
            elif battle == "item" or battle == "Item":
                hp += (bhp/4)
                messagebox.showinfo("Battle", "" + name + " healed "
                                    "" + str(bhp/4) + " health!")

                if spd >= espd and spd >= pspd:
                    if pspd >= espd:
                        pdmg()
                        victim()
                    else:
                        victim()
                        pdmg()
                                
                                
                elif spd >= espd and spd <= pspd:
                    pdmg()
                    victim()

                elif spd <= espd and spd >= pspd:
                    victim()
                    pdmg()
                            
                            
                else:
                    if pspd >= espd:
                        pdmg()
                        victim()
                    else:
                        victim()
                        pdmg()
            else:
                continue
    
    global bhp
    global bphp
    global lvl
    global plvl
    hp = bhp
    php = bphp
    exp += eexp
    messagebox.showinfo("Battle", "" + name + " gained " + str(eexp) + " experience points.")
    while exp > 15:
        exp -= 15
        lvl += 1
        messagebox.showinfo("Level Up!", "" + name + " has reached level " + str(lvl) + "."
                            " All stats were upped by 4!")
        spd += 4
        attack += 4
        defense += 4
        bhp +=5
    else:
        pass
    pexp += eexp
    messagebox.showinfo("Battle", "" + name2 + " gained " + str(eexp) + " experience points.")
    while pexp > 17:
        pexp -= 17
        plvl += 1
        messagebox.showinfo("Level Up!", "" + name2 + " has reached level " + str(lvl) + "."
                            " All stats were upped by 4!")
        pspd += 4
        patk += 4
        pdef += 4
        bphp += 5
    else:
        pass
        

# Battle 1
ename = "???"
messagebox.showinfo(""+ name2 + "", "Alright let's do this. I'm "
                       "not too bad of a fighter but we have  to play this smart. "
                       "We can't run otherwise we'll get ourselves killed. "
                       "But we can fight, use items, and guard.")

while ehp > 0:
    tutorial = simpledialog.askstring("" + name2 + "", "Do want me to explain "
                                  "how these work? (yes/no)")
    if tutorial == "Yes" or tutorial == "yes":
        messagebox.showinfo("" + name2 + "", "OK, we'll start with guard."
                        " if you guard, you'll take less damage and "
                        "might have a better chance to dodge. Try it out.")
        battle = simpledialog.askstring("Guard", "Type guard.")
        if battle == "guard" or battle == "Guard":
            dmt()
            
        else:
            dmt()
        messagebox.showinfo("Stats", "Your HP: " + str(hp) + "; Partner's HP: " + str(php) + " ;        Enemy HP: " + str(ehp) + ".")
        messagebox.showinfo("" + name2 + "", "Nice, you would've"
                                        " some more damage had you attacked."
                                        " But be weary, you can't attack while"
                                        " guarding. But since there's two of "
                                        "us, I can attack if they try to attack"
                                        " you. So make sure you play it smart.")
        battle = simpledialog.askstring("" + name2 + "", "Now, let's try attack."
                                        "You'll deal damage and hopefully be able"
                                        " to defeat them. Sometimes you might"
                                        " find an opening to deal extra damage. Try it."
                                        " Type attack.")
        if battle == "Attack" or battle == "attack":
            dmg()
        else:
            dmg()
        messagebox.showinfo("" + name + "", "Nice! Lastly, let me tell you"
                            " about items. Some can heal while others will"
                            " buff your power. But the same thing as guard, "
                            "you're vulnerable to an attack. Try to heal.")
        battle = simpledialog.askstring("Battle", "Type item.")
        if battle == "item" or battle == "item":
            hp += (hp/4)
            messagebox.showinfo("Heal!", "You healed " ,)
        else:
            hp += (hp/4)
            messagebox.showinfo("Heal!", "You healed 10 HP!")
        messagebox.showinfo("Stats", "Your HP: " + str(hp) + ";        Enemy HP: " + str(ehp) + ".")
        
        messagebox.showinfo("" + name2 + "", "Great! That's all there is"
                            " too it. Now let's finish this guy.")
        messagebox.showinfo("???", "What...? You guys are strong. Guess I gotta"
                            " try harder.")
        ehp = 20
        messagebox.showinfo("???", "The enemy is fully healed!")
        messagebox.showinfo("" + name2 + "", "Whoa, guess we under"
                            "esimated him. Let's make sure we stay"
                            " on guard.")

        battleseq()
        pass
        
           
                                        
    elif tutorial == "no" or tutorial == "No":
        
        battleseq()
                        
                    
                        
                    
                                                
    else:
        continue
os.startfile('vic1.mp3')
messagebox.showinfo("TIPS:", "You only lose if " + name + " (the player) "
                    "runs out of health. After each battle experience"
                    " points are gained. Training will allow you to ga"
                    "in more experience points so take advantage.")
messagebox.showinfo("???",
                    "Grr... Guess you two are stronger than I thought."
                    " Can't believe I lost. I'll be back though")
messagebox.showinfo("???",
                    "You kids don't know who you're messing with.")
messagebox.showinfo("" + name2 + "",
                    "Yeah get out of here scum. " + name + ", you did"
                    " a really nice job back there! I'm impressed at "
                    "how you handled that weapon. I've n"
                    "ever seen anyone do that...")
choice = simpledialog.askstring("" + name2 + "",
                                "Anyways, don't worry about it. By the way"
                                "\nare you ready to go to town? Or do you want to do some training?" + \
                                "\n              (A) Let's head to town."
                                "\n              (B) Need to get stronger. Let's train.")

while choice != "a" or choice == "A":
    if choice == "b" or choice == "B":
        # Enemy Stats, copy paste for each enemy to change stats, maybe weapons
        ehp = 20
        eatk = 15
        edef = 18
        esp = 15
        espd = 13
        eweap = 10
        eexp = 2

        messagebox.showinfo("" + name2 + "", "Alright, I'll leave you too it. "
                            "Let me know when you're ready.")
        os.startfile('battle.mp3')
        battleseq()
        os.startfile('vic1.mp3')
        choice = simpledialog.askstring("" + name2 + "",
                                "Nice moves out there! You don't get much exeperience for hitting a "
                                "\nrock but still nice. What's the plan now? Town or train some more?" + \
                                "\n(A) Let's head to town."
                                "\n(B) Need to get stronger. Let's train.")
        if choice == "A" or choice == "a":
            break
        else:
            continue
    elif choice == "b" or choice == "B":
        break
    else:
        choice == simpledialog.askstring("" + name2 + "",
                            "\nWhat was that?" + \
                            "\n      (A) Sorry. Let's head to town"
                            "\n      (B) Let's train some more")
        continue

#At the inn and backstories

messagebox.showinfo("" + name2 + "", "Alright, to town it is. Let's make sure"
                    " you get taken care of.")
os.startfile('town.mp3')
messagebox.showinfo("" + name2 +  "",
                    "Well, here we are. Now the inn should be- Ah! "
                    "There it is! Come on, you can rest up there.")
messagebox.showinfo("Innkeeper", "Oh, hello there " + name2 + ". I"
                    " see that you've brought a friend along.")
messagebox.showinfo("" + name2 + "", "Haha, yup. He's been through"
                    " quite a bit. I found him unconscious on the "
                    "road and we were attacked. But he proved to be "
                    "quite the capable fighter.")
messagebox.showinfo("Innkeeper", "Well, just head on up and you'll find"
                    " " + name2 + "'s room. By the way what was your name?"
                    "... Oh, " + name + " is it? Well pleased to make your"
                    " acquaintance. And please, enjoy your stay.")
messagebox.showinfo("" + name2 + "", "Thanks. " + name + ", after you"
                    "r rest, find me and I'll help you out, ok?"
                    " See you then.")
messagebox.showinfo("" + name + "", "" + name + " went to sleep!")
os.startfile('emotion.mp3')
messagebox.showinfo("" + name + "", "" + name + " woke up and looked "
                    "around. Heading downstairs, he hears banging"
                    " sounds. Looking around, he sees " + name2 + ""
                    ". " + name + " heads towards him.")
messagebox.showinfo("" + name2 + "", "Hah! Take that! No, no, no! "
                    "I can't help people if I can't get that move"
                    " down... Oh! " + name + "! I, uh, didn't see"
                    " you there. Yeah I train by myself a lot...")
choice = simpledialog.askstring("" + name + "",
                                "\n    (A) Training without me? Let me join!" + \
                                "\n    (B) What's up? Something bothering you?"
                                "\n    (C) Come on, back to the inn.")
while choice != "c" or choice != "C":
    if choice == "a" or choice == "A":
        messagebox.showinfo("" + name2 + "", "Really? Alright, uh, let's get started")
        messagebox.showinfo("Knight", "Hey, are you two training too?"
                            " Why don't we spar?")
        messagebox.showinfo("" + name2 + "",
                            "Hey, sounds good. Ready for this " + name + "?")
        os.startfile('battle2.mp3')
        ehp = 25
        eatk = 17
        edef = 16
        esp = 15
        espd = 18
        eweap = 10
        eexp = 8
        ename = "Knight"
        battleseq()
        os.startfile('vic1.mp3')
        messagebox.showinfo("Knight", "Whoa, you two are tough!"
                            " Ha, didn't think you had it in ya."
                            " Ever think of joining the guard?")
        messagebox.showinfo("" + name2 + "",
                            "Ha, you weren't so bad yourself. "
                            "And we'll definitely think about your offer."
                            " Anyways, take it easy.")
        messagebox.showinfo("Knight", "Same to you! See you later!")
        messagebox.showinfo("" + name2 + "", "That guy was pretty tough."
                            " Anyways, let's head back to the inn. Also,"
                            " " + name + "? Thanks. I really needed that.")
        break

    elif choice == "B" or choice == "b":
        messagebox.showinfo("" + name2 + "", "*Sigh* Well, " + name + ""
                            ", I never told you this but... My parent's wer"
                            "e murdered by the gang that terrorizes the area"
                            " around here. I grew up fending for myself and...")
        messagebox.showinfo("" + name2 + "", "...")
        messagebox.showinfo("" + name2 + "", "...I'm just so freaking angry."
                            " They need to be taken down! AHHHH!! ...")
        messagebox.showinfo("" + name2 + "", "Sorry. You didn't deserve"
                            " that. But... I really appreciate your concern."
                            " My parents may have died but they must've thought"
                            " ahead, cause they left me these weapons and a "
                            "good reputation. That's why I vowed to fight for"
                            " those who can't fight for themselves.")
        messagebox.showinfo("" + name2 + "", "It's just what keeps me going."
                            " I'm sure you have your own dreams too, but I w"
                            "on't pester you about that.")
        os.startfile('town.mp3')
        choice = simpledialog.askstring("" + name + "",
                                "\nAnyways, thanks for listening. What do you want to do now?" + \
                                "\n    (A) Let's train some more!"
                                "\n    (B) Can I here your story again?"
                                "\n    (C) Come on, back to the inn.")
        continue

    elif choice == "C" or choice == "c":
        break
    
    else:
        choice = simpledialog.askstring("" + name + "",
                                "\n    (A) Training without me? Let me join!" + \
                                "\n    (B) What's up? Something bothering you?"
                                "\n    (C) Come on, back to the inn.")
messagebox.showinfo("" + name2 + "", "Alright then. Let's head back to the"
                    " inn.")
os.startfile('silence.mp3')
messagebox.showinfo("Civilian", "Someone help!!")
os.startfile('encounter.mp3')
messagebox.showinfo("" + name2 + "", "That didn't sound good. Come on"
                    " " + name + ", let's go!")
messagebox.showinfo("Thug", "Lady, give me your jewelry or else!")
messagebox.showinfo("Civilian", "N-no, please!")
messagebox.showinfo("" + name2 + "", "Hey, let her go! You're gonna"
                    " have to go through us first!")
messagebox.showinfo("Thug", "Ha, I finally found you!")
messagebox.showinfo("" + name2 + "", "Wha-What?")
messagebox.showinfo("Thug", "You won't get away with what you did to the boss.")
messagebox.showinfo("" + name2 + "", "Whoa! This guy means business!"
                    " " + name + ", get ready!")

ehp = 28
eatk = 22
edef = 20
esp = 15
espd = 19
eweap = 10
eexp = 13
ename == "Thug"
battleseq()
messagebox.showinfo("Thug", "The boss wasn't kidding about your guy's"
                    " strength... Guess I'll have to get the rest of the gang.")
messagebox.showinfo("" + name2 + "",
                    "Whoa, that guy was actually pretty tough. He's gonna get"
                    " the rest of the gang soon...")
choice = simpledialog.askstring("" + name2 + "",
                                "\n" + name + ", what should we do?" + \
                                "\n     (A) We should check on the lady that got mugged."
                                "\n     (B) Let him go? We gotta strike first!")
while choice != "a" or choice == "A" or choice != "b" or choice != "B":
    if choice == "a" or choice == "A":
        messagebox.showinfo("" + name2 + "", "Yeah, you're right. Let's go see"
                            " how she's doing.")
        os.startfile('civilian.mp3')
        messagebox.showinfo("" + name2 + "", "Hey there. You took quite"
                            " the experience there ma'am. Are you alright?")
        messagebox.showinfo("Civilian", "Oh, I'm fine thank you. By the loo"
                            "ks of it, he was after you. I know some doctors"
                            " if you need anything.")
        messagebox.showinfo("" + name2 + "", "We're fine, thank you. That"
                            " thug was no match for us. But do you know a"
                            "nything of what he was talking about?")
        messagebox.showinfo("Civilian", "Well, these are only rumors but..."
                            " I heard the gang that thug was in is trying t"
                            "o activate the ancient stones.")
        os.startfile('silence.mp3')
        messagebox.showinfo("" + name2 + "", "Wait. Did you say the ancient stones?")
        messagebox.showinfo("Civilian", "Yes. The very same stones of ancient lege"
                            "nd. I thought it was just a myth but some people thin"
                            "k that the gang might actually do it.")
        os.startfile('danger.mp3')
        messagebox.showinfo("" + name2 + "", "Oh, no. This is bad...")
        messagebox.showinfo("" + name2 + "", "" + name + "! We have to"
                            " stop them. If they activate those stones,"
                            " the entire world will be in danger. I'll"
                            " tell you about them while we go there. "
                            "Come on!")
        messagebox.showinfo("" + name2 + "", "*Huff, huff* Alright " + name + ""
                            " here's the deal. Long ago, there was a lot of"
                            " magic in the world. Like actual dark, deadly ma"
                            "gic. People got sick of the magic users because "
                            "of the chaos they caused and attempted to eradic"
                            "ate all magical wielders. As a last ditch attemp"
                            "t to have revenge against these people, magic wi"
                            "elders made a weapon. It wiped out almost the en"
                            "tire population and took out all magic users.")
        messagebox.showinfo("" + name2 + "", "We have to stop them at all costs"
                            ". If we don't... ")
        messagebox.showinfo("Thug", "Hey, you two!")
        os.startfile('encounter.mp3')
        messagebox.showinfo("" + name2 + "", "Crap, they're here!")
        messagebox.showinfo("Thug", "Heh, did you think I'd actually let you"
                            " two go off after embarassing me?")
        messagebox.showinfo("" + name2 + "", "It's over! We know what you're "
                            "up too! We won't let you activate the ancient rocks!")
        messagebox.showinfo("Thug", "Heh, so you found out? I might've let"
                            " you two go before but now I definitely have to"
                            " kill you. I got friends too now!")
        messagebox.showinfo("" + name2 + "", "" + name + "! We can't waste time"
                            " here! Just take out a few and let's book it to the"
                            " rocks!")
        messagebox.showinfo("Heavy Thug", "You two won't get away!")
        messagebox.showinfo("" + name2 + "", "First up. Let's do it!")
        ehp = 35
        eatk = 23
        edef = 26
        esp = 15
        espd = 11
        eweap = 12
        eexp = 11
        ename = "Heavy Thug"
        battleseq()
        os.startfile('encounter.mp3')
        messagebox.showinfo("" + name2 + "", "That took awhile but I think the"
                            " other thugs are getting nervous.")
        messagebox.showinfo("Mercenary", "You two look like a challenge"
                            ". Why don't I stain your blood on my new blade?")
        messagebox.showinfo("" + name2 + "", "He looks tough... Be careful "
                            "" + name + "!")
        ehp = 30
        eatk = 27
        edef = 23
        esp = 15
        espd = 21
        eweap = 17
        eexp = 15
        ename = "Mercenary"
        os.startfile('battle.mp3')
        battleseq()
        os.startfile('danger.mp3')
        messagebox.showinfo("Mercenary", "H-How can this be? Urgh...")
        messagebox.showinfo("" + name2 + "", "They're all shocked we beat"
                            " that guy! Now's our chance, run!")
        messagebox.showinfo("" + name2 + "", "I see it! There's the ancient r"
                            "ocks! We're almost there!")
        break
        
        
        
        
           
        

    elif choice == "b" or choice == "B":
        messagebox.showinfo("" + name2 + "",
                            "Alright, let's go after them!")
        os.startfile('base.mp3')
        messagebox.showinfo("" + name2 + "", "From I heard, they hang out a"
                            "round here. But I don't-")
        messagebox.showinfo("Gang Guard", "Hey you two!")
        messagebox.showinfo("" + name2 + "", "Crap! We're spotted!")
        messagebox.showinfo("Gang Guard", "You two... You two must be the"
                            " ones the boss was talking about! Heh, must b"
                            "e pretty strong if you actually survived an e"
                            "ncounter with him.")
        messagebox.showinfo("" + name2 + "", "Take us to your boss! Or"
                            " do we have to do it the hard way?")
        messagebox.showinfo("Gang Guard", "Ha. Tough talk for the two of"
                            " you. Bring it on!")
        messagebox.showinfo("" + name2 + "", "Alright " + name + ". It's time"
                            " to bring justice!")
        ehp = 30
        eatk = 30
        edef = 21
        esp = 15
        espd = 18
        eweap = 12
        eexp = 12
        ename = "Gang Guard"
        battleseq()
        os.startfile('vic1.mp3')
        messagebox.showinfo("Gang Guard", "Hah...hah... The boss was right"
                            " about your strength. But by now, they must'v"
                            "e done it.")
        messagebox.showinfo("" + name2 + "", "Done what?")
        messagebox.showinfo("Gang Guard", "Heheh, activate the ancient rocks.")
        os.startfile('silence.mp3')
        messagebox.showinfo("" + name2 + "", "W-What did you say?")
        messagebox.showinfo("Gang Guard", "You heard me, the ancient rocks.")
        os.startfile('danger.mp3')
        messagebox.showinfo("Gang Guard", "The boss was worried that you mi"
                            "ght interfere with our affairs so he sent som"
                            "e of us to distract you. Soon, we'll have con"
                            "trol of the whole world. And there's nothing y"
                            "ou can do about it.")
        messagebox.showinfo("" + name2 + "", "No... No, no, no! This can't be!"
                            " " + name + "! We have to go. Now! I'll tell you"
                            " about it on the way, just follow me!")
        messagebox.showinfo("" + name2 + "", "*Huff, huff* Alright " + name + ""
                            " here's the deal. Long ago, there was a lot of"
                            " magic in the world. Like actual dark, deadly ma"
                            "gic. People got sick of the magic users because "
                            "of the chaos they caused and attempted to eradic"
                            "ate all magical wielders. As a last ditch attemp"
                            "t to have revenge against these people, magic wi"
                            "elders made a weapon. It wiped out almost the en"
                            "tire population and took out all magic users.")
        messagebox.showinfo("" + name2 + "", "We're almost there, just over-")
        messagebox.showinfo("Thug Brawler", "Hah! Where do you think you're going?")
        os.startfile('encounter.mp3')
        messagebox.showinfo("" + name2 + "", "No, not now!")
        messagebox.showinfo("Thug Brawler", "From the looks of it, you're heading"
                            " in the wrong direction. Let me show you the right way!")
        messagebox.showinfo("" + name2 + "", "" + name + ", we have to make this"
                            " quick. Let's do it!")
        os.startfile('battle.mp3')
        ehp = 28
        eatk = 27
        edef = 21
        esp = 15
        espd = 23
        eweap = 14
        eexp = 10
        ename = "Thug Brawler"
        battleseq()
        os.startfile('danger.mp3')
        messagebox.showinfo("" + name2 + "", "No time! We gotta go " + name + ".")
        messagebox.showinfo("" + name2 + "", "There it is! We made it.")
        break
  
        
        
                            

    else:
        choice = simpledialog.askstring("" + name2 + "",
                                "\n" + name + ", what should we do?" + \
                                "\n     (A) We should check on the lady that got mugged."
                                "\n     (B) Let him go? We gotta strike first!")
        continue
messagebox.showinfo("" + name2 + "", "Hey! We're here to stop you!")
messagebox.showinfo("???", "So you finally made it!")
messagebox.showinfo("" + name2 + "", "Hang on... You're the one that at"
                    "tacked us on the road! Don't tell me your-")
messagebox.showinfo("???", "Heh, that's right. I'm the boss of this here gang"
                    ". And we will succeed in activating the weapon.")
messagebox.showinfo("" + name2 + "", "You won't get away with this... Um...")
messagebox.showinfo("???", "Ha! Don't even know the enemy's name do you? "
                    "Very well...")
messagebox.showinfo("Catalyz", "You may call me Catalyz. And you are about "
                    " to die. Mikel!")
messagebox.showinfo("Mikel", "You should be honored. The flesh that this bla"
                    "de touches is only those of the strongest warriors.")
messagebox.showinfo("" + name2 + "", "" + name + "! This is it. We have to "
                    "defeat them. Otherwise it's game over. Let's do it!")
os.startfile('mikel.mp3')
ehp = 34
eatk = 31
edef = 28
esp = 15
espd = 32
eweap = 17
eexp = 20
ename = "Assassin Mikel"
battleseq()
os.startfile('civilian.mp3')
messagebox.showinfo("Mikel", "How? How can such powerful strength be possible"
                    "? Hrgh, ugh...")
messagebox.showinfo("" + name2 + "", "It's over Catalyz! You've lost!")
messagebox.showinfo("Catalyz", "Mikel lost. Not I. Let me tell you something"
                    ", back on the road, I was hardly trying. Though I was a"
                    " bit shocked you beat me even at half my strength I can"
                    " assure you that I will not make the same mistake again"
                    ".")
messagebox.showinfo("" + name2 + "", "" + name + "! I don't think he's bluff"
                    "ing. But we've gotten stonger too! We won't let you des"
                    "troy the world!")
messagebox.showinfo("Catalyz", "Destroy the world? Haha, you're mistaken if y"
                    "ou think I'd destroy the world I oh so want to conquer!")
messagebox.showinfo("" + name2 + "", "What? What else are you going to do wi"
                    "th them?")
messagebox.showinfo("Catalyz", "Hahahaha! You'll seen soon enough. Now come"
                    " at me!")
os.startfile('boss.mp3')
ehp = 40
eatk = 36
edef = 33
esp = 15
espd = 29
eweap = 19
eexp = 25
ename = "Catalyz"
battleseq()
messagebox.showinfo("" + name2 + "", "We-We did it!")
messagebox.showinfo("Catalyz", "Yes but you're too late. Now I will do the"
                    " ritual.")
messagebox.showinfo("Catalyz", "FUSION")
os.startfile('danger.mp3')
messagebox.showinfo("" + name2 + "", "Fusion? What's he doing?"
                    " " + name + ", get back!")
messagebox.showinfo("Catalyz", "AHWOOOOOHHH!!!")
os.startfile('silence.mp3')
messagebox.showinfo("" + name2 + "", "...Oh god. " + name + ", it's impos"
                    "sible, but we have to stop him. This is it.")
os.startfile('boss2.mp3')
messagebox.showinfo("Ancient Catalyz", "...You two will not stop me.")
messagebox.showinfo("Ancient Catalyz", "BUT I WILL BE GLAD TO KILL YOU")
ehp = 60
eatk = 48
edef = 42
esp = 15
espd = 27
eweap = 22
eexp = 28
ename = "Ancient Catalyz"
battleseq()
os.startfile('battle2.mp3')
messagebox.showinfo("" + name2 + "", "*Huff* We actually... we actually "
                    "defeated him.")
messagebox.showinfo("Ancient Catalyz", "How? How can this be possible?"
                    " I did everything. I am fused with the ultimate w"
                    "eapon! How did I lose!?")
os.startfile('silence.mp3')
messagebox.showinfo("???", "Because you are weak.")
messagebox.showinfo("" + name2 + "", "Wha-Who said that?")
messagebox.showinfo("???", "Puny mortal. You really thought that you could ta"
                    "me my power? I will show you the true power of The Grea"
                    "t Ancient!")
messagebox.showinfo("Ancient Catalyz", "What? What is this- AAAHHHHH!!")
messagebox.showinfo("...", "FWOOOM!")
messagebox.showinfo
messagebox.showinfo("" + name2 + "", "What is that?")
os.startfile('final.mp3')
messagebox.showinfo("The Great Ancient", "I am The Great Ancient! I am the d"
                    "ark power that once destroyed the world! And now my powe"
                    "r has been awakened. Prepare to be defeated mortal!")
messagebox.showinfo("" + name2 + "", "" + name + "! This is it! If we lose"
                    " here, we lose everything!")
choice = simpledialog.askstring("" + name2 + "", "\nAre you ready for this?" + \
                                "\n     (A) Ready when you are friend!"
                                "\n     (B) This is it... We won't lose!"
                                "\n     (C) Uh, can I take a quick bathroom break?")
while choice != "a" or choice != "A" or choice != "b" or choice != "B" or choice != "c" or choice != "C":
    if choice == "a" or choice == "A":
        messagebox.showinfo("" + name2 + "", "Friend... I haven't heard that"
                            " for so long. Thank you for standing by my side!"
                            " I won't let you down " + name + "!")
        break
    elif choice == "b" or choice == "B":
        messagebox.showinfo("" + name2 + "", "That's the spirit! Let's finis"
                            "h this once and for all!")
        break
    elif choice == "c" or choice == "C":
        messagebox.showinfo("" + name2 + "", "Man, able to joke in a time like"
                            " this... I hope you're ready " + name + "!"
                            " Everything rides on this battle!")
        break
    else:
        choice = simpledialog.askstring("" + name2 + "", "\nAre you ready for this?" + \
                                "\n     (A) Ready when you are friend!"
                                "\n     (B) This is it... We won't lose!"
                                "\n     (C) Uh, can I take a quick bathroom break?")
        continue
messagebox.showinfo("" + name2 + "", "Great Ancient! Your reign will end just a"
                    "s it begun! I, " + name2 + " and my partner " + name + ""
                    " will defeat you!")
messagebox.showinfo("The Great Ancient", "Hahahaha... You think you can"
                    " defeat me?")
messagebox.showinfo("" + name2 + "", "You will not succeed. Prepare to "
                    "be defeated!")
messagebox.showinfo("The Great Ancient", "Hahahaha...")
messagebox.showinfo("The Great Ancient", "COME AT ME")
ehp = 80
eatk = 53
edef = 50
esp = 15
espd = 40
eweap = 26
eexp = 30
ename = "The Great Ancient"
battleseq()
os.startfile('endgame.mp3')
messagebox.showinfo("The Great Ancient", "No! I am the ultimate weapon! I can"
                    "not be defeated! You two are just mortals! How is this p"
                    "ossible?")
messagebox.showinfo("" + name2 + "", "" +  name + "! Let's finish this!")

ehp = 100
eatk = (pdef + pspd/2) - add
edef = 40
esp = 15
espd = 1
eweap = 0
eexp = 30
ename = "The Great Ancient: Ancient Core"
battleseq()
messagebox.showinfo("The Great Ancient", "The ultimate weapon... is defeated.")
messagebox.showinfo("" + name2 + "", "*Huff* We did it... we saved the world..."
                    " " + name + "... We did it...")
choice = simpledialog.askstring("" + name + "",
                                "\n (A) Haha, yeah we sure did..." + \
                                "\n (B) Are you sure we did?"
                                "\n (C) I know... We did it...")
while choice != "a" or choice != "A" or choice != "b" or choice != "B" or choice != "C" or choice != "c":
    if choice == "a" or choice == "A":
        messagebox.showinfo("" + name2 + "", "It was hard, but it was worthit"
                            ". " + name + "... Thank you so much! My dream is"
                            " complete!")
        os.startfile('endgame2.mp3')
        break
    elif choice == "b" or choice == "B":
        messagebox.showinfo("" + name2 + "",
                            "Ha! Don't be playing jokes with me! But I can't"
                            " believe this all happened in one day and it's"
                            " the day I met you! Thank you... " + name + ".")
        os.startfile('endgame2.mp3')
        break
    elif choice == "C" or choice == "c":
        messagebox.showinfo("" + name2 + "", "Unbelieveable, right? But we did"
                            " it, even with just one day. You really are a gre"
                            "at warrior. And a great friend. Thanks " + name + ""
                            "!")
        os.startfile('endgame2.mp3')
        break
    else:
        choice = simpledialog.askstring("" + name + "",
                                "\n (A) Haha, yeah we sure did..." + \
                                "\n (B) Are you sure we did?"
                                "\n (C) I know... We did it...")
        continue
messagebox.showinfo("" + name + "",
                    "That was my adventure. Of how me and " + name2 + ""
                    " saved the world. I will never forget that day. I"
                    " helped achieve his dream, and he made me realize"
                    " a new dream.")
messagebox.showinfo("" + name + "",
                    "...To keep the world safe from harm.")
messagebox.showinfo("Thank you!",
                    "Thank you for playing! Restart the program to play again"
                    " and get some different choices or be satisfied with sav"
                    "ing the world!")
root.destroy()
os._exit
                    
                            
                                    
 
                



