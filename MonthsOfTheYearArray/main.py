def checkNumber(userNum,lower,upper):
    if not userNum.isnumeric():
        exit("Input not numeric")
    elif int(userNum) > upper or int(userNum) < lower:
        exit("Number must be within range")

monthsOfTheYear = ["January","February","March","April","May","June","July","August","September","October","November","December"]
userMonth = input("Enter a number between 1 and 12\n")
checkNumber(userMonth,1,12)
print(f"Result: {monthsOfTheYear[int(userMonth) - 1]}")
