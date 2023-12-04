import arcade
from bullet import Bullet
class Spaceship(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.change_x = 0
        self.change_y = 0
        self.center_x = width // 2
        self.center_y = height // 10
        self.width = 60
        self.height = 60 
        self.game_width = width
        self.speed = 15
        self.bullet_list = []

    def move(self):
        if self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

        elif self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
