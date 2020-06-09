#Recall: .split()
phrase = "hello+world+pikachu"

print(  phrase.split("+")[0]    )


#File I/O
x = input("What is your name") #stored in short term

#long term memory
name = input("Enter your name: ")
#put name into long term storage so we can access it later

#ask the operating system for a link to a file

file_pointer = open("names.txt","a")
#put the user's name into the file
file_pointer.write(name)
file_pointer.write("\n")

#close the file - we are done
file_pointer.close()

print("all done")

#Programming example: Pokemon names
try:
    file_pointer = open("names.txt","r") #read only 

except:
    print("File doesn't exist")

else:
    #ask the program to grab all the data as a big string

    alldata = file_pointer.read()

    #close the file
    file_pointer.close()

    print(alldata)
    #alpha order:
    #convert the string into a list
    #.rstrip() method -> takes out all white space from the right
    alldata = alldata.rstrip()
    #likewise, .lstrip takes out white spaces from the left
    names_list = alldata.split("\n")
    #sort the names
    names_list.sort()
    print(names_list)


#Programming example: scores
#open up the scores file
file_pointer = open("scores.txt",'r')

#read the data as a big string
alldata = file_pointer.read()

#close the file
file_pointer.close()

#isolate each student
students = alldata.split("\n")

print(students)

#isolate scores
for item in students:
    split_item = item.split(",")
    print(split_item)

    #extract the scores from this student's list
    scores = split_item[1:]
    for i in range(len(scores)):
        scores[i] = int(scores[i])

    print(scores)
    print(sum(scores)/len(scores))




