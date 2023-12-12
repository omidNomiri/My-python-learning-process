import arcade
import random

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
        self.speed = 3

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

class Rocket(arcade.Sprite):
    def __init__(self, width, height, color, name):
        super().__init__()
        self.center_x = width
        self.center_y = height
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.color = color
        self.width = 30
        self.height = 60
        self.name = name
        self.score = 0

    def move(self):
        ...

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title="Pong")
        arcade.set_background_color(arcade.color.DEEP_CARROT_ORANGE)
        self.player1 = Rocket(40, self.height//2, arcade.color.BLUE_BELL, "player 1")
        self.player2 = Rocket(self.width-40, self.height//2, arcade.color.AQUA, "player 2")
        self.ball = Ball(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2, self.width-30, self.height-30, arcade.color.WHITE, 5)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height-30, arcade.color.WHITE, 3)
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        if self.ball.center_y < 30 or self.ball.center_y > self.height-30:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.player1,self.ball) or arcade.check_for_collision(self.player2,self.ball):
            self.ball.change_x *= -1
        
        self.ball.move()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player1.height < y < self.height-self.player1.height:
            self.player1.center_y = y

game = Game()
arcade.run()