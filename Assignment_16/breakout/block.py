import arcade

class Block(arcade.Sprite):
    def __init__(self, center_x, center_y, color):
        super().__init__()
        self.width = 50
        self.height = 20
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
