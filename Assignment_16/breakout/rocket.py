import arcade

class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 80
        self.height = 20
        self.center_x = game.width//2
        self.center_y = 30
        self.change_x = 0
        self.change_y = 0
        self.color = arcade.color.REDWOOD
        self.speed = 3
        self.score = 0
        self.health = 3

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
