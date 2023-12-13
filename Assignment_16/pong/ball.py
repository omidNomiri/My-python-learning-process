import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 5
        self.height = 5
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x = random.choice([1,-1])
        self.change_y = random.choice([1,-1])
        self.radius = 15
        self.color = arcade.color.LIGHT_MEDIUM_ORCHID
        self.speed = 5

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)