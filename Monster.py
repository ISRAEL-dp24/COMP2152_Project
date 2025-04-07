from Character import Character

def initialize_monster(selected_opponent):
    if selected_opponent == "Monster":
        return Character("Monster", health_points=20, combat_strength=5)
    elif selected_opponent == "Demon":
        return Character("Demon", health_points=18, combat_strength=6)
    elif selected_opponent == "Titan":
        return Character("Titan", health_points=30, combat_strength=4)
    elif selected_opponent == "Ghost Knight":
        return Character("Ghost Knight", health_points=15, combat_strength=8)