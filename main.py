import turtle
def koch_curve(t, iterations, length, shortening_factor, angle):
  if iterations == 0:
    t.forward(length)
  else:
    print("Loop: " + str(loop))
    print("iteration before: " + str(iterations))
    iterations = iterations - 1
    print("iteration after: " + str(iterations))
    length = length / shortening_factor
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.right(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.right(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
t = turtle.Turtle()
t.hideturtle()
turtle.colormode(255)
t.pencolor((255, 0, 102))
t.pensize(3)
loop = 1
for i in range(4):
  koch_curve(t, 2, 200, 3, 90)
  t.left(90)
  loop = loop+1
turtle.mainloop()
