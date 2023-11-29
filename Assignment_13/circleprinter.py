import arcade

class circle_on_cube(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="on star")
        self.circle_width = 30    
        self.circle_height = 30    
        self.RED = arcade.color.RED
        self.BLUE = arcade.color.BLUE

    def draw_circle(self, x, y, color):
        arcade.draw_circle_filled(x, y, 10, color)

    def on_draw(self):
        arcade.start_render()

        for i in range(0, self.width, self.circle_width):
            for j in range(0, self.height, self.circle_height):
                if (i // self.circle_width % 2 == j // self.circle_height % 2):
                    color = self.RED 
                else:
                    color = self.BLUE

                self.draw_circle(i + self.circle_width, j + self.circle_height, color)

printer = circle_on_cube()
arcade.run()
