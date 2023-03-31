#import modules
from tkinter import *
import time
from random import randint

#Creating variables
hunger = 100
boredom = 0
cleanliness = 100
fatigue = 0
day = 0

#display function
def display():
    global hunger
    global day

#criteria for image change
    if hunger <= 60:
        char.config(image = ok)
    if hunger <= 30:
        char.config(image = ill)
    if hunger <= 10:
        char.config(image = low)
    if hunger >= 100:
        char.config(image = full)
#end of game
    if day == 50:
        print("You Win")
        exit()
    
    #Display text
    hungertxt.config(text="Hunger: " + str(hunger))
    boredomtxt.config(text="Boredom: " + str(boredom))
    cleanlinesstxt.config(text="Cleanliness: " + str(cleanliness))
    fatiguetxt.config(text="Fatigue: " + str(fatigue))
    daytxt.config(text="Day: " + str(day))

#refreshes display every 100ms
    char.after(100, display)
    
#Incr /Decr variables
def hungerLoss():
    global hunger
    hunger = hunger -1
#if player is still alive keep updating
    if death():
        hungertxt.after(5000, hungerLoss)
#if hunger goes above 100 reset it to 100
    if hunger >100:
        hunger =100
    
def days():
    global day
    day = day + 1
    if death():
        daytxt.after(10000, days)

def cleanLoss():
    global cleanliness
    global hunger
    cleanliness = cleanliness -1
    if death():
        cleanlinesstxt.after(3000, cleanLoss)
#if cleanliness reaches 0 hunger is set to 15
    if cleanliness == 0:
        hunger = 15
    if cleanliness > 100:
        cleanliness = 100

def fatigueInc():
    global fatigue
    global hunger
    fatigue = fatigue + 1
    if death():
        fatiguetxt.after(7000, fatigueInc)
    if fatigue == 100:
        hunger = 15
    if fatigue < 0:
        fatigue = 0

def bored():
    global boredom
    global hunger
    boredom = boredom +5
    if death():
        boredomtxt.after(5000, bored)
    if boredom == 100:
        hunger = 15
    if boredom < 0:
        boredom = 0

#Allows the character to live and die
def death():
    global hunger
    if hunger <= 0:
        print("Gameover")
        exit()
        return False
    else:
        return True

#Button Functions
#Hunger increases when button is pressed
def type1():
    global hunger
    if hunger <100:
        hunger = hunger +20
        
#Mini game which  decreases characters boredom
def type2():
    global boredom
    char1 = randint(1,3)
    guess = input("Choose a number between 1 and 3: ")
    guess = int(guess)
    if guess == char1:
        print("Correct")
        boredom = 0
    else:
        print("Incorrect")
        boredom = boredom -20

#When clicked cleanliness increases        
def type3():
    global cleanliness
    if cleanliness < 100:
        cleanliness = cleanliness + 10

#when clicked fatigue decreases
def type4():
    global fatigue
    if fatigue > 0:
        time.sleep(2)
        fatigue = 0
        
#Creating Tkinter window
window = Tk()
window.title("Tamagotchi Game")

#Images
full = PhotoImage(file="green.png")
ok = PhotoImage(file="blue.png")
ill = PhotoImage(file="orange.png")
low = PhotoImage(file="red.png")
sleep = PhotoImage(file="sleep.png")
win = PhotoImage(file="win.png")

#Label attributes (text, font and font size)
hungertxt = Label(window, text="Hunger: " + str(hunger), font = ('Cambria', 16))
hungertxt.pack()

boredomtxt = Label(window, text="Boredom: " + str(boredom), font = ('Cambria', 16))
boredomtxt.pack()

cleanlinesstxt = Label(window, text="Cleanliness: " + str(cleanliness), font = ('Cambria', 16))
cleanlinesstxt.pack()

fatiguetxt = Label(window, text="Fatigue: " + str(fatigue), font = ('Cambria', 16))
fatiguetxt.pack()

daytxt = Label(window, text="Day: " + str(day), font = ('Cambria', 16))
daytxt.pack()

char = Label(window, image = full)
char.pack()

#Button creation attributes (text, font, font size and width)
button1= Button(window, text= "Feed",font =('Cambria', 14), width = 30, command=type1)
button1.pack()

button2= Button(window, text = "Play",font =('Cambria', 14), width = 30, command=type2)
button2.pack()

button3= Button(window, text= "Clean",font =('Cambria', 14), width = 30, command=type3)
button3.pack()

button4= Button(window, text = "Sleep",font =('Cambria', 14), width = 30, command=type4)
button4.pack()


#Run functions
display()
hungerLoss()
cleanLoss()
fatigueInc()
bored()
days()
window.mainloop()

