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
game_images= [rock, paper, scissors]
#Write your code below this line 👇
print("Welcome to rock paper scissors game!")
player1 = int(input("type 0 for rock,1 for paper and 2 for scissors\n"))
if player1 >= 0 and player1 <=2:
  print(game_images[player1])
  print("Computer chose:")
  player2 = random.randint(0,2)
  print(game_images[player2])
  if player1 == 0 and player2 == 0:
    print("It's a Tie")
  elif player1 == 0 and player2 == 1:
   print("You lose")
  elif player1 == 0 and player2 == 2:
    print("You Win")
  elif player1 == 1 and player2 == 0:
   print("You win")
  elif player1 == 1 and player2 == 1:
   print("It's a Tie")
  elif player1 == 1 and player2 == 2:
    print("You lose")
  elif player1 == 2 and player2 == 0:
   print("You lose")
  elif player1 == 2 and player2 == 1:
    print("You Win")
  elif player1 == 2 and player2 == 2:
    print("It's a Tie")

else:
  print("Invalid Number, Try Again.")

