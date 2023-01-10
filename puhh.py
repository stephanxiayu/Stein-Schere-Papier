rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("Stein, Papier, Schere gegen den Computer....")
print("Deine Wahl: ")
wahl=input("Wähle: Stein = 0, Papier = 1, Schere = 2  ")
zahl=int(wahl)
print("Deine Wahl: ")
if zahl==0:
    print(rock)
elif zahl==1:
    print(paper)    
elif zahl==2:
    print(scissors)   
else: 
    print("alter, bist du dämlich?!")     


Computer=[rock,paper,scissors, ]


Computer=random.choice(Computer) 
print("wahl des Computers:")
print(Computer)
     

if str(zahl)==str(0) and Computer==scissors:
    print("Du hast gegen den Computer gewonnen! Juhu")
elif str(zahl)==str(1) and Computer==rock:  
    print("Du hast gegen den Computer gewonnen! Juhu")
elif str(zahl)==str(2) and Computer==paper: 
    print("Du hast gegen den Computer gewonnen! Juhu")
elif str(zahl)==str(2) and Computer==rock: 
    print("Der Computer hat gewonnen! buhhhhh")    
elif str(zahl)==str(1) and Computer==scissors: 
    print("Der Computer hat gewonnen! buhhhhh")     
elif str(zahl)==str(0) and Computer==paper: 
    print("Der Computer hat gewonnen! buhhhhh")        
else:    
    print("unendschieden, versuch es nochmal")    



