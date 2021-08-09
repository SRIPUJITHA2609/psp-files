import turtle
group1 = turtle.Turtle()
turtle.title("spiral")
screen = turtle.Screen()
screen.bgcolor("white")
list = ["grey","black"]
for i in range(200):
    group1.color(list[i%2])
    group1.width(2)
    group1.forward(i)
    group1.left(59)
    group1.speed(200)
