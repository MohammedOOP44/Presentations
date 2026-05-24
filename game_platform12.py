import arcade
from constants12 import PLATFORM_COLOR

class Platform(arcade.Sprite):
    def __init__(self,x:float,y:float,width:int,height:int):
        super().__init__()

        self.texture = arcade.make_soft_square_texture(
            size=50,
            color=PLATFORM_COLOR,
            outer_alpha=255
        )

        self.width    = width
        self.height   = height

        self.center_x = x
        self.center_y = y