#!/bin/python
# to find the factorial of a number

def fact(a):
    f = 1
    for i in range (1,a+1):
        f = f*i
    return f

x=int(input("Enter a number: "))
fact = fact(x)
print (fact)
