from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

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
def draw_geometric_figure(num_sides):
    '''
    draw a geometric figure
    '''
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
def draw_triangle_square_pentagon_hexagon_heptagon_octagon_nonagon_decagon():
    """
    draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
    """
    for shape_side_n in range(3, 11):
        tim.color(random.choice(colours))
        draw_geometric_figure(shape_side_n)


tim.shape("turtle") # set a turtle shape

#draw_square()
#draw_dashed_line()
#draw_triangle_square_pentagon_hexagon_heptagon_octagon_nonagon_decagon()


screen = Screen()
screen.exitonclick() # screen close only if you click him