#Import Modules
from tkinter import *
import time
import os

#Define Piano Keys -Bass
#F1 - B1
def playF():
    print("F1")
    canvas.coords(notepic, 190,339)
    canvas.coords(shpNotepic, -15,-15)
    
def playFSharp():
    print("F#1")
    canvas.coords(shpNotepic, 190,339)
    canvas.coords(notepic, -15,-15)
    
def playG():
    print("G1")
    canvas.coords(notepic, 210,327)
    canvas.coords(shpNotepic, -15,-15)

def playGSharp():
    print("G#1")
    canvas.coords(shpNotepic, 210, 327)
    canvas.coords(notepic, -15,-15)
    
def playA():
    print("A1")
    canvas.coords(notepic, 230, 316)
    canvas.coords(shpNotepic, -15,-15)
    
def playASharp():
    print("A#1")
    canvas.coords(shpNotepic, 230, 316)
    canvas.coords(notepic, -15,-15)
    
def playB():
    print("B1")
    canvas.coords(notepic, 250, 304)
    canvas.coords(shpNotepic, -15,-15)

#C2 - B2
def playC2():
    print("C2")
    canvas.coords(notepic, 270, 292)
    canvas.coords(shpNotepic, -15,-15)

def playCSharp2():
    print("C#2")
    canvas.coords(shpNotepic, 270, 292)
    canvas.coords(notepic, -15,-15)

def playD2():
    print("D2")
    canvas.coords(notepic, 290, 280)
    canvas.coords(shpNotepic, -15,-15)
    
def playDSharp2():
    print("D#2")
    canvas.coords(shpNotepic, 290, 280)
    canvas.coords(notepic, -15,-15)
    
def playE2():
    print("E2")
    canvas.coords(notepic, 310, 268)
    canvas.coords(shpNotepic, -15,-15)
    
def playF2():
    print("F2")
    canvas.coords(notepic, 330, 257)
    canvas.coords(shpNotepic, -15,-15)
    
def playFSharp2():
    print("F#2")
    canvas.coords(shpNotepic, 330, 257)
    canvas.coords(notepic, -15,-15)
    
def playG2():
    print("G2")
    canvas.coords(notepic, 350, 246)
    canvas.coords(shpNotepic, -15,-15)
    
def playGSharp2():
    print("G#2")
    canvas.coords(shpNotepic, 350, 246)
    canvas.coords(notepic, -15,-15)
    
def playA2():
    print("A2")
    canvas.coords(notepic, 370, 235)
    canvas.coords(shpNotepic, -15,-15)
    
def playASharp2():
    print("A#2")
    canvas.coords(shpNotepic, 370, 235)
    canvas.coords(notepic, -15,-15)
    
def playB2():
    print("B2")
    canvas.coords(notepic, 390, 223)
    canvas.coords(shpNotepic, -15,-15)
    
#Define Piano Keys - Treble Clef
#C3 - B3
def playC3():
    print("C3")
    canvas.coords(notepic, 410, 195)
    canvas.coords(shpNotepic, -15,-15)

def playCSharp3():
    print("C#3")
    canvas.coords(shpNotepic, 410, 195)
    canvas.coords(notepic, -15,-15)

def playD3():
    print("D3")
    canvas.coords(notepic, 430, 168)
    canvas.coords(shpNotepic, -15,-15)
    
def playDSharp3():
    print("D#3")
    canvas.coords(shpNotepic, 430, 168)
    canvas.coords(notepic, -15,-15)

def playE3():
    print("E3")
    canvas.coords(notepic, 470,156)
    canvas.coords(shpNotepic, -15,-15)

def playF3():
    print("F3")
    canvas.coords(notepic, 490,145)
    canvas.coords(shpNotepic, -15,-15)

def playFSharp3():
    print("F#3")
    canvas.coords(shpNotepic, 490,145)
    canvas.coords(notepic, -15,-15)

