'''
#recall while loop
c = 0
while c < 10:
    print(c)
    c+= 1

#intro to for loop   
for something in [10,20,30,40]: #[x,y,z] is a list
    print(something)
#strings are collection of characters
for something in "pikachu":
    print(something)

phrase = input("Enter a phrase:")
#Count vowels: a,e,i,o,u
for letter in phrase:
    if letter == "a" or letter == "e" \\
    or letter == "i" or letter == "o" or letter == "u":
        print(letter, "is a vowel")
    else:
        print(letter,"is not a vowel")

#range() function, must be integers
#print number 1 - 10
#                   11,5,-1
#                   5,10,2
import time #time.time() generate the current time Unix Epoch

start = time.time()
for number in range(10,-1,-1): #never reach the upperbounds
    print(number)
    time.sleep(1)
    
end = time.time()

print("Time elapsed:",end-start)
#time.sleep(2) -- put program sleep in 2-seconds


#Squares
print("Number\tSqaure")

for i in range(1,11):
    print(i,i**2,sep="\t")

#rewite with while loop
c = 1
print("Number\tSqaure")

while c < 11:
    print(c,c**2,sep="\t")
    c+=1

#This while loop cannot be converted to a for loop
number = int(input("Enter a positive number:"))
while number <= 0:
    print("Try again")
    number = int(input("Enter a positive number:"))


#Patterns: Stair star
for i in range(2,13,2):
    print("*"*i)
#Look at the numerical sequence and then look at the graphics

#Pattern 2:
for i in range(2,13,2):
    print(" "*(12-i),"*"*i, sep="")

#Pattern 3:
for star in range (2,13,2):
    print("*"*star)
for star in range (10,0,-2):
    print("*"*star)


#PySculputer 3D
cube(0,0,0)
cube(-500,0,0)
cube(500,0,0)
#cubes are exactly 50 unit
cube(0,50,0)

cube(0,0,0)
cube(-500,0,0)
cube(500,0,0)
#cubes are exactly 50 unit
cube(0,50,0)

#Produce cubes for the whole x-axis
for i in range (-500,501,50):
  cube(i,0,0)
#z-axis
for i in range (-500,501,50):
  cube(0,0,i)
for i in range (50,501,50):
  cube(0,i,0)

#do it in one loop
for i in range(-500,501,50):
  cube(i,0,0)
  if i > 0:
    cube(0,i,0)
  cube(0,0,i) 

#adjust size: cube(0,0,0,100,500,10)
thickness = 10

for i in range(-500,501,50):
  cube(i,thickness*0.5,0, 50, thickness,50)
  thickness += 20
  if i > 0:
    cube(0,i,0)
  cube(0,0,i) 


start = int(input("Enter a start value:"))
end = int(input("Enter an end value:"))

for i in range(start, end+1):
    print(i)


#Lottery Program
import random
#ask user for how many numbers they want
wanted = int(input("How many you want:"))

#loop that number of times
for i in range (wanted): #user-controlled range

    #generate a random between 1 and 60:
    r = random.randint(1,60)
    print(r)


#PySculputer 3D   
import random

#ask user for how many cubes they want
wanted = int(input3d("How many:"))

for i in range (wanted):
  x = random.randint(-500,500)
  y = random.randint(-500,500)
  z = random.randint(-500,500)

  u = random.randint(10,90)
  v = random.randint(10,90)
  w = random.randint(10,90)
  cube(x,y,z,u,v,w)


'''
#Most IMPORTANT idea: Nested Loops
#              [0,1,2]
for i in range (3):
    print("#",i)
    print("***")
#              [0,1,2]
    for j in range (3): #inner loop
        print(j)

#clock
import time

for hour in range (0,24):
    
    for minute in range (0,60):

        for second in range (0,60):

            #print(hour,":",minute, ":", second)
            #time.sleep(1)

            #if we want to make the print function faster
            value = str(hour) +":",str(minute)+":"+str(second)
            print(value)



