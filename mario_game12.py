# ──────────────────────────────────────────
#  mario_game.py  –  Student A (base layer)
#  Student B will EXTEND this file,
#  adding enemies, coins, UI, camera, etc.
# ──────────────────────────────────────────
from constants12 import SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE
from player12 import Player
from game_platform12 import Platform
import arcade


class Mario_Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.background_color = arcade.color.SKY_BLUE
        self.player = None
        self.player_list = None
        self.platforms = None

    def setup(self):
        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.platforms = arcade.SpriteList(use_spatial_hash=True)
        self.create_level_1()

        

    def on_draw(self):
        self.clear()
        self.platforms.draw()
        self.player_list.draw()

    def on_update(self, delta_time:float):
        self.player.update()
        self.check_collisions()

    def on_key_press(self,key,modifiers):
        if key == arcade.key.RIGHT:
            self.player.move_right()
        elif key == arcade.key.LEFT:
            self.player.move_left()
        elif key == arcade.key.UP:
            self.player.jump()
        

    def on_key_release(self,key,modifiers):
        if key in (arcade.key.RIGHT,arcade.key.LEFT):
            self.player.stop_horizontal()

#Platform(400, 20, 800, 40)
#         │    │    │    │
#         │    │    │    └── height = 40  → how TALL the platform is
#         │    │    └─────── width  = 800 → how WIDE the platform is
#         │    └──────────── y      = 20  → how HIGH from the bottom
#         └───────────────── x      = 400 → how FAR from the left

    def create_level_1(self):
        level_layout = [
            (400,20,800,40),    # ground
            (200,150,120,20),   # low,  left
            (400,300,150,20),   # mid,  right
            (650,450,100,20),    # high, middle
            (100,450,100,20)
        ]

        for x,y,w,h in level_layout:
            plat = Platform(x,y,w,h)
            self.platforms.append(plat)


    def check_collisions(self):
        hit_list = arcade.check_for_collision_with_list(self.player,self.platforms)
        if hit_list:
            for p in hit_list:
                if self.player.change_y <= 0 :
                    self.player.change_y = 0
                    self.player.center_y = p.center_y + p.height
                    self.player.is_on_ground = True
        else:
            self.player.is_on_ground = False 

            
    def reset_level(self):
        self.player.reset()
        self.platforms.clear()
        self.create_level_1()
        

    


        




    


    