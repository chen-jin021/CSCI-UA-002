#Programming: advanced lists
import random

try:
    
    fp = open("cards.txt","r")
except:
    print("File not found")
else:
    data = fp.read()
    fp.close()
    print(data)

    cards = data.split("\n")
    print(cards)

    #shuffle the list so that it is in a random order

    #make a new list to hold a shuffled deck
    shuffled = []
    
    #as long as there is a card left to shuffle
    while len(cards) > 0:

        #pick one at random
        i = random.randint(0,len(cards)-1)

        #put the card at this index into our shuffled list
        shuffled.append( cards[i] )

        #delete the card from the cards list
        del cards[i]
        
    print(shuffled)

#multi-dimensional lists
a = [10,20,30,"apple"]
print(a[3][1],type(a[3]))#dig into 'apple' first 'p'

b = [[1,2,3],[4,5,6],[7,[8,9]]]
print(len(b)) #3
#access number 2:
print(b[0][1])
print(b[1][2])
print(b[2][1][0]) #three sets of brackets

#programming challenge to multi-dimensional lists
#Tic Tac Toe
import random

board = [

    [".",".","."],
    [".",".","."],
    [".",".","."],

    ]

def print_board():
    for row in board:
        print(row[0],row[1],row[2])

#this var keeps track of who's turn it is
token = "X"
while True:
    print_board()

    #ask the user for their spot
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))

    if row >= 0 and row <= 2 and col >= 0 and col <= 2:

        if board[row][col] == ".":
            #place their token here
            board [ row ] [col] = "token"

            #swap to the other token
            #***TOGGLE ALGO***
            if token == "X":
                token = "O"
            else:
                token = "X"
        else:
            print("Cheater!")
    else:
        print("Invalid")

    print_board()    


#Dictionary
import random

mylist = [10,20,30]
mystring = "abc"
#key CAN NOT be duplicated
dict = {"name":"pikachu","name":"Charmander"}

#unordered, hold keys and values
mydictionary = {"name":"pikachu", True:"hello",999:"pika"}
#Key cannot be MUTABLE --> NO LISTS!!
print(mydictionary)

#.value
print(mydictionary[999])

#creating a dictionary
mydictionary = {}
print(mydictionary)
#adding into a dictionary
mydictionary["name"] = "Craig"
print(mydictionary)
mydictionary["name"] = "John"
print(mydictionary)

if "name" in mydictionary:
    print(mydictionary["name"])
else:
    print("It's not there")

#deleting from a dictionary
del mydictionary ["name"]
print (mydictionary)

#iterating over a list
a = [100,200,300]
for item in a:
    print(item)

for i in range(len(a)):
    print(a[i])
  
#iterating over a dictionary
d = {"a":5,"b":10,"c":100}
for key in d:
    print(key,d[key])


#Programming Challenge: Gradebook
#set up a dictionary to hold all of our scores
scores = {}

#ask the teacher to enter in some student names and their scores
while True:

    #ask for student name
    name = input("Enter a name ('end' to end): ")
    if name == "end":
        break

    #ask for score
    s = int(input("Score: "))

    #see if this is a new student
    if name not in scores:

        #associate the student with their score in the dictionary
        scores[name] = [s]
        
    else:
        scores[name].append(s)

    print(scores)


#generate report
#names of students
#all of their scores
#their average score
for key in scores:
    #names of students
    print(key)
    #value (score) associated with the student name
    print(scores[key])
    #avg
    num = len(scores[key])
    total = 0
    for i in range(len(scores[key])):
        total += scores[key][i]
    avg = total/num
    print(avg)


d = {"x":1,"y":4,"a":0}
print(d.keys())
#sorted function --> sorting the keys
new_d = sorted(d)
print(new_d)







