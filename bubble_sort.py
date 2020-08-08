# to arrange nos. in a list in ascending order using bubble sort

print ("Enter a list of numbers:")
t=0
a= []
while True:
    x=input()
    if x=='':
        break
    a.append(int(x))

n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if (a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
            # t = a[j]
            # a[j] = a[j+1]
            # a[j+1] = t


for i in range(n):
    print(a[i], end=', ')

