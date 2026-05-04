from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle") # set a turtle shape
tim.color("red") # change shape color

# repeat this 2 lines 4 times because is a square
for _ in range(4):
    tim.right(90) # rotate 90 degrees (turn right)
    tim.forward(100) # move down 100 steps


screen = Screen()
screen.exitonclick() # screen close only if you click him