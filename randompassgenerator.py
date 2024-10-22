import string
import random



password_length = int(input("How long would you like your password to be? "))

num = input("do you want to include numbers?(y/n)")
letters = input("do you want to include letters?(y/n)")
symbols = input("do you want to include symbols?(y/n)")

char=""
if num.lower() == "y":
    char+=string.digits
if letters.lower() == "y":
    char+=string.ascii_letters
if symbols.lower() == "y":
    char+=string.punctuation

password=""
for x in range(password_length):
   password+=random.choice(char)

print("your password is: " + password)