# Coin
# Remember to use the random module
# # Hint: Remember to import the random module here at the top of the file.
# import random
#
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#
# r = random.randint(0, 1)
#
# if r == 1:
#     print("Heads")
# elif r == 0:
#     print("Tails")
#
# 
# 
# # Banker Roulette
# # You can use random.choice(names) to do it in one line.
# import random 
# 
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# 
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 
# n = random.randint(0,len(names)-1)
# print(f"{names[n]} is going to buy the meal today!")
# 
# # Treasure map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 
# map[int(position[1])-1][int(position[0])-1] = 'X'
# 
# print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissor
import random 

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

game_images = [rock, paper, scissors]   

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")