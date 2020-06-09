#3-4 programming challenging - for loop, functions and string mechanics
#Zoom room-NYU Classes and turn in source code
#Homework-like programming questions but shorter length
#There can be smaller questions inside a questions
#Open-book exam tends to be harder than in-class exams
#IPO Notation will be given for some functions

#Functions Part II:
import random

x = random.randint(1,10) #blackbox--we don't know what's inside

print(x)


x = len("pikachu") #integer
q = input("What is your name?")#string
z = int(4.5)#integer
r = print("Hello")#NONE--returning nothing

def a():
    print(5)
    print("hello")
    print("whatever")
def b():
    return 5

a()
answer = a() #this calls the function but NONE is returned to answer
#b() nothing prints out
#answer = b()
print(answer)

#Pollev--no ouput because x = 16 is not printed
#RETURN != PRINT
#Pollev Q2: main5,b5,a5,b6,main5-B

#IPO Notation:Documentation techinuqe
#Function:
#Input:
#Processing:
#Output:

#Programming Challenge: Feet to Inches
#Function:feet to inches(a)
#Input:a number of feet (integer)
#Processing: convert supplied value into inches
#Output: returns inches (integers)
def feet_to_inches(a):

    #convert feet into inches
    inches = feet * 12

    #return the value to the user
    return inches

    #unreachable code
    print('hi')
answer1 = feet_to_inches(1)
print(answer1)
print( (feet_to_inches(2) )

number = 500.234
print( format(number, ".2f") )

#Programming Challenging: Two Dice
#input: sides of dice to roll
#processing: generates two die values
#ouput: two dice values(integers)
import random

def roll_two_dice (size,double_allowed):
    while True:
        d1 = random.randint(1,size)
        d2 = random.randint(1,size)
        if d1 == d2 and answer == "Y":
            print(d1,d2)
            continue
        else:
            break
    
    #return the two dice
    return d1,d2


#ask the user if want doubles:
answer = input("Rule out doubles? Y/N")

a,b = roll_two_dice(6,answer)
print("Roll number 1:",a,"and roll number 2:",b)








