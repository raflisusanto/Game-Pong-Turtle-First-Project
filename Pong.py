import turtle
import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("blue")
win.setup(width=800, height=600)
win.tracer()

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #maximum speed (animation)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #defaultnya 20x20 px
paddle_a.penup() #will not draw a line when it moves
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #maximum speed (animation)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #defaultnya 20x20 px
paddle_b.penup() #will not draw a line when it moves
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #maximum speed (animation)
ball.shape("circle")
ball.color("white")
ball.penup() #will not draw a line when it moves
ball.goto(0, 0)
ball.dx = 2 #dx = delta X
ball.dy = 2 #move 2 pixel jadi kalo dua duanya ada x,y berarti nanti gerak nya diagonal

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle() #di hide si turtle nya
pen.goto(0, 260) #letak scorenya
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal")) #font, fontsize, normal/bold/itallic

#Function
def paddle_a_up():
    y = paddle_a.ycor() #ycor -> returns the y coordinate
    y += 20
    paddle_a.sety(y) #set y to the new y

def paddle_a_down():
    y = paddle_a.ycor() #ycor -> returns the y coordinate
    y -= 20
    paddle_a.sety(y) #set y to the new y

def paddle_b_up():
    y = paddle_b.ycor()  # ycor -> returns the y coordinate
    y += 20
    paddle_b.sety(y)  # set y to the new y

def paddle_b_down():
    y = paddle_b.ycor()  # ycor -> returns the y coordinate
    y -= 20
    paddle_b.sety(y)  # set y to the new y

#Keyboard Binding
win.listen() # listen for keyboard inputs
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "e") #Up
win.onkeypress(paddle_b_down, "d") #Down

# while True => loop forever, win.update() => update screennya terus
# break => bisa break si loop nya

# Main game loop
while True:
    win.update()

    # Ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290) #this avoids certain types of problem
        ball.dy *= -1 #reverse the direction
        winsound.PlaySound("C:/Users/MSI/Documents/pythonPROJECT/Games Project/bounce.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("C:/Users/MSI/Documents/pythonPROJECT/Games Project/bounce.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 #back to center and reverse direction
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))

    # Paddle and ball collisions
    # Pokonya ini problem matematis, masalah kordinat. Ntar si ball harus mantul di area si paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <= paddle_b.ycor() + 50 and ball.ycor() >= paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("C:/Users/MSI/Documents/pythonPROJECT/Games Project/bounce.mp3", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <= paddle_a.ycor() + 50 and ball.ycor() >= paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("C:/Users/MSI/Documents/pythonPROJECT/Games Project/bounce.mp3", winsound.SND_ASYNC)