from turtle import Turtle,Screen, screensize
import time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.snake_length()
        

    def snake_length(self):
        screen = Screen()
        screen.tracer(0)
        
        
        self.position_list = [ (0,0) , (-20,0) , (-40,0) ]
        for position in self.position_list:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

        self.head = self.segment[0]
        screen.update()
        
    
    def move_snake(self):
        segment = self.segments
        screen = Screen()
        screen.tracer(0)
        game_is_on = True

        while game_is_on:
            
            screen.update()
            time.sleep(0.1)

            for seg in range(len(segment)-1, 0 , -1):
                new_x = segment[seg-1].xcor()
                new_y = segment[seg-1].ycor()
                segment[seg].goto( x=new_x, y=new_y)
            
            segment[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
          self.add_segment(position)  

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
            

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
        