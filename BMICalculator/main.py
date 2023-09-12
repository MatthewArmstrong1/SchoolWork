from decimal import *
getcontext().prec = 2

# decimal library setup, python is weird :(

def GetWeight():
  global Weight
  Weight = input("What is your weight (In KG)?\n")
  if not float(Weight):
    print("Weight must be a number")
    exit()
  Weight = Decimal(Weight)

def GetHeight():
  global Height
  Height = input("What is your height (In metres)?\n")
  if not float(Height):
    print("Height must be a number")
    exit()
  Height = Decimal(Height)

def GetCategory(BMI):
  if BMI < 18.5:
    return "Underweight"
  elif BMI >= 18.5 and BMI < 25:
    return "Ideal weight"
  elif BMI >= 25:
    return "Overweight"
  return "Unable to calculate category; an error occured"

GetWeight()
GetHeight()
BMI = Weight / Decimal(pow(Height,Height))
print(f"BMI is {str(BMI)}\nThis is a {GetCategory(BMI)} BMI")
