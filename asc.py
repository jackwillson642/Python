a = [9,6,5,3,2]
t = 0
for i in range(0,4):
    for j in range(i+1,4):
        if a[i]>a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t


for k in range(0,5):
    print(a[k], end =',')
