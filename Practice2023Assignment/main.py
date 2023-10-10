# mileage at start, number of charging stations visited, valid kilowatt rating (7,22,50), mileage at each station

# rates: 7kw for £0, 22kw for £0.005, 50kw for £0.01 all for miles

def CheckInt(string):
  if not string.isnumeric():
    exit("Input must be numeric")

milesAtStations = []
ratingsAtStations = []
chargesPerLeg = []
totalCharge = 0
mileage = input("What was the vehicle's mileage at the start of the journey?\n")
CheckInt(mileage)

amountOfStations = input("How many charging stations did you visit on the journey?\n")
CheckInt(amountOfStations)

for i in range(int(amountOfStations)):
  mileageAtNextStation = input(f"What was the vehicle's mileage at station number {i+1}?\n")
  CheckInt(mileageAtNextStation)
  if int(mileageAtNextStation) <= 0:
    exit("Mileage cannot be zero")
  elif i != 0 and int(milesAtStations[i-1]) >= int(mileageAtNextStation):
    exit("Mileage cannot be the same or less than the previous station's mileage")
  elif int(mileageAtNextStation) <= int(mileage):
    exit("Mileage at this station cannot be less than or equal to the starting mileage")
  milesAtStations.append(mileageAtNextStation)
  ratingOfStation = input(f"What was the rating of the station number {i+1}? (7, 22 or 50)\n")
  if int(ratingOfStation) != 7 and int(ratingOfStation) != 22 and int(ratingOfStation) != 50:
    exit("Rating must be 7, 22 or 50")
  ratingsAtStations.append(ratingOfStation)
    

for i in range(len(milesAtStations)):
  if i != 0:
    milesSinceLastStation = int(milesAtStations[i]) - int(milesAtStations[i-1])
  else:
    milesSinceLastStation = int(milesAtStations[i]) - int(mileage)
  if int(ratingsAtStations[i]) == 7:
    chargeForLeg = 0
  elif int(ratingsAtStations[i]) == 22:
    chargeForLeg = 0.005 * milesSinceLastStation
  else:
    chargeForLeg = 0.01 * milesSinceLastStation
  chargesPerLeg.append(chargeForLeg)

print("--------\n")

for i in range(len(chargesPerLeg)):
  print(f"The charge for leg {i+1} is £{chargesPerLeg[i]}")
  totalCharge = totalCharge + chargesPerLeg[i]

print(f"The total charge is £{round(totalCharge,2)}")
print(f"Total mileage is: {int(milesAtStations[len(milesAtStations) - 1]) - int(mileage)} miles")
