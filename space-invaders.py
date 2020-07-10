import turtle
import os
import time
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw board

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.hideturtle()
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

# Create the Player turtle
player = turtle.Turtle()
player.color("grey")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 20

# Choose a number of enemies
n_o_e = 5

# Create an empty list of enemies
enemies = []

# add enemies to the list
for i in range(n_o_e):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("green")
    enemy.shape("square")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# Create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 35

# collision checking
def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > -100:
        y = -100
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -250:
        y = -250
    player.sety(y)

def fire_bullet():
    global bulletstate
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
        # Move the bullet to just above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()
    bulletstate = "fire"


# Keyboard Bindings
turtle.listen()
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_bullet, "space")

score = 0


score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))

# Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Enemy Boundary Checking and moving it up and down
        if  enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40 
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40 
            enemyspeed *= -1
            enemy.sety(y)

        if iscollision(bullet, enemy):
            score = score + 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
            print(score)
            bullet.hideturtle()
            bullet.setx(0)
            bullet.sety(0)
            bulletstate = "ready"
            enemy.goto(random.randint(0, 200), random.randint(200, 250))

        if iscollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")

    # Move the Bullet
    if bulletstate == "fire":   
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check if collision happened
    if iscollision(bullet, enemy):
        score = score + 10
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
        print(score)
        bullet.hideturtle()
        bullet.setx(0)
        bullet.sety(0)
        bulletstate = "ready"
        enemy.goto(random.randint(0, 200), random.randint(200, 250))

    
