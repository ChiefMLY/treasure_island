print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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


#This prompts the user to make their first move
move_1 = input("You're at a Crossroad \nWould you like to go 'Left' or 'Right': \n")
#A fail safe ot ensure only the right command is entered
if move_1.lower() not in ['left','right']:
  print('You entered the wrong command, try again')
else:
#Game continues if user goes left
  if move_1.lower() == 'left':
#This prompts the user to make their second move
    move_2 = input("There is a river in front of you would you like to 'Swim' or 'Wait' for a boat \n")
#Game Continues if user wait for a boat
    if move_2.lower() == 'wait':
#This prompts the user to make their third move
      move_3 = input("Congratulations you have made it to the next stage \nThere are three doors in front of you 'Red','Blue' and 'Yellow' \nWhich one would you like to open? \n")
#User gets burnt by Hot Larva if they open the red door
      if move_3.lower() == 'red':
        print('Wrong Door \n You just got burnt by Hot Larva \nGAME OVER')
#User gets eaten by wild beasts if they open the blue door
      elif move_3.lower() == 'blue':
        print('Wrong Door \n You just got eaten by wild beasts \nGAME OVER')
#User Wins the game if they open the yellow door
      elif move_3.lower() == 'yellow':
        print("Congratulations !!! \nYOU WIN !!!")
#User gets eaten by shark if they decide to Swim
    else:
      print('You just got eaten by a Shark \nGAME OVER')
#User falls in a hole if they go Right
  else:
    print('You fell into a hole \nGAME OVER')
