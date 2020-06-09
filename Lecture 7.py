
import random
#random.seed(123456) #start here instead of looking at the computer

#ask user for RPS
u = input("R,P,S: ")

# flip a coin
coin = random.randint(1,2)

if coin == 1:
    
    #now we want to "cheat" so user will lose everytime
    if u == "R":
        c = "P"
    elif u == "P":
        c = "S"
    else:
        c = "P"
else:   
    #computer random RPS
    number = random.randint(1,3)
    if number == 1:
        c = "R"
    elif number == 2:
        c = "P"
    else:
        c = "S"


print("The computer selected", c)

#Output who won
if u == c:
    print("TIE")
elif (u == "R" and c == "S") or (u == "S" and c == "P") or (u == "P" and c == "R"):
    print("YOU WON")
else:
    print("LOST")


#introduced genetic algorithm
    

#degree conversion
convert = "yes"
while convert == "yes":
    #ask for input
    temp_f = int(input("Temp in F:"))

    #convert to c
    temp_c = (temp_f - 32)* 5/9

    #output
    print("Temp in c:", temp_c)

    #ask whether continue
    convert = input("Continue? (\"yes\" or \"no\")")

    print("...here we go...")
    
print("All done")




#pick a random number
import random
secret = random.randint(1,10)

game = "on"
while game == "on":
    
    #get a user guess
    guess = int(input("Enter a guess:"))

    #correct?
    if guess == secret:
        print("You got it")
        game = "over"
        
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")


#heads tails
import random

heads = 0
tails = 0


while (heads + tails) <= 1000000:
    coin = random.randint(1,2)

    if coin == 1:
        heads += 1
    else:
        tails += 1

print("Heads:",heads)
print("Tails:",tails)

