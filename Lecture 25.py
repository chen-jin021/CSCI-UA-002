#recall dictionary
d = {}
l = [100,200,300,400,500]
l.append(10)
d["number"] = 10
print(l,d)

#Number of bugs by species
#Number of bugs by location
#Number of bugs by species & location

#access the data file
fp = open("bugs.txt","r")
bugs = fp.read()
fp.close()

#isloate lines
lines = bugs.split("\n")

#set up a counter to keep track of bugs by species
by_species = {}
by_location = {}
by_location_and_species = {}

#examine every line of data
for line in lines:
    
    items = line.split(",")

    try:
        
        #make variables to hold our values
        location = items[0]
        species = items[1]
        amount = int(items[2])
        
    except:
        print("Bad line of data")
        
    else:
        
        #see if this is a new key in the dictionary
        if species not in by_species:
            #add it!
            by_species[species] = amount
        else:
            #update it
            by_species[species] += amount

        #by location
        if location not in by_location:
            #add it!
            by_location[location] = amount
        else:
            #update it
            by_location[location] += amount

        #by location and species
        newkey = location+"_"+species

        if newkey not in by_location_and_species:
            by_location_and_species[newkey] = amount
        else:
            by_location_and_species[newkey] += amount
            
        
#report by species
print("Report by species: ")
for bug in by_species:
    print(bug,by_species[bug])
print()
print("Report by location: ")
for location in by_location:
    print(location,by_location[location])
print()
print("Report by location and species: ")
for location_and_species in by_location_and_species:
    print(location_and_species,by_location_and_species[location_and_species])





#by_species[location] = [species,amount]

















