import random

def rollDice():
      number = random.randint(1,6)
      print(number)

while True:
      input('Press any key to roll the dice')
      rollDice()