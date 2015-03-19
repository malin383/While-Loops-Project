# Simulator by Niraj Mali
#credits
'Music:'
'Fire Emblem Awakeing: Music 62'
'Youtube, Jojikiba: Walking on grass (sound effect)'
'MGQ Battle Sequence'
'Pokemon: Aquacorde Town'

    

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
    if exp > 15:
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
    if pexp > 18:
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
        attack += 18
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
                patk += 17
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
# Enemy Stats, copy paste for each enemy to change stats, maybe weapons
ehp = 20
eatk = 10
edef = 10
esp = 10
espd = 10
eweap = 5
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
        padamt = ((eweap + eatk)) - (pdef) + add
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
    hp
    while ehp > 0:
        if hp <= 0:
            os.startfile('death.mp3')
            messagebox.showinfo("" + name2 + "", "Stay with me! No, you can't!"
                            " Don't-")
            messagebox.showinfo(". . .", "" + name + " took too much "
                                "damage and failed to complete his journey."
                                " Thus, ended " + name + " and " + name2 + "'s journey.")
            messagebox.showinfo("You Lost", "You lost")
            root.destroy()
            os._exit
            break
            
            
        else:
            battle = simpledialog.askstring("\nBattle", "HP: " + str(hp) + "" + \
                                            "\nPartner HP: " + str(php) + ""
                                            "\n" + ename + ": " + str(ehp) + ""
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
                        victim
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
    if exp > 15:
        exp -= 15
        lvl += 1
        messagebox.showinfo("Level Up!", "" + name + " has reached level " + str(lvl) + "."
                            " All stats were upped by 4!")
        speed += 4
        attack += 4
        defense += 4
        hp +=5
    else:
        pass
    pexp += eexp
    messagebox.showinfo("Battle", "" + name2 + " gained " + str(eexp) + " experience points.")
    if pexp > 17:
        pexp - 17
        plvl += 1
        messagebox.showinfo("Level Up!", "" + name2 + " has reached level " + str(lvl) + "."
                            "All stats were upped by 4!")
        pspd += 4
        patk += 4
        pdef += 4
        php += 5
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
                                  "how these work? (y/n)")
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
                    "runs out of health. Also, after each battle experience"
                    " points are gained.")
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
        eexp = 1

        messagebox.showinfo("" + name2 + "", "Alright, I'll leave you too it."
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
        messagebox.showinfo("" + name2 + "", "What was that?")
        choice
messagebox.showinfo("" + name2 + "", "Alright, to town it is. Let's make sure"
                    " you get taken care of.")

                



