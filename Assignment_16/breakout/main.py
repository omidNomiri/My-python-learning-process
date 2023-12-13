import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 10
        self.height = 10
        self.center_x = game.width//2
        self.center_y = 300
        self.change_x = random.choice([1, -1])
        self.change_y = -1
        self.radius = 12
        self.speed = 3
        self.color = arcade.color.UA_RED

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

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

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=800, title="breakout")
        arcade.set_background_color(arcade.color.PINE_GREEN)
        self.player = Rocket(self)
        self.ball = Ball(self)
        self.block_list = arcade.SpriteList()

        for i in range(400, self.height-100, 50):
            for j in range(90, self.width-80, 80):
                new_block = Block(j, i,arcade.color.YELLOW_ROSE)
                new_block.center_x = j
                new_block.center_y = i
                self.block_list.append(new_block)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(250, 360, self.width-80, self.height, arcade.color.DARK_BLUE, 3)
        arcade.draw_text(f"score: {self.player.score}", (self.width//2)+30, self.height-30, arcade.color.BLACK, 18)
        arcade.draw_text(f"health: {self.player.health}", (self.width//2)-110, self.height-30, arcade.color.BLACK, 18)
        self.player.draw()
        self.ball.draw()
        for block in self.block_list:
            block.draw()

        if self.player.health == 0:
            arcade.draw_text("GAME OVER", (self.width//2)-95, self.height//2, arcade.color.RED, 24)
            self.player.change_x = 0
            self.player.change_y = 0
            self.ball.change_x = 0
            self.ball.change_y = 0
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.player.move()
        self.ball.move()
        
        if 50 >= self.ball.center_x or self.ball.center_x >= self.width - 50:
            self.ball.change_x *= -1

        if self.ball.center_y >= self.height - 50:
            self.ball.change_y *= -1

        if self.player.center_x <= 80:
            self.player.change_x = 0

        if self.player.center_x >= self.width -80:
            self.player.change_x = 0

        if arcade.check_for_collision(self.player, self.ball):
            self.ball.change_y *= -1

        for block in self.block_list:
            if arcade.check_for_collision(self.ball, block):
                self.player.score += 1
                self.block_list.remove(block)
                self.ball.change_y *= -1

        if self.ball.center_y < 0:
            self.player.health -= 1
            del self.ball
            self.ball = Ball(self)
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol== arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -1
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 1

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player.width < x < self.width - self.player.width:
            self.player.change_x = 0
            self.player.center_x = x

game = Game()
arcade.run()
