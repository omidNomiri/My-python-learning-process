import arcade
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=480,height=720,title="on star")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.defender = Spaceship(self.width,self.height)
        self.enemy_list = []
        arcade.schedule(self.add_enemy, 3)

    def add_enemy(self, delta_time):
        new_enemy = Enemy(self.width, self.height)
        self.enemy_list.append(new_enemy)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

        self.defender.draw()
        for enemy in self.enemy_list:
            enemy.draw()

        for bullet in self.defender.bullet_list:
            bullet.draw()

    def on_key_release(self, symbol: int, modifiers: int):
        self.defender.change_x = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.defender.change_x = 1
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.defender.change_x = -1
        elif symbol == arcade.key.SPACE:
            self.defender.fire()

    def on_update(self, delta_time: float):
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.defender,enemy):
                print("Game Over")
                exit(0)
        
        for enemy in self.enemy_list:
            for bullet in self.defender.bullet_list:
                if arcade.check_for_collision(bullet,enemy):
                    self.enemy_list.remove(enemy)
                    self.defender.bullet_list.remove(bullet)

        self.defender.move()

        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.defender.bullet_list:
            bullet.move()

        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)

        for bullet in self.defender.bullet_list:
            if bullet.center_y < 0:
                self.defender.bullet_list.remove(bullet)

        

window = Game()
arcade.run()
