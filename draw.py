from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

### turtle crossing game ###

from turtle import Turtle,Screen
from player import Player
from car_maneger import Carmanger
from scoreboard import Scoreboard
import time
## normale all class call
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("pink")
player = Player()
car_manger = Carmanger()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up,"8")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.creat_cars()
    car_manger.move_cars()
    for car in car_manger.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_statrt()
        car_manger.level_up()        

screen.exitonclick()

## scoreboard maker ##

from turtle import Turtle, left

Font = ("courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.write(f"level:{self.level}",align="left",font=Font)
    def update_scoreboard(self):
        self.clear()
        self.write(f"level:{self.level}",align="left",font=Font)   
    def increase_level(self):
        self.level += 1    
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"game over",align="center",font=Font)    

## car manger ## 

from turtle import Turtle
import random
clors = ["red","orange","green","blue","purple"]
stating_move_distance  = 5
move_increment = 10

class Carmanger(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = stating_move_distance
    def creat_cars(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choices(clors))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)    
    def level_up(self):
        self.car_speed += move_increment        

## player manger ## 


from turtle import Turtle

starting_postion = (0,-280)
move_distance = 10
finish_line = 280

class Player(Turtle):
    def __init__(self):
       super().__init__()
       self.shape("turtle")
       self.color("blue")
       self.penup()
       self.goto(starting_postion)
       self.setheading(90)
    def move_up(self):
        self.forward(move_distance)  
    def go_to_statrt(self):
        self.goto(starting_postion)     
    def is_at_finish_line(self):
        if self.ycor()>finish_line:
            return True
        else :
            False    
