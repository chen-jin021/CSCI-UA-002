#Data types
# "=" is an assignment operator
# x=7+"1.0" this is ERROR
answer = input("Enter a value: ")
print(answer,type(answer))

n1 = input("Number 1: ")
n2 = input('Number 2: ')

#convert this into an integer
n1_int = int(n1)
n2_int = int(n2)

print(n1_int + n2_int)
#different from:
print(n1 + n2)

#简便convert的方法：nesting
x = int(input('Enter a number: ')) #注：there are two parentheses

#Programming Challenge
#ask the user for their name
name = input("Name: ")

#ask the user for 3 test scores
score1 = float(input ("Enter score 1: "))
#the user input mismatch the converting data type can crash the program
score2 = float(input ("Enter score 2: "))
score3 = float(input ("Enter score 3: "))

#compute sum of scores
total = score1 + score2 + score3

#compute average
average = total/3

#generate output
print("Your score in class is",average)


#Programming challenge -coin

#ask the user for the number of coins they have
#pennies
#nickels
#dimes
#quarters
pennies = int(input("Pennies: "))
nickels = int(input("Nickels: "))
dimes = int(input("Dimes: "))
quarters = int(input("Quarters: "))

#somehow convert these coins into currency
money = pennies*0.01 + nickels *0.05 + dimes*0.1 + quarters *0.25

#generate output
print('You have',money,'in your pocket!')

Weired Issue:
Pennies: 3
Nickels: 2
Dimes: 2
Quarters: 1
You have 0.5800000000000001 in your pocket

This is due to the "floating point inaccuracy"


#Errors:
#Syntax errors: didn't use your laguage right
#Runtime errors: laguage is fine, but the program crashed (usually, problem with user input)
#Logic errors: sytax-correct, runs perfectly but the result is not expected



#Metro Card program
card = float(input("How much is left on your card: "))
#compute the left rides
rides_left =int(card//2.75) # // or int()
print(rides_left)



#Time Calculations
seconds = int(input('Enter second: '))

#compute minutes
minutes = seconds // 60
reminder_seconds = seconds % 60
hours = minutes//60
reminder_minutes = minutes % 60

print("That is",hours,"hours",reminder_minutes,"minutes",reminder_seconds,"seconds")



#Format functions
format(52752.3242,".2f")#generates string
money = 100.70
money_format= format(100.70,".2f") #perserve your insignificant 0s
