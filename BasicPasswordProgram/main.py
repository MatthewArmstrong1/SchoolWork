USERNAME = "Admin1"
PASSWORD = "Password"

Inputted_Username = input("What is the username?\n")
Inputted_Password = input("What is the password?\n")

if Inputted_Username == USERNAME and Inputted_Password == PASSWORD:
  print("Access granted!")
else:
  print("Access denied")
