import turtle
import math
screen = turtle.Screen ()
screen.setup (500, 500)
screen.title ("Tính chu vi diện tích hình tròn")
t = turtle.Turtle ()

bk = input ("Nhập bán kính hình tròn r: ")
r = int (bk)
t.penup ()
t.goto (0, -r)
t.pendown ()
t.circle (r)
t.hideturtle ()


c = 2 * math.pi * r
s = math.pi * r * r
print ("Chu vi hình tròn là: ", c)
print ("Diện tích hình tròn là: ", s)

turtle.done ()