import turtle
import math
import time
import random
import pygame
pygame.init()

# Set up the screen
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("wow such game")
wn.setup(600, 800)
wn.bgpic("background.gif")
wn.tracer(0)

# Register shape

shapes = ["background.gif", "cat.gif", "dogLeft.gif", "dogRight.gif",
          "hat.gif", "home.gif", "homeCat.gif", "log.gif", "smallCat.gif"]
    
for shape in shapes:
    wn.register_shape(shape)
    
# Sound effects
jumpSound = pygame.mixer.Sound("jump.mp3")
waterSound = pygame.mixer.Sound("water.mp3")
dogSound = pygame.mixer.Sound("dog.mp3")
winSound = pygame.mixer.Sound("win.mp3")
loseSound = pygame.mixer.Sound("gameOver.mp3")
homeSound = pygame.mixer.Sound("homeSound.mp3")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()



# Create classes
class Pen():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()
        
    def update(self):
        pass
        
    def isCollision(self, thing):
        # Axis Aligned Bounding Box
        xCollision = (math.fabs(self.x - thing.x) * 2) < (self.width + thing.width)
        yCollision = (math.fabs(self.y - thing.y) * 2) < (self.height + thing.height)
        
        return (xCollision and yCollision)

class Player(Pen):
    def __init__(self, x, y, width, height, image):
        Pen.__init__(self, x, y, width, height, image)
        self.dx = 0 # movement speed
        self.collision = False
        self.catHome = 0
        self.maxTime = 60
        self.remainingTime = 60
        self.startingTime = time.time()
        self.lives = 3
        self.gameOver = False
        
    # Movement
    def up(self):
        self.y += 50
        jumpSound.play()

    def down(self):
        self.y -= 50
        jumpSound.play()

    def right(self):
        self.x += 50
        jumpSound.play()

    def left(self):
        self.x -= 50
        jumpSound.play()
        
    def update(self):
        self.x += self.dx
        # Border checking
        if self.x < -300 or self.x > 300:
            self.x = 0
            self.y = -300
            
        if self.y < -400:
            self.y = -400
        
        self.remainingTime = self.maxTime - round(time.time() - self.startingTime)
        
        # Out of time
        if self.remainingTime <= 0:
            player.lives -= 1
            self.goHome()
            
    def goHome(self):
        self.dx = 0
        self.x = 0
        self.y = -400
        self.maxTime = 60
        self.remainingTime = 60
        self.startingTime = time.time()
        
        if self.lives == 0:
            self.gameOver = True
               
class Dog(Pen):
    def __init__(self, x, y, width, height, image, dx):
        Pen.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400
            
# The wood logs
class Log(Pen):
    def __init__(self, x, y, width, height, image, dx):
        Pen.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400

class Hat(Pen):
    def __init__(self, x, y, width, height, image, dx):
        Pen.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400
            
                  
class Home(Pen):
    def __init__(self, x, y, width, height, image):
        Pen.__init__(self, x, y, width, height, image)
        self.dx = 0

class Timer():
    def __init__(self, maxTime):
        self.x = 200
        self.y = -375
        self.maxTime = maxTime
        self.width = 200
        
    def render(self, time, pen):
        pen.color("green")
        pen.pensize(5)
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        percent = time / self.maxTime
        dx = percent * self.width
        
        if dx < self.width // 2:
            pen.color('red')
            
        pen.goto(self.x-dx, self.y)
        pen.penup()
        
# Create objects
player = Player(0, -325, 40, 40, "cat.gif")
timer = Timer(60)

level_1 = [
    Dog(0, -275, 121, 40, "dogLeft.gif", -0.1),
    Dog(221, -275, 121, 40, "dogLeft.gif", -0.1),
    
    Dog(0, -225, 121, 40, "dogRight.gif", 0.1),
    Dog(221, -225, 121, 40, "dogRight.gif", 0.1),
    
    Dog(0, -175, 121, 40, "dogLeft.gif", -0.1),
    Dog(221, -175, 121, 40, "dogLeft.gif", -0.1),
    
    Dog(0, -125, 121, 40, "dogRight.gif", 0.1),
    Dog(221, -125, 121, 40, "dogRight.gif", 0.1),
    
    Dog(0, -75, 121, 40, "dogLeft.gif", -0.1),
    Dog(221, -75, 121, 40, "dogLeft.gif", -0.1),
    
    Log(0, 25, 161, 40, "log.gif", 0.2),
    Log(261, 25, 161, 40, "log.gif", 0.2),
    
    Log(0, 75, 161, 40, "log.gif", -0.2),
    Log(261, 75, 161, 40, "log.gif", -0.2),
    
    Hat(0, 125, 50, 40, "hat.gif", 0.15),
    Hat(255, 125, 50, 40, "hat.gif", 0.15),
    
    Hat(0, 175, 50, 40, "hat.gif", -0.15),
    Hat(255, 175, 50, 40, "hat.gif", -0.15),
    
    Log(0, 225, 161, 40, "log.gif", 0.2),
    Log(261, 225, 161, 40, "log.gif", 0.2)
    ]

homes = [
    Home(0, 275, 50, 50, "home.gif"), 
    Home(-100, 275, 50, 50, "home.gif"),
    Home(-200, 275, 50, 50, "home.gif"),
    Home(100, 275, 50, 50, "home.gif"),
    Home(200, 275, 50, 50, "home.gif")
    ]

# Create list of Pens
Pens = level_1 + homes
Pens.append(player)

# Keyboard binding
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

# Game over screen
pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.up()
def showGameOverScreen():
        pen2.color("red")
        pen2.goto(0, 0)
        pen2.write("Game Over", align="center", font=("Arial", 24, "normal"))
        pen2.goto(0, -50)
        pen2.write("Press Q to quit or R to restart", align="center", font=("Arial", 24, "normal"))
        wn.listen()
        wn.onkeypress(quitGame, "q")
        wn.onkeypress(restart, "r")

checkGameQuit = [0]
def quitGame():
    checkGameQuit[0] = 1
    
def restart():
    player.gameOver = False
    pen2.clear()

# Main
while not checkGameQuit[0]:    
    # Render
    for Pen in Pens:
        Pen.render(pen)
        Pen.update()
        
    # Render the timer
    timer.render(player.remainingTime, pen)
    
    # Render the lives
    pen.goto(-290, -375)
    pen.shape("smallCat.gif")
    for life in range(player.lives):
        pen.goto(-280 + (life * 30), -375)
        pen.stamp()
    
    # Check for collisions
    player.dx = 0
    player.collision = False
    for Pen in Pens:
        if player.isCollision(Pen):
            if isinstance(Pen, Dog):
                dogSound.play(1)
                player.lives -= 1
                player.goHome()
                break
            elif isinstance(Pen, Log):
                player.dx = Pen.dx
                player.collision = True
                break
            elif isinstance(Pen, Hat):
                player.dx = Pen.dx
                player.collision = True
                break
            elif isinstance(Pen, Home):
                homeSound.play()
                player.goHome()
                Pen.image = "homeCat.gif"
                player.catHome += 1
                break
                
    if player.y > 0 and player.collision != True:
        waterSound.play()
        player.lives -= 1
        player.goHome()

    # Made it home 5 times
    if player.catHome == 5:
        player.goHome()
        player.catHome = 0
        for home in homes:
            home.image = "home.gif"
        
    # Player runs out of lives
    if player.lives == 0:
        player.goHome()
        player.catHome = 0
        for home in homes:
            home.image = "home.gif"
        player.lives = 3
    
    if player.gameOver:
        showGameOverScreen()
        
    # Update screen
    wn.update()
    pen.clear()

    

