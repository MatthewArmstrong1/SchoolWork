MAX_NUM_OF_MARKS = 160

def CheckNumberValidity(stringNumber,range):
  if not stringNumber.isnumeric():
    print("Must be a number!")
    exit()
  elif int(stringNumber) > range:
    print(f"The number must be within a set range! (0-{str(range)}")
    exit()
  elif int(stringNumber) < 0:
    print("Number cannot be negative!")
    exit()

def GetUserPrelimResult():
  global PrelimResult
  PrelimResult = input("What did you score on your prelim (Out of 110)?\n")
  CheckNumberValidity(PrelimResult,110)
  PrelimResult = int(PrelimResult)

def GetUserAssignmentGrade():
  global AssignmentResult
  AssignmentResult = input("What did you score on your assignment (Out of 50)?\n")
  CheckNumberValidity(AssignmentResult,50)
  AssignmentResult = int(AssignmentResult)

def CalculateResult():
  Total = AssignmentResult + PrelimResult
  Percentage = round((Total/MAX_NUM_OF_MARKS) * 100)
  Mark = ""
  if Percentage >= 70:
    Mark = "A"
  elif Percentage >= 60 and Percentage <= 69:
    Mark = "B"
  elif Percentage >= 50 and Percentage <= 59:
    Mark = "C"
  else:
    Mark = "Fail"

  print(f"\n\nPrelim mark: {str(PrelimResult)}")
  print(f"Assignment mark: {str(AssignmentResult)}")
  print(f"Percentage: {str(Percentage)}")
  print(f"Grade: {Mark}")

GetUserPrelimResult()
GetUserAssignmentGrade()
CalculateResult()
