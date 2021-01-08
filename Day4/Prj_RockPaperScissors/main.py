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

#GUI STUFF
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Not a valid choice. You lose!")
    exit()

options = [rock, paper, scissors]

comp_choice = random.randint(0,2)

print("Computer chose:\n"+options[comp_choice])

#rule logic
if player_choice == comp_choice:
    print("It's a draw")
elif player_choice == 0 and comp_choice == 1:
    print("You lose")
elif player_choice == 0 and comp_choice == 2:
    print("You win")
elif player_choice == 1 and comp_choice == 0:
    print("You win")
elif player_choice == 1 and comp_choice == 2:
    print("You lose")
elif player_choice == 2 and comp_choice == 0:
    print("You lose")
elif player_choice == 2 and comp_choice == 1:
    print("You win")
elif player_choice > 2:
    print("You need to input a correct value")

# Facit

# print(options[player_choice])

# print("Computer chose:")
# print(options[comp_choice])



if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
elif player_choice == 0 and comp_choice == 2:
    print("You win")
elif player_choice==2 and comp_choice ==0:
    print("You lose")
elif player_choice < comp_choice:
    print("You lose")
elif player_choice > comp_choice:
    print("You win")
elif player_choice == comp_choice:
    print("It's a draw")