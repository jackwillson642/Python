# to print the fibbonaci sequence

n = int(input("Enter n: "))
x=0
y=1
for i in range(n):
    x = x + y
    print (x)
    y = x - y
