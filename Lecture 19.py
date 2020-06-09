#Biased towards later content
#15-20 min per program
#Review: Function

def a():
    print('a')
    
def b():
    print('b')
    
def c():
    print('c')
    a()
    
def d():
    print('d')
    c()

print("x")
d()

#Trace the output
def a(x):
    print(x)
    x += 1
    print(x)

x = 10
print(x)
a(x)
print(x)


#Review: String manipulations
#Programming Challenging Question 1:
def stats(string):
    #numeric contain in string
    #sum of all numeric
    #the largest numeric character
    largest_num = 0
    smallest_num = 9
    numeric_sum = 0
    numeric_char = 0

    non_numeric = 0
    for i in string:
        if i.isnumeric() == False:
            non_numeric += 1
    if non_numeric == len(string):
        return 0,non_numeric,"undefined","undefined","undefined","undefined"
    
    for i in string:
        if i.isnumeric() == True:
            numeric_sum += int(i)
            
            numeric_char += 1
            
            if int(i) >= largest_num:
                largest_num = int(i)
            if int(i) <= smallest_num:
                smallest_num = int(i)
        
    #non-numeric characters
    len_string = len(string)
    
    #average of all numeric sum
    average_numeric = numeric_sum / numeric_char

        

    return numeric_char, non_numeric, numeric_sum,average_numeric, largest_num, smallest_num


g,b,t,a,mx,mn = stats("12345")
print (g, b, t, a, mx, mn)
# 5 0 15 3.0 5 1
g,b,t,a,mx,mn = stats("111111191111181111113")
print (g, b, t, a, mx, mn)
# 21 0 38 1.809523 9 1
g,b,t,a,mx,mn = stats("pikachu")
print (g, b, t, a, mx, mn)
# 0 7 undefined undefined undefined undefined
g,b,t,a,mx,mn = stats("123pikachu456")
print (g, b, t, a, mx, mn)
# 6 7 21 3.5 6 1
g,b,t,a,mx,mn = stats("")
print (g, b, t, a, mx, mn)
# 0 7 undefined undefined undefined undefined









import random

def pokemon_generator (time):

    if time[2] != ":" or len(time) != 5:
        return "INVALID TIME"

    #check valid:
    hour = int(time[0]+time[1])
    minute = int(time[3]+time[4])
    
    if 0< hour < 24 and 0 <= minute <= 59:
        #Case 1:
        if 6 <= hour <= 17 and 0 <= minute <= 59:
            random_pick = random.randint(1,2)
            if random_pick == 1:
                return "Pidgey"
            else:
                return "Caterpie"
        else:
            random_pick = random.randint(1,2)
            if random_pick == 1:
                return "Rattata"
            else:
                return "Zubat"
    else:
        return "INVALID TIME"
            


print ( pokemon_generator("06:00") ) # Pidgey
print ( pokemon_generator("09:57") ) # Pidgey
print ( pokemon_generator("18:05") ) # Zubat
print ( pokemon_generator("23:42") ) # Rattata
print ( pokemon_generator("99:00") ) # INVALID TIME
print ( pokemon_generator("06:99") ) # INVALID TIME
print ( pokemon_generator("apple:00")) # INVALID TIME
print ( pokemon_generator("00:pear") ) # INVALID TIME
print ( pokemon_generator("pikapika") ) # INVALID TIME
print ( pokemon_generator("06-00") ) # INVALID TIME

'''



#Password Generator:

#Length:
#randomly generate a num bt 8-13
#this determines the length

#for in between random (1,3) and each stands for num upper and lower
#ASCII table find upper and lower case range








    
