# main.py
from hero import Hero
from game import Game


def main():
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name)
    computer = Hero("Компьютер")

    game = Game(player, computer)
    game.start()


if __name__ == "__main__":
    main()
