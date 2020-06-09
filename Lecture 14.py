
def fun1 ():
    print('hi')

#call the function
fun1()
#functions are reusable
fun1()
for i in range(10):
    fun1()
#define function before envoke it
#similarly,
import random #we have to import random first
num = random.randint(1,5)
print(num)

#Flow of execution
#There can be a temporary deviation if we created a function and call it later
def hello():
    print("Hi there!")
    print("I'm a function!")
print("Good morning")
print("Welcome to class")

hello()
print("And now we are done")

#Defined function inside another defined function
def b():
    print("b")
    a()
def a():
    print("a")


b() #Python runs this because up till here, Python has pre-scanned fun a()



#aruguments
print("hi")
len("hello")
random.randint(1,5)
def add_two_numbers(a,b):#parameters
    print("I got",a,"and",b)

add_two_numbers(10,5)#we need two arguments



#local variables
def fun3(a):
    print("Inside fun 3:",a)
    a += 1
    print("Inside fun 3:",a)

a = 10
print("Outside:",a)
fun3(a)
print("Outside:",a)

a = 10
def fun4():
    print(a) #because there is no local variable-a

fun4()


#Important
a = 10
def fun4():
    global a #--- if we have this, then the next line works
    a += 1 #WRONG: functions cannot change the value of the global variable
    print(a) #because there is no local variable-a

fun4()


def fun5():
    a = 10
    print("Inside",a)
    a += 1
    print("inside",a)

fun5()
print(a) #---- We cannot access variable a anymore [local variables]



#Programming challenge:
def tip_calculator (bill,tip_rate):
    #compute how much tip to leave
    tip_to_leave = bill * tip_rate

    #compute the total bill
    total_bill = bill + tip_to_leave

    #output to the user
    print("Tip to leave:",tip_to_leave)
    print("Total bill:",total_bill)

    # see if they need to be more generous
    if tip_rate < 0.15:
        print("Be more generous!")
    

b = float(input("How much is your check:"))
r = float(input("What is your tip rate in percentage"))

tip(b,r)



name = input("What is your name")

def fun6(x):
    a = 100
    answer = a + x
    return answer

biganswer = fun6(2)
print(biganswer)
# print(answer) - would not work, answer is still local

print( fun6(2) )
print( len("Python") )











