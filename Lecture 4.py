# format function
price = 1000022.70
print(price)#this will not print the last 0
format_price = format(price,".2f") 
print(format_price)
fprice_2 = format(price,",")#setting up commas
print(fprice_2)
fprice_3 = format(110.72,">10.2f")
print(fprice_3)
fprice_4 = format(110.72,"^10.2f")
print(fprice_4)

#This class, we are doing homework 2
