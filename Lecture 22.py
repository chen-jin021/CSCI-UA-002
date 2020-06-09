#Exceptions
value = "apple"

#defensive coding
if value.isdigit():
    x = int(value) # ->this could cause runtime error
else:
    print("can't do that")


value = "55"   
#exception handling
try:
    #try something that could cause an issue
    x = int(value)
    print("x is",x)
    
except:
    #if there was a runtime error in "try" block:
    print(value,"cannot be turned into an integer")
    
#optional: else block
else:
    #this will run if everything in the 'try' block succeeded
    print("everything was okay")

print("done")


#comprehensive data validation
while True:
    try:
        num = float(input("Enter a number: "))
    except:
        print("Not convertable")
    else:    
        if num < 0:
            print("No negatives allowed")
        else:
            break


#Strings and Lists - Parsing
data = "Craig,Professor,NYU"
print(data)
#grab substring
data_split = data.split(",") #.split() produce a list
print(data_split)
print(data_split[0])


string = "A+B+C+"
string_split = string.split("+")
print(string_split[3]) #empty string

string = "A++B++C"
string_split = string.split("+")
print(string_split)

string = "A++B++C"
string_split = string.split(",") #split never generate runtime error
print(string_split)


string = "A++B+C++D"
string_split = string.split("++") #allow for more than one character
print(string_split)


#Parsing: turning data into numeric datatype
data = "100,90,80,70,55,32,71,87,99,31"

#turn the data into a list
split_data = data.split(",")
print(split_data)

int_list = []
for element in split_data:
    int_version = int(element)
    int_list.append (int_version)
print(int_list)


#let's do it with just one list:
data = "100,90,80,70,55,32,71,87,99,31"

#turn the data into a list:
split_data = data.split(",")

for i in range(0,len(split_data)):
    split_data[i] = int(split_data[i])
    print(split_data)


#Programming challenge: Morse Code
code = "0,-----,1,.----,2,..---,3,…--,4,....-,5,.....,6,-....,7,--...,8,---..,9,----.,A,.-,B,-...,C,-.-.,D,-..,E,.,F,..-.,G,--.,H,....,I,..,J,.---,K,-.-,L,.-..,M,--,N,-.,O,---,P,.--.,Q,--.-,R,.-.,S,...,T,-,U,..-,V,...-,W,.--,X,-..-,Y,-.--,Z,--.."
#split up the code string so we can access all of the elements
split_code = code.split(",")

#ask the user for a word
word = input("enter a word: ").upper()

morse = []
for c in word:
    try:
        loc = split_code.index(c)
    except:
        pass
    else:
        command = split_code[loc+1]
        print(c,":",command)
        morse.append(command)
print(morse)


#External Data
import urllib.request

#define the website we are pulling data from
url = "https://cs.nyu.edu/~kapp/python/girls_2010.txt"

try:
    #open a request - urlopen method
    request = urllib.request.urlopen(url)

except:
    print("URL invalid")

else:
    #once this is open, grab the data from the website
    data = request.read().decode("utf-8")

    print(data)
    #split the string into a list
    names = data.split("\n")
    print(names)

    #ask the user for a name
    name = input("enter a name: ").upper()

    #see if the name is popular in 2010
    if name in names:
        
        #if so, tell them HOW popular (they are ranked by popularity)
        rank = names.index(name) +1
        print(name,"is the",rank,"most popular")

    else:
        print(name,"is not popular this year")
    


#External Data
import urllib.request

#define the website we are pulling data from
url = "https://cs.nyu.edu/~kapp/python/WorldSeriesWinners.txt"

try:
    #open a request - urlopen method
    request = urllib.request.urlopen(url)

except:
    print("URL invalid")

else:
    #once this is open, grab the data from the website
    data = request.read().decode("utf-8")
    teams = data.split("\n")

    print(teams)
    
#frequency algorithm -> two parallel lists
#unique lists
#count list
unique = []
count = []

for t in teams:
    #is it new?
    if t not in unique:
        unique.append( t )
        count.append( 1 )
    else:
        #find the position
        pos = unique.index(t)
        count[pos] += 1
print(unique)
print(count)

most_wins = max(count)
most_wins_position = count.index(most_wins)
team_win = unique[most_wins_position]

print("Team is:",team_win)
        
    







