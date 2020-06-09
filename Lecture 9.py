#compare the length of two strings
print(len("applesause")>len("apple"))

#see if they can log into our program
password = input("Enter a password: ")

#convert the password to all lowercase
password = str.lower(password)
#On the oppsite hand,str.upper(password))

if password == "abc123":
    print("Welcome")
else:
    print("Invalid")

#while loops
num1 = int(input("Enter a number:"))
while num1 <= 0:
    print("Try again")
    num1 = int(input("Enter a number:"))


#secret number:
import random

guesses = 0

secret = int(input("Enter a number: "))

while True:
    
    guess = random.randint(1,100000)
    guesses += 1
    if guess == secret:
        print("found it on try #",guesses)
        break
