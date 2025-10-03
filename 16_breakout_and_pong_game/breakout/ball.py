import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 10
        self.height = 10
        self.center_x = game.width//2
        self.center_y = 300
        self.change_x = random.choice([1, -1])
        self.change_y = -1
        self.radius = 12
        self.speed = 3
        self.color = arcade.color.UA_RED

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
