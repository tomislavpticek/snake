from turtle import Turtle

MOVE_DIST = 20


class Snake:
    body = []

    def __init__(self):
        for var in range(0, 3):
            tmp_part = Turtle()
            tmp_part.penup()
            tmp_part.color("white")
            tmp_part.shape("square")

            if len(self.body) >= 1:
                tmp_part.setx(self.body[-1].xcor() - 20)
                print(tmp_part.xcor())
                self.body.append(tmp_part)
            else:
                self.body.append(tmp_part)
        self.snake_head = self.body[0]

    def food_collision(self, food):
        if self.snake_head.distance(food) < 15:
            food.move()
            self.grow()
            return True
        return False

    def border_collision(self):
        if self.snake_head.xcor() >= 280 or self.snake_head.xcor() <= -280 or self.snake_head.ycor() >= 280 or self.snake_head.ycor() <= -280:
            return True
        return False

    def body_collision(self):
        for part in self.body[1:]:
            if self.snake_head.distance(part) < 10:
                return True
        return False

    def grow(self):
        tmp_part = Turtle()
        tmp_part.penup()
        tmp_part.color("white")
        tmp_part.shape("square")
        self.body.append(tmp_part)

    def move_forward(self):
        for var in range((len(self.body) - 1), -1, -1):
            if var >= 1:
                self.body[var].setposition(x=self.body[var - 1].xcor(), y=self.body[var - 1].ycor())
            else:
                self.snake_head.forward(MOVE_DIST)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
