# # Odd or even
# number = int(input("Which number do you want to check? "))
# number = int(number)
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")
#
#
# # BMI (body mass index)
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# w = float(weight)
# h = float(height)
#
# BMI = w/(h**2)
# BMI_int = round(BMI)
#
# if BMI_int < 18.5:
#     print(f"Your BMI is {BMI_int}, you are underweight")
# elif BMI_int < 25:
#     print(f"Your BMI is {BMI_int}, you have a normal weight")
# elif BMI_int < 30:
#     print(f"Your BMI is {BMI_int}, you are slightly overweight")
# elif BMI_int < 35:
#     print(f"Your BMI is {BMI_int}, you are obese")
# else:
#     print(f"Your BMI is {BMI_int}, you are clinically obese")
#
#
# # Leap year
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year.')
#         else:
#             print('Not leap year')
#     else:
#         print('Leap year.')
# else:
#     print('Not leap year.')
#
#
# # Python pizza
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# price = 0
# if size == "L":
#     price += 25
# elif size == "M":
#     price += 20
# elif size == "S":
#     price += 15
#
# if add_pepperoni == "Y":
#     if size == "S":
#         price += 2
#     else:
#         price += 3
#
# if extra_cheese == "Y":
#     price += 1
#
# print("Your final bill is: ${}.".format(price))
#
# 
# 
# # Love calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 
# o1 = o2 = 0
# for i in "true":
#     o = 0
#     for j in name1.lower():
#         if j == i:
#             o +=1
#     for j in name2.lower():
#         if j == i:
#             o +=1
#     o1 += o
# 
# for i in "love":
#     o = 0
#     for j in name1.lower():
#         if j == i:
#             o +=1
#     for j in name2.lower():
#         if j == i:
#             o +=1
#     o2 += o
# 
# 
# love_score = str(o1) + str(o2)
# love_score = int(love_score)
# 
# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score > 40 and love_score < 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")


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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

a = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
if a.lower() != 'left':
  print('Fall into a hole. Game Over.')
  exit()


b = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
if b.lower() != 'wait':
  print('Attacked by trout. Game Over.')
  exit()

c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

if c.lower() == 'red':
  print('Burnd by fire. Game Over')
  exit()  
elif c.lower() == 'blue':
  print('Eatten by beasts. Game Over.')
  exit()
elif c.lower() == 'yellow':
  print('You Win!')
else:
  print('Game Over.')
  exit()
    
    