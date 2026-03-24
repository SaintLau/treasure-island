# ASCII ART from ascii.co.uk/art
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input('You reach a crossroad. What turn will you make?\nType "left" or "right" ').lower()

if turn == "left":
   boat = input('You came across a lake. In the middle, you spot an island. You want to go there. '
          'Will you "wait" for a boat or "swim"? \n').lower()
   if boat == "wait":
       door = input('Congratulations, you reach the island.'
                    'At a distance, you spot an old house. You approach and enter the house.'
                    'You have three doors. You can only pick one. '
                    'Which do you pick? The "yellow", "red" or "blue" door \n').lower()
       if door == "red":
           print("The room is full of fire. Game over")
       elif door == "yellow":
           print("YOU FOUND THE TREASURE!")
       elif door == "blue":
               print("This room is haunting...game over")
       else:
           print("This door does not exist. Game over")
   else:
       print("You were eaten by a shark...game over")

else:
    print("You fell from a cliff...Game over")
