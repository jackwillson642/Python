import time

def calcProd():
    pro = 1
    for i in range(1, 100000):
        pro = pro*i
    return pro


startTime = time.time()
prod = calcProd()
endTime = time.time()

print("The result is %s digits long." % (len(str(prod))))
print("The process took %s seconds." % (endTime - startTime))


# import time
# def calcProd():
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()

# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))
