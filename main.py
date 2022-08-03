import turtle as t

tim = t.Turtle()
screen = t.Screen()


def go_forwards():
    tim.forward(10)


def go_backwards():
    tim.backward(10)


def go_counter_clockwise():
    tim.setheading(tim.heading() + 10)


def go_clockwise():
    tim.setheading(tim.heading() - 10)


def clear_drawing():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


t.onkey(go_forwards, 'w')
t.onkey(go_backwards, 's')
t.onkey(go_counter_clockwise, 'a')
t.onkey(go_clockwise, 'd')
t.onkey(clear_drawing, 'c')

screen.listen()
screen.exitonclick()
