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
        self.speed = 5

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

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title="Pong")
        arcade.set_background_color(arcade.color.DEEP_CARROT_ORANGE)
        self.player1 = Rocket(40, self.height//2, arcade.color.BLUE_BELL, "player 1")
        self.player2 = Rocket(self.width-40, self.height//2, arcade.color.AQUA, "player 2")
        self.ball = Ball(self)
        self.players = arcade.SpriteList()
        self.players.append(self.player1)
        self.players.append(self.player2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2, self.width-30, self.height-30, arcade.color.WHITE, 5)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height-30, arcade.color.WHITE, 3)
        arcade.draw_text(f"score player1:{self.player1.score}", 20, 30, arcade.color.BLACK, 18)
        arcade.draw_text(f"score player2:{self.player2.score}", self.width-190, 30, arcade.color.BLACK, 18)
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        if self.ball.center_y < 30 or self.ball.center_y > self.height-30:
            self.ball.change_y *= -1

        if arcade.check_for_collision_with_list(self.ball, self.players):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            self.player2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width:
            self.player1.score += 1
            del self.ball
            self.ball = Ball(self)
        
        self.ball.move()
        self.player2.move(self.ball, self)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player1.height < y < self.height-self.player1.height:
            self.player1.center_y = y

game = Game()
arcade.run()