import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0,width)
        self.center_y = height + 15
        self.width = 60
        self.height = 60 
        self.angle = 180
        self.speed = 2

    def move(self):
        self.center_y -= 1
