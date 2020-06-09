while 5>2:
    print('hi')
    #break code to stop this infinite loop
    break
print('ok')


#Grocery Checkout Calculator
total = 0.0
again = "yes"
#float input Here this is called an accumulator variable

while again == "yes":
    #ask the user for a price
    price = float(input("Enter a price: "))

    #Add the price value to the accum variable
    total += price

    #ask if we want to stop
    again = input("Do you want to add another item?")

#calculate 7% sales tax
tax = 0.07 * total

print("The total is",total,"and the tax is",tax)





#Sentinel: Alternative of Grocery Checkout Calculator
total = 0.0
#float input Here this is called an accumulator variable

while True:
    #ask the user for a price
    price = float(input("Enter a price, type 0 to end: "))

    if price == 0:
        break

    #Add the price value to the accum variable
    total += price

#calculate 7% sales tax
tax = 0.07 * total

print("The total is",total,"and the tax is",tax)




#ask the user for a positive number
#Grocery Checkout Calculator
total = 0.0
items = 0
#float input Here this is called an accumulator variable

while True:
    #ask the user for a price
    price = float(input("Enter a price, type 0 to end"))
    while price <= 0:
        print("Bad user!")
        print("I said a POSITIVE number")
        number = int(input("Enter a positive number: ")

    if price == 0:
        break
    else:
        #Add the price value to the accum variable
        total += price
        items += 1

#calculate 7% sales tax
tax = 0.07 * total

print("The total is",total,"and the tax is",tax)
print("There is total item:",items)
