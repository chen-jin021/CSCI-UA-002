#Truthiness
a = 5
b = 10

if a < b:
    print("1")

if b > a:
    print("2")

if b: # a and b are integers
      # and any integers are considered true if they are positive or negative
      # therefore they are true
    print("3")

if a:
    print("4")

    
#Any string with length 1 or greater is true
if "apple":
    print("x")
if "":
    print("y")

a = 5
b = 10
c = 20
d = 30

if a < b and c <d:
    print("Yes")


#Guppies temp
temp = int(input("Enter a temp in f: "))

#Is the temp too cold - 72 or less
if temp > 72:
    print("Too cold")

if temp > 86:
    print("Too hot!")

if temp >= 72 and temp <= 86:
    print("Just right")


#import random for the secret number
import random

#Guess a number:
guess = int(input("Enter your guess number: " ))

secret = random.randint(1,10)

#see if you got it correct
if guess == secret:
    print("Correct!")
    
else:
    # too low
    if guess < secret:
        print("Too Low!")
        

    # too high
    else:
        print("Too High!")

    print("The number was: ",secret)
#press command+[ or command+] to move around


x=10
y=5

if x < y:
    print("A")
else:
    print("B")
    if y*2 == 10:
        print("C")
    else:
        print("D")



#Overtime calculator
rate = float(input("Your hourly rate: "))

#ask for the number of hours worked
hours = float(input("How many hours you worked: "))

#they worked 40 hours or less
if hours <= 40:
    pay = hours * rate
    print("Your pay is: ",pay)

else:
    pay = (40-hours) * (rate * 1.5) + 40*rate
    print("Your pay is: ",pay)



#Grade calculator
#ask for grade as an integer
grade = int(input("Enter your score: "))

# >100      bad
# <100      bad

#90-100     A
#80-90      B
#70-80      C
#0-70       F
if grade<100 or grade>100:
    print("Not valid")
#if that is not true, then the grade is valid
else:
    #we are guarenteed that number
    #is in the range 0 - 100
    if grade >= 90:
        print("A")
    else:
        if grade >= 80:
            print("B")
        else:
            if grade >= 70:
                print("C")
            else:
                print("F")
        


#How about elif statement
x = 5

if x == 1:
    print("1")
elif x == 2:
    print("2")
elif x==5:
    print("5")
elif x==10 -5:
    print("5 again!")
else:
    print("?")


#rewrite the grade program
#Use the pervious questions etc.
if grade < 0 or grade >100:
    print("Not valid")
elif grade >=90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
