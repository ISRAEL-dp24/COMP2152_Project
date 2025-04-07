class Character:

    def __init__(self, name, combat_strength, health_points):
        self._combat_strength = combat_strength
        self._health_points = health_points
        self.name = name

    def attack(self, opponent):
        damage = self._combat_strength
        opponent.health_points -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def defend(self, damage):
        self._health_points = max(0, self._health_points - damage)
        print(f"{self.name} defends and loses {damage} health points!")
    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 0:
            self._combat_strength = value
        else:
            raise ValueError("Combat strength cannot be negative!")

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self._health_points = value
        else:
            raise ValueError("Health points cannot be negative!")

    def __del__(self):
        print("The Character object is being destroyed by the garbage collector")