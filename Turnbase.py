import random

class Character:
    def __init__(self, name, health, attack, defense, dodge_chance=0.2):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.dodge_chance = dodge_chance

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if random.random() > self.dodge_chance:
            actual_damage = max(0, damage)
            self.health -= actual_damage
            if self.health < 0:
                self.health = 0
            return actual_damage
        else:
            print(f"{self.name} dodged the attack!")
            return 0

    def attack_opponent(self, opponent):
        damage = max(0, self.attack - opponent.defense)
        opponent_damaged = opponent.take_damage(damage)
        return damage  
        
class Player(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def drop_loot(self):
        loot = random.choice(['Gold', 'Health Potion', 'Magic Scroll'])
        print(f"{self.name} dropped {loot}!")

def battle(player, enemy):
    print(f"Battle between {player.name} and {enemy.name} begins!")

    turn_count = 1

    while player.is_alive() and enemy.is_alive():
        print(f"=== Turn {turn_count} ===")

        # Hero (player) menyerang dragon (enemy)
        player_damage = player.attack_opponent(enemy)
        print(f"{player.name} attacks {enemy.name} and deals {player_damage} damage.")
        print(f"{enemy.name}'s Health: {enemy.health}")

        if not enemy.is_alive():
            break  # Keluar dari loop jika musuh sudah mati

        # Dragon (enemy) menyerang hero (player)
        enemy_damage = enemy.attack_opponent(player)
        print(f"{enemy.name} attacks {player.name} and deals {enemy_damage} damage.")
        print(f"{player.name}'s Health: {player.health}")

        turn_count += 1

    if player.is_alive():
        print(f"{player.name} wins the battle in {turn_count - 1} turns!")
        enemy.drop_loot()
    else:
        print(f"{enemy.name} wins the battle in {turn_count - 1} turns. Game over.")

# Membuat karakter pemain dan musuh
player = Player("Hero", 50, 12, 5)
enemy = Enemy("Dragon", 100, 10, 2)  

# Memulai pertempuran
battle(player, enemy)