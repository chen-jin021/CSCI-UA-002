#String manipulation
for i in [10,15]:#This is a list
    print(i)
    
for i in "hello world":
    print(i)

word = "Sally Sells Sea Shells by the Sea Shore"
#write a program to count the number of 's' characters in this string
s_count = 0
#for letter in word.lower():
#if letter in ['S','s']:
for letter in word:
    if letter == "S" or letter == "s":
        s_count += 1

#make a function - character_count
def character_count(w,desired):
    found = 0
    for letter in w:
        if letter == desired:
            found += 1
    return found

s_count = character_count (word,"S")+ character_count (word,"s")
print(s_count)


number_of_s = word.lower().count('s')
print(number_of_s)



#String indexing:
#        012345
word1 = "python"

desired = 5

#ERROR: print(word1[7]) - index error
if desired >= len(word1):
    print("Doesn't exists")
else:
    print(word1[desired])

print(word1[-1])
#is equivalent to:
print(word1[len(word1)-1])

#Slice - just like the range function
print(word1[0:2])#py
print(word1[2:])#thon

#Pollev
#Q1: o
#Q2: s
#Q3: e
#Q4: hom
#Q5: sweet home!
#Q6: hewto!



#Programming Challenge: username generation
#first name
first = input("Enter first name: ")
#last name
last = input("Enter last name: ")
#N-number
nnum = input("Enter N-number: ")

#extract first two char of first and last
initial_first = first[0]+first[1]
initial_last = last[:2]
last_three = nnum[-3:]

net_id = initial_first + initial_last + last_three
print(net_id)


#pig latin
word = input("word: ")
first = word[0]
pig_latin = word[1:]+first+"ay"
print(pig_latin)


#iterating over the string
phrase = "hello world"

for i in range(0,len(phrase),2):
    print(i,phrase[i])

for letter in phrase:
    print(letter)


#ASCII table: ord() chr()
print(ord("A")) #65

for letter in "hello world":
    print(letter, ord(letter))


print( chr(66) )
for i in range(65,97):
    print(i, chr(i))


#NOTE: IF GENERATE ONLY LETTERS NOT NUMBERS -> WHILE LOOP TO EXAMINE!
#generate random password
#10 characters long, upper, lower and number:
import random

#accum to hold pw
password=""
number = 0
lower = 0
upper = 0

while True:
    #generate 10 values
    for i in range(10):
        choice = random.randint(1,3)
        if choice == 1: #uppercase letters
            password += chr(random.randint(65,90))
            upper += 1
        elif choice == 2:#lowercase letter
            password += chr(random.randint(97,122))
            lower += 1
        else:#numbers
            password += chr(random.randint(48,57))
            number += 1
    if not (upper == 0 or number == 0 or lower == 0):
        break
    else:
        print(password,". We need to regenerate!")
    
print(password)


#encoding mechanism -
#a ->b add one

word = "apple"

encoded = ""

for i in word:
    ascii_code = ord(i) #REMARK: i STANDS FOR THE ACTUAL LETTER
    encoded += chr(ascii_code+1)
    
print(word)
print(encoded)

#decode the code
decoded = ""
for i in encoded:
    decoded += chr(ord(i)-1)

print(decoded)



#String OPERATORS
print("apple" in "applesauce")
print("apple" in "appdejkle")#gives False because it's not in particular order
print("apple" not in "appdjejwle")#True


#String METHODS
#String testing methods
print("apple".isalpha())
print("apple and pear".isalpha())#false as there is space
#functions belong to objects
#CANNOT DO 5.isalpha()
#BECAUSE THESE FUNCTIONS ARE STRING FUNCTIONS

#Programming challenge:
phrase = input("Enter a phrase: ")

spaces = 0
digits = 0
vowels = 0 #aeiou
consonants = 0 #any letter that is not vowel

#examine every char in the phrase
for c in phrase:
    if c.isspace():
        spaces += 1
    elif c.isnumeric():
    #elif c in "0123456789":
    #elif 48 <= ord(c) <= 57:
        digits += 1
    elif c.isalpha():
        if c.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Spaces:",spaces)
print("Digits:",digits)
print("Vowels:",vowels)
print("Cons:",consonants)
            


#immutable property of string
word = "Python"
word2 = word.lower()
print(word2,"and word original is",word)  
