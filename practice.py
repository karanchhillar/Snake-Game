from turtle import Turtle,Screen
import time
screen = Screen()
class Snake:

    def __init__(self):
        self.segment = []
        self.position = [(0,0),(-20,0),(-40,0)]



    def snake_length(self):
        
        screen.tracer(0)
        for i in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(self.position[i-1])
            self.segment.append(tim)
        screen.update()

        
    def move_snake(self):
        screen.tracer(0)
        time.sleep(0.1)
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.1)
            for j in range(len(self.segment)-1, 0 , -1):
                new_x = self.segment[j-1].xcor()
                new_y = self.segment[j-1].ycor()
                self.segment[j].goto( x=new_x , y=new_y )

            self.segment[0].fd(20)
        