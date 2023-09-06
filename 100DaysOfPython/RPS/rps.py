import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''
choiceList = ["0", "1", "2"]
computerChoice = random.choice(choiceList)
player_input = input("type 0 for Rock, 1 for paper, 2 for scissors: ")
if player_input == "0":
    choice = rock
elif player_input == "1":
    choice = paper
elif player_input == "2":
    choice = scissors
else:
    choice =  "Sorry try again"
time.sleep(1.5)
print(f"You Chose {choice}")
print("*---------*")
time.sleep(1.5)
if computerChoice == "0":
    cChoice = rock
elif computerChoice == "1":
    cChoice = paper
elif computerChoice == "2":
    cChoice = scissors
print(f"computer chose {cChoice}")

game_conditions = {
    '0': {'2': 'YOU WIN', '1': 'YOU LOSE'},
    '1': {'0': 'YOU WIN', '2': 'YOU LOSE'},
    '2': {'1': 'YOU WIN', '0': 'YOU LOSE'}
}
result = game_conditions[player_input][computerChoice]
time.sleep(1.5)
print("-------------------------")
print(result)
#rock beats scissors
#paper beats rock
#scissors beats paper