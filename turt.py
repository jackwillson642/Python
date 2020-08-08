import turtle


while True:
    t = turtle.Turtle()
    t.ht()
    for j in range(3,6):
        for i in range(6):
            t.forward(100)
            t.right(60)

        t.forward(100)
        t.left(60)
        t.pensize(j)
        j+=1
    t.clear()
    

turtle.done()
