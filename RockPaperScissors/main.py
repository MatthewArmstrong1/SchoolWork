import random

computerNumber = random.randint(0,2)
choices = ["Rock","Paper","Scissors"]

def GameLogic():
    print("What choice are you making?")
    print("\n1 = Rock\n2 = Paper\n3= Scissors")
    NewInput = input("\n\nWhat choice are you going to make?\n")
    if not NewInput.isnumeric():
        print("Your input was not a valid choice")
    elif int(NewInput) < 0 and int(NewInput) > 3:
        print("Your input was not a valid choice")
    
    NewInput = int(NewInput) - 1
    
    print("------")
    print(f"You chose {choices[NewInput]}; the computer chose {choices[computerNumber]}")
    if computerNumber == 0 and NewInput == 1:
        Win()
    elif NewInput == 0 and computerNumber == 1:
        Lose()
    elif NewInput == 2 and computerNumber == 1:
        Win()
    elif NewInput == 0 and computerNumber == 2:
        Win()
    elif NewInput == 2 and computerNumber == 0:
        Lose()
    else:
        print("You draw!")
      
def Win():
    print("You win!")

def Lose():
    print("You loose!")
    
GameLogic()