def playG3():
    print("G3")
    canvas.coords(notepic, 510,133)
    canvas.coords(shpNotepic, -15,-15)
  
def playGSharp3():
    print("G#3")
    canvas.coords(shpNotepic, 510,133)
    canvas.coords(notepic, -15,-15)

def playA3():
    print("A3")
    canvas.coords(notepic, 530,122)
    canvas.coords(shpNotepic, -15,-15)
    
def playASharp3():
    print("A#3")
    canvas.coords(shpNotepic, 530,122)
    canvas.coords(notepic, -15,-15)

def playB3():
    print("B3")
    canvas.coords(notepic, 550,111)
    canvas.coords(shpNotepic, -15,-15)

#C4 -F4
def playC4():
    print("C4")
    canvas.coords(notepic, 570,98)
    canvas.coords(shpNotepic, -15,-15)

def playCSharp4():
    print("C#4")
    canvas.coords(shpNotepic, 570,98)
    canvas.coords(notepic, -15,-15)

def playD4():
    print("D4")
    canvas.coords(notepic, 590,87)
    canvas.coords(shpNotepic, -15,-15)

def playDSharp4():
    print("D#4")
    canvas.coords(shpNotepic, 590,87)
    canvas.coords(notepic, -15,-15)
    
def playE4():
    print("E4")
    canvas.coords(notepic, 610,76)
    canvas.coords(shpNotepic, -15,-15)

def playF4():
    print("F4")
    canvas.coords(notepic, 630,65)
    canvas.coords(shpNotepic, -15,-15)
    
#Creation of Tkinter window
window = Tk()
window.title("Piano App")
window.config(bg = "white")

#Buttons

#Image
stave = PhotoImage(file="Images/grand-staff.gif")
note = PhotoImage(file="Images/semi-breve.gif")
shpNote  = PhotoImage(file="Images/semi-breveShp.gif")

#Canvas
canvas= Canvas(window, bg="white", width=1200, height=400)
canvas.create_image(100,100)
stavepic = canvas.create_image(600,200, image= stave) 
notepic = canvas.create_image(600,200, image= note)
shpNotepic = canvas.create_image(600,200, image= shpNote)
canvas.lower(stavepic)
canvas.tag_raise(notepic)
canvas.grid(row = 0, column = 0, columnspan=23)

#Start position for notes
canvas.coords(shpNotepic, -15,-15)
canvas.coords(notepic, -15,-15)

#Piano key creation - Bass Clef
#F1 - B1
FKey = Button(window, text= "F", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playF)
FKey.grid(row = 3,column = 3, columnspan = 1) 

