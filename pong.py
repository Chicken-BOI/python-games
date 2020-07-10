import turtle

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
#doesn't allow changes
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
Paddle_a = turtle.Turtle()
Paddle_a.speed(0)
Paddle_a.shape("square")
Paddle_a.color("white")
Paddle_a.shapesize(stretch_len=1, stretch_wid=5)
Paddle_a.penup()
Paddle_a.goto(-350, 0)

# Paddle B
Paddle_b = turtle.Turtle()
Paddle_b.speed(0)
Paddle_b.shape("square")
Paddle_b.color("white")
Paddle_b.shapesize(stretch_len=1, stretch_wid=5)
Paddle_b.penup()
Paddle_b.goto(350, 0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)

# d delta and x is x speed or anything else
Ball.dx = 2
Ball.dy = -2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def Paddle_a_up():
    y = Paddle_a.ycor()
    y += 20
    Paddle_a.sety(y)

def Paddle_a_down():
    y = Paddle_a.ycor()
    y -= 20
    Paddle_a.sety(y)

def Paddle_b_up():
    y = Paddle_b.ycor()
    y += 20
    Paddle_b.sety(y)

def Paddle_b_down():
    y = Paddle_b.ycor()
    y -= 20
    Paddle_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(Paddle_a_up, "w")
win.onkeypress(Paddle_a_down, "s")
win.onkeypress(Paddle_b_up, "Up")
win.onkeypress(Paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))    

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Paddle_b.ycor() + 50 and Ball.ycor() > Paddle_b.ycor() -40):
        Ball.setx(340)  
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Paddle_a.ycor() + 50 and Ball.ycor() > Paddle_a.ycor() -40):
        Ball.setx(-340)  
        Ball.dx *= -1