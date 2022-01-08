from turtle import Screen, Turtle, left
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#constants 
LEFT_X = -370
RIGTH_X = 370

#creating the screen

screen = Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

#turn off the animation
screen.tracer(0)

# create left and right paddle
right_paddle = Paddle(cord_x=RIGTH_X, cord_y=0)
left_paddle  = Paddle(cord_x=LEFT_X, cord_y=0)

#create the left scoreboard
scoreboard = Scoreboard()

# create a ball
ball = Ball()

#the screen will  listen to the events
# and the function will execute 
screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    #this controls the movement of the ball
    ball.move()
    

    #detect collision with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()
    
    # detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
       
    # detect Right paddle misses
    if ball.xcor() > 400:
        scoreboard.update_left_score()
        ball.reset_position()
       

    #detect Left paddle misses
    if ball.xcor() < -400:
        scoreboard.update_right_score()
        ball.reset_position()

       







#exit the screen once everything is done
screen.exitonclick()