FSharpKey = Button(window, text= "F#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playFSharp)
FSharpKey.grid(row = 2, column = 3, columnspan = 2)

GKey = Button(window, text= "G", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playG)
GKey.grid(row = 3,column = 4, columnspan = 1)

GSharpKey = Button(window, text= "G#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playGSharp)
GSharpKey.grid(row = 2, column = 4, columnspan = 2)

AKey = Button(window, text= "A", font =('Arial', 14), width = 5, height = 10 ,bg ="white", command = playA)
AKey.grid(row = 3,column = 5, columnspan = 1)

ASharpKey = Button(window, text= "A#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playASharp)
ASharpKey.grid(row = 2, column = 5, columnspan = 2)

BKey = Button(window, text= "B", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playB)
BKey.grid(row = 3,column = 6, columnspan = 1)

#C2 - B2
C2Key = Button(window, text= "C", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playC2)
C2Key.grid(row = 3,column = 7, columnspan = 1)

C2SharpKey = Button(window, text= "C#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg="black", command = playCSharp2)
C2SharpKey.grid(row = 2, column = 7, columnspan = 2)

D2Key = Button(window, text = "D",font =('Arial', 14), width = 5, height = 10, bg ="white", command = playD2)
D2Key.grid(row = 3,column = 8, columnspan = 1)

D2SharpKey = Button(window, text= "D#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg="black", command = playDSharp2)
D2SharpKey.grid(row = 2, column = 8, columnspan = 2)

E2Key = Button(window, text= "E", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playE2)
E2Key.grid(row = 3,column = 9, columnspan = 1)

F2Key = Button(window, text= "F", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playF2)
F2Key.grid(row = 3,column = 10, columnspan = 1) 

F2SharpKey = Button(window, text= "F#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playFSharp2)
F2SharpKey.grid(row = 2, column = 10, columnspan = 2)

G2Key = Button(window, text= "G", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playG2)
G2Key.grid(row = 3,column = 11, columnspan = 1)

G2SharpKey = Button(window, text= "G#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playGSharp2)
G2SharpKey.grid(row = 2, column = 11, columnspan = 2)

A2Key = Button(window, text= "A", font =('Arial', 14), width = 5, height = 10 ,bg ="white", command = playA2)
A2Key.grid(row = 3,column = 12, columnspan = 1)

A2SharpKey = Button(window, text= "A#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playASharp2)
A2SharpKey.grid(row = 2, column = 12, columnspan = 2)

B2Key = Button(window, text= "B", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playB2)
B2Key.grid(row = 3,column = 13, columnspan = 1)

#Piano key creation -Treble Clef
#C3 - B3
CKey = Button(window, text= "C", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playC3)
CKey.grid(row = 3,column = 14, columnspan = 1)

CSharpKey = Button(window, text= "C#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg="black", command = playCSharp3)
CSharpKey.grid(row = 2, column = 14, columnspan = 2)

DKey = Button(window, text = "D",font =('Arial', 14), width = 5, height = 10, bg ="white", command = playD3)
DKey.grid(row = 3,column = 15, columnspan = 1)

DSharpKey = Button(window, text= "D#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg="black", command = playDSharp3)
DSharpKey.grid(row = 2, column = 15, columnspan = 2)

EKey = Button(window, text= "E", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playE3)
EKey.grid(row = 3,column = 16, columnspan = 1)

FKey = Button(window, text= "F", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playF3)
FKey.grid(row = 3,column = 17, columnspan = 1) 

FSharpKey = Button(window, text= "F#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playFSharp3)
FSharpKey.grid(row = 2, column = 17, columnspan = 2)

GKey = Button(window, text= "G", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playG3)
GKey.grid(row = 3,column = 18, columnspan = 1)

GSharpKey = Button(window, text= "G#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playGSharp3)
GSharpKey.grid(row = 2, column = 18, columnspan = 2)

AKey = Button(window, text= "A", font =('Arial', 14), width = 5, height = 10 ,bg ="white", command = playA3)
AKey.grid(row = 3,column = 19, columnspan = 1)

ASharpKey = Button(window, text= "A#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg = "black", command = playASharp3)
ASharpKey.grid(row = 2, column = 19, columnspan = 2)

BKey = Button(window, text= "B", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playB3)
BKey.grid(row = 3,column = 20, columnspan = 1)

#C4 - F4
CKey = Button(window, text= "C", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playC4)
CKey.grid(row = 3,column = 21, columnspan = 1)

CSharpKey = Button(window, text= "C#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg="black", command = playCSharp4)
CSharpKey.grid(row = 2, column = 21, columnspan = 2)

DKey = Button(window, text = "D",font =('Arial', 14), width = 5, height = 10, bg ="white", command = playD4)
DKey.grid(row = 3,column = 22, columnspan = 1)

DSharpKey = Button(window, text= "D#", font =('Arial', 14), width = 5, height = 5, fg = "white", bg="black", command = playDSharp4)
DSharpKey.grid(row = 2, column = 22, columnspan = 2)

EKey = Button(window, text= "E", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playE4)
EKey.grid(row = 3,column = 23, columnspan = 1)

FKey = Button(window, text= "F", font =('Arial', 14), width = 5, height = 10, bg ="white", command = playF4)
FKey.grid(row = 3,column = 24, columnspan = 1) 


window.mainloop()
