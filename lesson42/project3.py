import turtle
turtle.Screen().bgcolor("Orange")
turtle.title("Welcome to Turtle Window")
board = turtle.Turtle()

# Square
board.pendown()
board.forward(150)
board.right(90)
board.forward(150)
board.right(90)
board.forward(150)
board.right(90)
board.forward(150)

# Move to the side
board.penup()
board.left(90)
board.forward(200)   # space between square and star
board.pendown()

# Star
board.forward(150)
board.right(144)
board.forward(150)
board.right(144)
board.forward(150)
board.right(144)
board.forward(150)
board.right(144)
board.forward(150)

turtle.done()
