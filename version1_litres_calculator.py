DISCOUNT_CODE = "luckyday"


def CalculateRate(rate):
  LitresForCalc = int(LitresRequired)
  return round(LitresForCalc * rate, 2)


def AskForDiscount():
  global DiscountCode
  DiscountCode = input("What is your discount code?\n")


def AskForLitres():
  global LitresRequired
  LitresRequired = input("How many litres do you need?\n")
  if not LitresRequired.isnumeric():
    print("Litres must be a number")
    exit()


AskForLitres()
AskForDiscount()
if DiscountCode == DISCOUNT_CODE:
  print(f"For {LitresRequired} litres you will pay £{str(CalculateRate(1))}")
else:
  print(
      f"For {LitresRequired} litres you will pay £{str(CalculateRate(1.15))}")
