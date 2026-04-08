import arcade

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800,800,"HEROOOOOOOs")

    def on_draw(self):
        self.clear()
        arcade.draw_text("Heloo!",700,100,arcade.color.WHITE,24)

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()

    