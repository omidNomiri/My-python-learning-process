import arcade

class Enemy:
    ...

class spaceship(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 10
        self.width = 60
        self.height = 60 
        self.speed = 15

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280,height=960,title="on star")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.defender = spaceship(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

        self.defender.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.defender.center_x -= self.defender.speed
        elif symbol == 100:
            self.defender.center_x += self.defender.speed


window = Game()
arcade.run()
