import random

print("Welcome to the random name generator!")

firstlist = []
first = open("firstname.txt", "r")
for item in first:    
    lower = item.lower()
    strip = lower.strip()
    firstlist.append(strip.capitalize())
first.close()

lastlist = []
second = open("lastname.txt", "r")
for item in second:
    lower = item.lower()
    strip = lower.strip()
    lastlist.append(strip.capitalize())
second.close()

randFirst = firstlist[random.randrange(0,len(firstlist))]
randLast = lastlist[random.randrange(0, len(lastlist))]
print(randFirst, randLast)
