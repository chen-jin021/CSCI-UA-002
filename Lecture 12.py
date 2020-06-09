'''
list(range(3))
#[0,1,2]
for i in [2,5]: #this is a range function
    print(i,end="_")
'''
#nested loops
for i in range (3):
    print("*",i)
    for j in range (3):
        print("#",j)

#On exam for sure 
for i in range(2):
    print('X',end="_")
    for j in range(2):
        print(i,j,end="_")
