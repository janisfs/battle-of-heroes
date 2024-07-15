class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атаковал {other.name} и нанес {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0
