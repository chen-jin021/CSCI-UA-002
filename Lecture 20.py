#Lists are considered sequence objects
#comparison between string and lists
a = "hello"
b = [10,20,30,40,50,5.7,True,"hello"]

print(a[:2])
print(b[:2])

a2 = a + "apple"
print(a2)

b2 = b + [999]
print(b2)

x = "apple"
y = [1,2,3]

x = "!" + x
print(x)

y = [999] + y
print(y)


a = [1,2,3]
a += [999] #append
a = [888] + a #prepend
a.append(100)
a.insert(1,999)
print(a)


#Mutable data type-list
#Lists are Reference Types
mylist1 = [1,2,3]
mylist2 = mylist1

print(mylist1)
print(mylist2)

print("-----")

mylist1[0] = 999 #this will change mylist2 as well
#list is a reference type (Look at the picture attached in folder)


#We can avoid this by making a copy of the first list
#(instead of its reference)
mylist1 = [1,2,3]
mylist2 = [] + mylist1 #this forces Python to create a new space to hold mylist2

mylist1[0]=999
print(mylist1)
print(mylist2)


#Pollev Questions:
mylist = [1,2,3]
mylist += 2
print(mylist) #Crash


mylist = [2,10,1]
mylist += [5]
print(mylist) #[2,10,1,5]


mylist = [1,2,3]*2
print(mylist) #[1,2,3,1,2,3]

#Tricky one
v1 = "hi"
v2 = ["h","i"]

v1[0] = "!" #STRING ARE IMMUTABLE
v2[0] = "!"

print(v1,v2) #END UP CRASHING


a = [1,1]
b = [1,1]
a[0] = "Q"
c = a
c[0] = "R"
print(a,b,c) #['R',1] [1,1] ['R',1]


#Programming Challenging: Extra Points

grades = [90,100,70,45,76,84,93,21,36,99,100]

total = 0

for g in grades:
    total += g

average = total / len(grades)
print(average)
    
#apply 6 points
for i in range(len(grades)):
    grades[i] += 6

print(grades)


#Programming Challenge: Daily Sales
sales = []

for i in range(7):

    while True:
        today = int(input("Sales: "))

        if today < 0:
            print("Invalid")
        else:
            break
    sales.append(today)
print(sales)

#sum function
total = sum(sales)
print("Sum:",total)


#difference between 7th day and 1st day:
difference = sales[-1]-sales[0]
print("Difference is:",difference)


#Location using index method
x = [300,10,40,20]
item = 10
for i in range(0,len(x)):

    if x[i] == item:
        print("Found at",i)
        break
    
#defense structure: prevent crash if not found
if item in x:
    
    loc = x.index(item)
    print("Found at",loc)




#Programming: Common to both lists
a = [1,2,3,4,5]
b = [2,3,10,11,12,1]

newlists = []
for c in a:
    for d in b:
        if c == d:
            newlists.append(c)
print(newlists)
#we can sort elements - MUST BE THE SAME DATATYPE
newlists.sort()
print(newlists)




#Programming challenging: Price lookup
products = ['peanut butter', 'jelly', 'bread']
prices = [   3.99,            2.99,    1.99]
inventory = [10,              3,       17]


#ask the user for a product
p = input("Enter a product name: ")

#see if we sell this product
if p in products:
    print("We sell that")

    #look up the cost
    loc = products.index(p)
    price = prices[loc]
    
    print("Price:",price)
    print("We have",inventory[loc],"of this item")
    
else:
    print("Not available")
   

#Removing:
x = [100,200,300,400,0,500,0,0,0,0,999,0,900]

x.remove(300) #this will only pull out the first occured
print(x)
del x[11]
print(x)


#remove all the 0s ********
while 0 in x:
    x.remove(0)
print(x)

#max
print("Max number is", max(x))

#assume the first is largest
largest = x[0]

for i in range(len(x)):
    if x[i] > largest:
        largest = x[i]

print("largest is",largest)
























