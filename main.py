import random
from fileinput import close

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

game_elements=[rock,paper,scissors]
computer_choice=random.randint(0,2)
human_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:"))
if human_choice >= 3 or human_choice < 0:
    print("You typed an invalid number. You lose!")
elif human_choice==0 and computer_choice==1:
    print("Computer wins!")
elif human_choice==0 and computer_choice==2:
    print("You win!")
elif human_choice==1 and computer_choice==0:
    print("You win!")
elif human_choice==1 and computer_choice==2:
    print("Computer wins!")
elif human_choice==2 and computer_choice==0:
    print("Computer wins!")
elif human_choice==1 and computer_choice==2:
    print("You win!")
elif human_choice==computer_choice:
    print("Tie")

print(game_elements[human_choice])
print(game_elements[computer_choice])

