import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0,width)
        self.center_y = height + 15
        self.width = 60
        self.height = 60 
        self.angle = 180
        self.speed = 2

    def move(self):
        self.center_y -= 1

class spaceship(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.change_x = 0
        self.change_y = 0
        self.center_x = width // 2
        self.center_y = height // 10
        self.width = 60
        self.height = 60 
        self.game_width = width
        self.speed = 15

    def move(self):
        if self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

        elif self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=480,height=720,title="on star")
        arcade.set_background_color(arcade.color.DARK_VIOLET)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.defender = spaceship(self.width,self.height)
        self.list_of_enemy = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

        self.defender.draw()
        for enemy in self.list_of_enemy:
            enemy.draw()

    def on_key_release(self, symbol: int, modifiers: int):
        self.defender.change_x = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.defender.change_x = 1
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.defender.change_x = -1

    def on_update(self, delta_time: float):
        for enemy in self.list_of_enemy:
            if arcade.check_for_collision(self.defender,enemy):
                print("Game Over")
                exit(0)

        self.defender.move()

        for enemy in self.list_of_enemy:
            enemy.move()
    
        if random.randint(1,100) == 1:
            self.new_enemy = Enemy(self.width,self.height)
            self.list_of_enemy.append(self.new_enemy)

window = Game()
arcade.run()
