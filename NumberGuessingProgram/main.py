SET_NUMBER = 46

def GetUserNumber():
  global GuessedNumber
  GuessedNumber = input("Guess the number!\n")
  if not GuessedNumber.isnumeric():
    print("Your guess must be a valid, whole number")
    exit()
  GuessedNumber = int(GuessedNumber)

def Result():
  global GuessedNumber
  if GuessedNumber < SET_NUMBER:
    print("Your guess is too low! Try again")
  elif GuessedNumber > SET_NUMBER:
    print("Your guess is too high! Try again")
  else:
    print("Your guess is correct!")

GetUserNumber()
Result()
