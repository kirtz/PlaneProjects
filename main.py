"""
# variables

first_name = "Kirtan"
last_name = "PiZtachio"
full_name = first_name + " " + last_name
print("Hello " + full_name)
print(type(full_name))

#intergers - Ints

age = 21
age += 1
print(age)
print(type(age))


#Floats
height = 169.69
print("your height is: " + str (height)+"cm  ")
print(type(height))

#Booleans

human = True
print("Are you a human? "+str(human))
print(type(human))

#Multiple Assisgnments

Kirtz = Slay = Ash = Eriks = Yunesh = 10

print(Kirtz)
print(Slay)
print(Ash)
print(Eriks)
print(Yunesh)

#Strings Methods

print(len(full_name))
print((full_name.find("i")))
print(full_name.capitalize())
print(full_name.upper())
print(full_name.lower())
print(full_name.isdigit())
print(full_name.isalpha())
print(full_name.count("a"))
print(full_name.replace("o","0"))
print(full_name*2)

#user inputs

# user_Name = input("What is your name? ")
# user_Age = int(input("How old are you? "))
# user_Height = float(input("How Tall are you? "))

# print("Hello "+user_Name)
# print("You are "+str(user_Age)+ " years old")
# print("You are "+str(height)+"cm tall")

#math

import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,3))
print(math.sqrt(pi))
print(max(x,y,z))
print(min(x,y,z))
"""

"""Slicing = create a substring by extracting elements from another string
    indexing [] or slice ()
    [start:stop:step]

name = "Jesus Kirtz"

first_name = name[:5]
last_name = name[6:11]
step_test = name[0:11:3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(step_test)
print(reversed_name)


website = "https://netflix.com"
website2 = "https://lolesports.com"
slice = slice(8,-4,)
print(website[slice])
print(website2[slice])


#if statments = a block of code that will execute if its conditions are met (true0

age = int(input("What is ones age?: "))

if age >= 100:
    print("Ossan!")
elif age >= 18:
    print("Kawaii")
elif age < 0:
    print("Tell oka-san to push you out!")
else:
    print("I guess your just that age...")


#Logical Operators (and, or, not) = used to check if two or more conditional statements are met

temp = int(input("What is the temp outside?: "))

if temp >= 0 and temp <= 30:
    print("Basic human liveable shit, don't be a pussy!")
    print("Live a little and go out xD")
elif temp < 0 or temp >30:
    print("Damn Shit do be hitting the fan today lads")
    print("Stay inside like a pussy. xDDD")


# While loop = a statement that will execute coe as long as its conditions remains true.

name = ""

while len(name) == 0:
    name = input("Enter your name?:")

print("Hello " +name)


import time
# or loop = a statement that will execute its block of code a limited amount of time

# While loops = unlimited --- for loops = limited

# for i in range (10):
#    print(i)

# for o in range  (50,100,10):
#    print(o)

# for s in "Jesus Kirtz":
#    print(s)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Wake the fuck up")

"""

