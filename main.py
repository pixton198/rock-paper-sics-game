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
game=[rock , paper , scissors]
choice_user=int(input("what do you chose ? type 0 for rock,1 for paper,2 for scissors"))
if choice_user >= 3 and choice_user < 0:
    print("invalid oparation, you lose")
else:
    print(game[choice_user])
    com_choice=random.randint(0,2)
    print(game[com_choice])
    if choice_user == 0 and com_choice == 1:
        print("you lose !")
    elif com_choice == 1 and choice_user == 0:
        print("you win")
    elif com_choice == 1 and choice_user == 2:
        print("you win")
    elif com_choice == 2 and choice_user == 1:
        print("you lose")
    elif com_choice == 0 and choice_user == 2:
        print("you win")
    elif com_choice == 2 and choice_user == 0:
        print("you lose")
    elif com_choice == choice_user :
        print("it's draw")
