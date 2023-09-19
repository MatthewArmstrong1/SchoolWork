Number = input("Enter a 'real' number (One with decimal places):\n")

def isfloat(str):
    try: 
        float(str)
    except ValueError:
        return False
    
    if str.find(".") == -1:
        return False
    return True

if not isfloat(Number):
    print("Your number was not a real number!")
    exit()
    
def checkNumberLength(str):
    return len(str)

def roundNumber(intValue):
    return round(float(intValue))

def lengthOfRoundedNum(intValue):
    rounded = round(float(intValue))
    return len(str(rounded))

print(f'The length of the number is: {checkNumberLength(Number)}')
print(f'The rounded number is: {roundNumber(Number)}')
print(f'The length of the rounded number is: {lengthOfRoundedNum(Number)}')
