#while loop problem

#guess problem
import random

secret = int(input("Secret number:"))

attempts = 0
#ask the COMPUTUTER to guess until they get it correct
while True:
    #guess a number
    guess = random.randint(1,10000000)
    attempts += 1
    
    if guess == secret:
        print("I got it!")
        print("Attempts：",attempts)
        break


#make it more efficient
#guess problem
import random

secret = int(input("Secret number:"))

low = 0
high = 10000000
attempts = 0

#ask the COMPUTUTER to guess until they get it correct
while True:
    #guess a number
    guess = random.randint(low,high)
    attempts += 1
    print("My guess is,",guess)
    
    if guess == secret:
        print("I got it! I tried",attempts) 
        break
    
    elif guess < secret:
        low = guess
    else:
        high = guess








    
