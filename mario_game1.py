import arcade 
from constants12 import *
from player1 import Player
from platform import Platform1

class MarioGame(arcade.Window):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.SKY_BLUE
        self.player = None
        self.player_list = None
        self.platforms = None

    def setup(self):
        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.platforms = arcade.SpriteList(use_spatial_hash=True)
        self.create_level_1


    def on_draw(self):
        self.clear()
        self.platforms.draw()
        self.player_list.draw()

    def on_update(self):
        self.player.update()
        self.check_colisions()

    def on_key_press(self,key):
        if key == arcade.key.RIGHT:
            self.Player.move_right()
        elif key == arcade.key.LEFT:
            self.Player.move_left()
        elif key == arcade.key.UP:
            self.Player.jump()
        

    def on_key_release(self,key):
        if key in (arcade.key.RIGHT,arcade.key.LEFT):
            self.Player.stop_horizental()

    # platform(x,y,width,height)
    def create_level_1(self):
        level_lauout = [
            (400,20,800,40),  #ground 
            (200,150,120,20), # low,  left
            (400,300,150,20),   # mid,  right
            (650,450,100,20),    # high, middle
            (100,450,100,20)
        ]
        for x,y,w,h in level_lauout():
            plat = Platform1(x,y,w,h)
            self.platforms.append(plat)

    def check_colisions(self):
        hit_list = arcade.check_for_collision_with_list(self.player,self.platforms)
        if hit_list:
            for p in hit_list:
                if self.player.change_y < 0:
                    self.player.change_y = 0
                    self.player.center_y = p.center_y + p.height/2 + self.player.height/2
                    self.player.is_on_ground = True
                else:
                    self.player.is_on_ground = False

    def reset_level(self):
        self.player.reset()
        self.platforms.clear()
        self.create_level_1()


