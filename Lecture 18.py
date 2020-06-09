#Exam 2: 50% more complexity- 4 questions and 1hr 15min

#String methods
print("python".isalpha()) #--testing method
print("python".islower())
print("Python".isupper())

word = "python"
word = "Python"
print(word[0].isupper())

word = "python is cool"
print(word.isupper())
word2 = word.upper() #--modification method
print(word2)
print(word)
word3 = word.capitalize()
print(word3)

#searching & replacement method
phrase = "like a needle in a haystack needle needle needle"

if "needle" in phrase:
    print("found it!")
else:
    print("I didn't find it")


location = phrase.find("needle")
print(location) #index where substring begin

if location == -1: #-1 is a sentinel value, meaning we didn't find
    print("didn't find the string")
else:
    print('Found at location:',location)

#also can find the first one, slice it, find again in substring, slice etc.
time = phrase.count("needle")
print(time)
