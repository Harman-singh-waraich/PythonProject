import turtle
n = int(input("enter no. of squares"))
angle = 360/n
current = angle
head = turtle.Turtle()
head.speed(0)

for _ in range(n):
    head.forward(100)
    head.left(90)
    head.forward(100)
    head.left(90)
    head.forward(100)
    head.left(90)
    head.forward(100)
    head.home()
    head.left(current)
    current += angle
    
input("press enter to exit")
