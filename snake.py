from turtle import Turtle

# constant
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_HEADING = [0, 90, 180, 270]
SQUARE_SIZE = 20


class Snake:

    def __init__(self):
        self.head = Turtle()
        self.segment_square = []
        self.create_snake()
        # self.score = 0

    def create_snake(self):
        """It Creates Initial snake with initial position."""
        for position in INITIAL_POSITION:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segment_square.append(segment)
            
        self.head = self.segment_square[0]

    def update_new_portion_in_snake(self):
        [x_cor, y_cor] = [self.segment_square[-1].xcor(), self.segment_square[-1].ycor()]
        # print(x_cor, y_cor)
        if self.segment_square[0].heading() == 90:
            y_cor -= 20
        elif self.segment_square[0].heading() == 270:
            y_cor += 20
        elif self.segment_square[0].heading() == 0:
            x_cor -= 20
        else:
            x_cor += 20

        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto((x_cor, y_cor))
        self.segment_square.append(segment)

        # self.score += 1
        # print(self.score)

    def move(self):
        """It will move the snake forward by 20. i.e.
        position of 3rd square => position of 2nd.
        position of 2nd square => position of 1st.
        position of 1st will fd by 20"""
        
        segment_square = self.segment_square
        for seg in range(len(segment_square) - 1, 0, -1):
            x_cor = segment_square[seg - 1].xcor()
            y_cor = segment_square[seg - 1].ycor()
            segment_square[seg].goto(x_cor, y_cor)
        segment_square[0].fd(20)
        # self.head = (segment_square[0].xcor(), segment_square[0].ycor())

    def up(self):
        segment_square = self.segment_square
        if not segment_square[0].heading() == SNAKE_HEADING[3]:
            segment_square[0].setheading(SNAKE_HEADING[1])

    def down(self):
        segment_square = self.segment_square
        if not segment_square[0].heading() == SNAKE_HEADING[1]:
            segment_square[0].setheading(SNAKE_HEADING[3])

    def left(self):
        segment_square = self.segment_square
        if not segment_square[0].heading() == SNAKE_HEADING[0]:
            segment_square[0].setheading(SNAKE_HEADING[2])

    def right(self):
        segment_square = self.segment_square
        if not segment_square[0].heading() == SNAKE_HEADING[2]:
            segment_square[0].setheading(SNAKE_HEADING[0])

    def check_out_of_screen(self):
        x_cor = self.head.xcor()
        y_cor = self.head.ycor()
        # print(f"going to {x_cor}, {y_cor}")
        if x_cor > 310:
            x_cor = -300
        elif x_cor < -310:
            x_cor = 300
        elif y_cor > 310:
            y_cor = -300
        elif y_cor < -310:
            y_cor = 300

        self.head.goto(x_cor, y_cor)




