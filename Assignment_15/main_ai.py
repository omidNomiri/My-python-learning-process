import arcade
from snake import Snake
from food import Meat

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height = 600,title = "AI snake game")
        arcade.set_background_color(arcade.color.KHAKI)
        self.meat = Meat(self)
        self.snake = Snake(self)
        self.snake.score = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"score: {self.snake.score}",10,10)
        self.snake.draw()
        self.meat.draw()

        arcade.finish_render()

    def on_update(self, delta_time: float):

        if arcade.check_for_collision(self.snake, self.meat):
            self.snake.eat_meat(self.meat)
            self.meat = Meat(self)

        self.snake.move_with_ai(self.meat.center_x, self.meat.center_y)
        self.snake.move()

if __name__ == "__main__":
    game = Game()
    arcade.run()
