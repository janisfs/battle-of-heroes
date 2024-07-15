import random


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            self.display_health()

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break
            elif not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

    def display_health(self):
        print(f"{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")
        print()
