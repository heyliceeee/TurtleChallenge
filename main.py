from turtle import Turtle, Screen


def draw_square():
    '''
    draw a square
    '''
    # repeat this 2 lines 4 times because is a square
    for _ in range(4):
        tim.right(90)  # rotate 90 degrees (turn right)
        tim.forward(100)  # move forward 100 steps


def draw_dashed_line():
    '''
    draw a dashed line
    '''

    #tim.right(90)  # rotate 90 degrees (turn right)

    # repeat this 50 times
    for _ in range(15):
        tim.forward(10)  # move forward 10 steps
        tim.penup() # no draw while moving
        tim.forward(10)  # move forward 10 steps
        tim.pendown() # draw while moving


tim = Turtle()
tim.shape("turtle") # set a turtle shape
tim.color("red") # change shape color

#draw_square()
draw_dashed_line()


screen = Screen()
screen.exitonclick() # screen close only if you click him