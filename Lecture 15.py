 
def fun2(a):
    a += 1   
    return a 

answer=fun2(5)
print(answer)


def fun2(a):
    a += 1   #just because we have a value in the function,
    print(a) #it doesn't mean we can return the value

answer=fun2(5) #--this produces None (this is its own data type)
print(answer)



def fun1(a):
    print(a)
    a += 1
    print(a)
a = 5
print(a)
fun1(a)
print(a)

#output: 5 5 6 5 separated by lines


#Function Composition
def add(a,b):
    print(a+b) #add(1,1) print out here first
    return a+b

def sub(a,b):
    print(a-b)
    return a-b

def mult(a,b):
    print(a*b)
    return a*b

answer = 1 + 2 + 3 + add(1,1) #--add the return value (1+1)
answer2 = add(add(1,1),sub(2,1))#2 1 3 - separated by lines
print(answer)

#documentations of functions--blackbox model
#IPO notation:
#inputs:        two integers or floats
#processing:    prints the sum
#output:        returns the sum


#Important
import myfunctions

answer = myfunctions.add(1,2) + myfunctions.sub(1,1)
print(answer)




