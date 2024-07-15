# hero.py
import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            damage = random.randint(10, 20)
            other.health -= damage
            print(f"{self.name} атаковал {other.name} и нанес {damage} урона.")

    def is_alive(self):
        return self.health > 0
