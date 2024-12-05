# Lists
fruits = ['orange','melon','pineaple','lemon']
names = ["joseph","maria","vagner","daniel",]
ages = [24,12,33,24]

for x in fruits:
    print(f"{x}")
print("")

for x in names:
    print(f"{x}")
print("")

for x in ages:
    print(f"{x}")
print()

#Index
print("index")
print(fruits[0])
print(fruits[1:3])
print(fruits[2:4])
print(fruits[3:5])
print(fruits[4:6])
print(fruits[5:7])
print(fruits[6:8:2])
print("")

#Methods and function lists
names_new = ["daniel","renato","jose"]

for x in range(3):
    print("Add your name !")
    name_user = input("")

    #Add name end list
    names_new.append(name_user)

print(names_new)

#insert
# choose where put element
names_new.insert(0,"maria")
print(names_new)

#extend
#doing join elements
names_new.extend(names)
print(names_new)
print("")

#pop (remove index by default last element)
names_new.pop(0)
print(names_new)

names_new[1]
print(names_new)

#remove (remove element by name, only remove the first research)
names_new.remove("daniel")
names_new.remove("renato")
names_new.remove("jose")
print(names_new)
print()

#index - found where is element - display where it's with base in element
print(names_new.index("maria"))
print("")

#sort
names_new.sort()
print(names_new)
print()

#functions extra
print(len(names_new))
print(sum(ages))
print(min(ages))
print(max(ages))


