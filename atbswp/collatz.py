def collatz(number):
    if (number%2)==0:
        print(number//2)
        return(number//2)
    else:
        print(3*number+1)
        return(3*number+1)

print("Please enter a number.")
a = int(input())

while a!=1:
    a = collatz(a)
