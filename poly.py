
class Gun:
    def attack(self):
        print("shoot bullet!")

class Sword:
    def attack(self):
        print("swinig sword!")


class Player:
    def __init__(self):
        self.weapen = Gun()

    def use_weapen(self):
        self.weapen.attack()

player1 = Player()
player1.use_weapen()
player1.weapen = Sword()
player1.use_weapen()
