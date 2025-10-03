import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0,game.width)
        self.center_y = game.height + 15
        self.width = 60
        self.height = 60 
        self.angle = 180
        
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
        super().__init__(width=480,height=720,title="on star")
        arcade.set_background_color(arcade.color.DARK_VIOLET)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.defender = spaceship(self)
        self.enemy = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

        self.defender.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.defender.center_x -= self.defender.speed
        elif symbol == 100:
            self.defender.center_x += self.defender.speed

    def on_update(self, delta_time: float):
        self.enemy.center_y -= 1

window = Game()
arcade.run()
