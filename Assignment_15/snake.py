import random
import arcade

class Fruit(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Assignment_15/apple.png")
        self.width = 36
        self.height = 36
        self.center_x = random.randint(10,game.width - 10)
        self.center_y = random.randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Poisoned_fruit():
    ...

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.color = arcade.color.GO_GREEN
        self.speed = 3
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 15, self.color)
        for part in self.body:
            arcade.draw_circle_filled(part["x"], part["y"], 15, self.color)

    def move(self):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food):
        del food
        self.score += 1
        

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height = 600,title = "snake game")
        arcade.set_background_color(arcade.color.KHAKI)
        self.food = Fruit(self)
        self.snake = Snake(self)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        if symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
    def on_draw(self):
        arcade.start_render()
        
        self.snake.draw()
        self.food.draw()

        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)
            self.food = Fruit(self)

if __name__ == "__main__":
    game = Game()
    arcade.run()
