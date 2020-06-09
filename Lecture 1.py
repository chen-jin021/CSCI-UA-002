#print ("Hi, I am Criag.")
#this is a string
a = 3
b = 5
print("a + b = ",a+b)

#this is commenting
print("a","b","c",sep="***") #Python automatically place spaces between strings
print("AAA\nBBB\nCCC") #\n is a line breaker
print("EEE\tFFF\tGGG") #\t is a tab
print("A","B","C",sep="*",end="\t")
print("D\nE\nF",end="")
print("Q")


#Variables
name = "pikachu"

print("hello,",name)

top_speed = "fast"
TOP_SPEEF = "slow" #these two are different
#no numbers can be put in the front of a variable name
#can only use alphanumeric values and the “_” symbol in variable names


#Input function
name = input("What is your name? ")
print("Thanks,", name)


#One big program

#ask the user for four words
noun = input("enter a noun ")
verb = input("enter a verb ")
adj = input("enter an adjective ")
adv = input("enter an adverb ")

#Print the story with the new vars
print("The",adj,noun,"was very hungry, so it decided to" ,adv,verb, "to the nearest restaurant.")
