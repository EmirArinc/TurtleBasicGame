import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angel_right():
    turtle_instance.right(10)

def rotate_angel_left():
    turtle_instance.left(10)


def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angel_right,key="Down")
drawing_board.onkey(fun=rotate_angel_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_return_home,key="h")


turtle.mainloop()
