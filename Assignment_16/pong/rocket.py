import arcade

class Rocket(arcade.Sprite):
    def __init__(self, width, height, color, name):
        super().__init__()
        self.center_x = width
        self.center_y = height
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.color = color
        self.width = 10
        self.height = 60
        self.name = name
        self.score = 0

    def move(self,ball, game):
        if self.center_y > game.height - self.height:
            self.center_y = game.height - self.height

        if self.center_y < 60:
            self.center_y = 60

        if self.center_y > ball.center_y:
            self.change_y = -1

        if self.center_y < ball.center_y:
            self.change_y = 1

        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
