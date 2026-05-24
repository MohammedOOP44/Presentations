from constants12 import (GRAVITY,MOVE_SPEED,JUMP_SPEED,PLAYER_SIZE)
import arcade
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(
            ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        )
        self.scale = 0.5

        # Starting position (set again in reset())
        self.center_x = 100
        self.center_y = 200

        # Velocity
        self.change_x = 0
        self.change_y = 0

        # State flags
        self.is_on_ground = False

    def update(self):
        self.apply_gravity()
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_y < PLAYER_SIZE // 2:
            self.center_y = PLAYER_SIZE // 2
            self.change_y = 0
            self.is_on_ground = True 


    def apply_gravity(self):
        if not self.is_on_ground:
            self.change_y -= GRAVITY 


    def move_left(self):
        self.change_x = -MOVE_SPEED

    def move_right(self):
        self.change_x = MOVE_SPEED

    def jump(self):
        if self.is_on_ground:
            self.change_y = JUMP_SPEED 
            self.is_on_ground = False

    def stop_horizental(self):
        self.change_x = 0

    def reset(self):
        self.center_x = 100
        self.center_y = 200
        self.change_x = 0
        self.change_y = 0
        self.is_on_ground = False

    

