import os
import random


# Import turtle module
import turtle
# Required by MacOS to show the window
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()    
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)
        
        # Boundary Detection
        if self.xcor() > 290:  
            self.rt(60)

        if self.xcor() < -290:
            self.rt(60)

        if self.ycor() > 290:
            self.lt(60)

        if self.ycor() < -290:
            self.lt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.xcor() >= (other.ycor() - 20)) and \
        (self.xcor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        #self.goto(-1000, 1000)
    
    def fire(self):
        print("Fire function ", self.status)
        self.goto(player.xcor(), player.ycor())
        self.setheading(player.heading())
        if self.status == "ready":
            self.status = "shoot"

    def move(self):
        if self.status == "shoot":
            self.fd(self.speed)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # Draw boarder  
        self.pen.speed(0)
        self.pen.color("blue")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#create game object
game = Game()

# Draw the game border
game.draw_border()


# Create my sprites
player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)

# Key Board bindings
turtle.onkey(player.turn_left, "a")
turtle.onkey(player.turn_right, "d")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.decelerate, "s")
turtle.onkey(missile.fire, "space")
turtle.listen()

# Main Game Loop
while True:
    player.move()
    enemy.move()
    missile.move()

    # Checking for a  collision
    if player.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)








delay = input("Press enter to finish. > ")