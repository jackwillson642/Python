from random import *

randNum = randint(1,20)

print("I'm thinking of a number between 1 and 20")
a = int(input("Take a guess: "))

c=1
while True:
    if(a == randNum):
        print("Correct")
        break

    elif(a > randNum):
        print("Too high")

    else:
        print("Too low")

    a = int(input("Try again: "))
    c = c+1

print("You took %d Guesses" % c)
