#Programming Challenge: Weight Loss
weights = []

for i in range(7):
    weight = float(input("Weight on Day"+str(i+1)))
    if weight > 0:
        weights.append(weight)
        
print("Day 1:",weights[0],"Day 7:",weights[-1])
print("Change from first to last:",weights[-1]-weights[0])
print("Average weight",sum(weights)/len(weights))
print("Max:",max(weights),"Min:",min(weights))


#Programming Challenge: Color
colors = []

for i in range(5):
    c = input("Enter a color value: ")
    while True:
        if c not in colors:
            colors.append(c)
            break
        else:
            print("duplicate")
            c = input("Enter a color value: ")
            
print(colors)
colors.sort()
print(colors)


#Second way:
colors = []

while len(colors) < 5:
    c = input("Enter a color value: ")

    if c not in colors:
            colors.append(c)
    else:
        print("duplicate")
















        
