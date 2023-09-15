import random

def RollDice():
  global Dice1
  global Dice2
  Dice1 = random.randint(1,6)
  Dice2 = random.randint(1,6)

def CheckNumbers():
  Win = False
  if Dice1 == Dice2:
    Win = True

  print(f"\n\nDice 1 is: {str(Dice1)}")
  print(f"Dice 2 is: {str(Dice2)}")
  if Win == True:
    print("You win!")
  else:
    print("You don't win!")

RollDice()
CheckNumbers()
