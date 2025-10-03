import arcade
from snake import Snake
from food import Meatloaf
from food import Meat
from food import Plant

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height = 600,title = "snake game")
        arcade.set_background_color(arcade.color.KHAKI)
        self.meatloaf = Meatloaf(self)
        self.meat = Meat(self)
        self.plant = Plant(self)
        self.snake = Snake(self)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.snake.change_x = -1
            self.snake.change_y = 0
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.snake.change_x = 1
            self.snake.change_y = 0

    def on_draw(self):
        arcade.start_render()
        
        if self.snake.score == 0:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
            self.snake.change_x = 0
            self.snake.change_y = 0

        if self.snake.center_x == self.width or self.snake.center_y == self.height:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
            self.snake.change_x = 0
            self.snake.change_y = 0
        
        if self.snake.center_x == 0 or self.snake.center_y == 0:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
            self.snake.change_x = 0
            self.snake.change_y = 0
  
        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
                arcade.draw_text("GAME OVER!", 150, 300, arcade.color.RED_DEVIL, 35)
                self.snake.change_x = 0
                self.snake.change_y = 0

        arcade.draw_text(f"score: {self.snake.score}",10,10)
        self.snake.draw()
        self.meatloaf.draw()
        self.meat.draw()
        self.plant.draw()

        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.meatloaf):
            self.snake.eat_meatloaf(self.meatloaf)
            self.meatloaf = Meatloaf(self)

        if arcade.check_for_collision(self.snake, self.meat):
            self.snake.eat_meat(self.meat)
            self.meat = Meat(self)

        if arcade.check_for_collision(self.snake, self.plant):
            self.snake.eat_plant(self.plant)
            self.plant = Plant(self)

if __name__ == "__main__":
    game = Game()
    arcade.run()
