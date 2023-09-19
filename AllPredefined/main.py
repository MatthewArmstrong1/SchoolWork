import random

def isfloat(str):
    try: 
        float(str)
    except ValueError:
        return False
    
    if str.find(".") == -1:
        return False
    return True

def NameFunction():
    Name = input("What is your name?\n")
    print(f'Your name is {len(Name)} characters long!')

def DecimalPlaces():
    Number = input("Enter a number to be rounded to 1,2 and 3 D.P\n")
    if not isfloat(Number):
        print("Your number must be a real number!")
        exit()
    print(f'Rounded to 1 decimal place: {round(float(Number),1)}')
    print(f'Rounded to 2 decimal places: {round(float(Number),2)}')
    print(f'Rounded to 3 decimal place: {round(float(Number),3)}')
    
def RandomNumberGenerator():
    Number = input("Enter the upper range for the random number (Must be an int):\n")
    if isfloat(Number):
        print("Number cannot be a float")
        exit()
    Number = int(Number)
    print(f'Your random number is: {random.randint(1,Number)}')
    
def NumberInRange():
    print(f'The random number is: {random.randint(50,100)}')
    

print("Which program would you like to use?\n")
print("A: Name length checker")
print("B: 3 Decimal Place checker")
print("C: Random Number Generator")
print("D: Random Number Between 50 and 100\n")

Choice = input("Which one?\n")
if Choice == "A":
    NameFunction()
elif Choice == "B":
    DecimalPlaces()
elif Choice == "C":
    RandomNumberGenerator()
elif Choice == "D":
    NumberInRange()
else:
    print("Choice must be valid!")


