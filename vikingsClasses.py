class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return f'Odin Owns You All!'

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):

        import random

        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        s.receiveDamage(v.attack())

        if s.health <= 0:
            self.saxonArmy.remove(s)
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {s.damage} points of damage"

    def saxonAttack(self):

        import random

        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        
        v.receiveDamage(s.attack())

        if v.health <= 0:
            self.vikingArmy.remove(v)
            return f"{v.name} has died in act of combat"
        else:
            return f"{v.name} has received {v.damage} points of damage"
            

    def showStatus(self):

        if len(self.vikingArmy) == 0:
            return f'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) == 0:
            return f'Vikings have won the war of the century!'
        else:
            return f'Vikings and Saxons are still in the thick of battle.'

    


