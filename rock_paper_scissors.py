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
choices_list = [rock, paper, scissors]
length = len(choices_list)
rand_num = random.randint(0, (length-1))
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
num = int(input())
print("your choice is:"+choices_list[num])
print("computer choice is:"+choices_list[rand_num])
if num == 0 and rand_num == 1:
    print("you lose the game")
elif num == 0 and rand_num == 2:
    print("you won the game")
elif num == 1 and rand_num == 0:
    print("you won the game")
elif num == 1 and rand_num == 2:
    print("you lose the game")
elif num == 2 and rand_num == 0:
    print("you lose the game")
elif num == 2 and rand_num == 1:
    print("you won the game")
else:
    print("Match Draw")
