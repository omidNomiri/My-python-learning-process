import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.body_colors = [arcade.color.WOOD_BROWN, arcade.color.BROWN_NOSE]
        self.speed = 3
        self.score = 1
        self.body = []

    def draw(self):
        for i, part in enumerate(self.body):
            arcade.draw_circle_filled(part["x"], part["y"], 15, self.body_colors[i % len(self.body_colors)])
        arcade.draw_circle_filled(self.center_x, self.center_y, 15, arcade.color.DEEP_COFFEE)

    def move(self):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) >= self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def move_with_ai(self, center_x, center_y):
        if self.center_y > center_y:
            self.center_y -= self.speed

        if self.center_y < center_y:
            self.center_y += self.speed

        if self.center_x < center_x:
            self.center_x += self.speed
            
        if self.center_x > center_x:
            self.center_x -= self.speed

    def eat_meatloaf(self, meatloaf):
        del meatloaf
        self.score += 2

    def eat_meat(self, meat):
        del meat
        self.score += 1

    def eat_plant(self, plant):
        del plant
        self.score -= 1
        try:
            self.body.pop(0)
        except IndexError:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
