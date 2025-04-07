from Character import Character

def initialize_hero(selected_character):
    if selected_character == "Hero":
        return Character("Hero", health_points=20, combat_strength=5)
    elif selected_character == "Mage":
        return Character("Mage", health_points=15, combat_strength=6)
    elif selected_character == "Beast":
        return Character("Beast", health_points=25, combat_strength=4)
    elif selected_character == "Assassin":
        return Character("Assassin", health_points=18, combat_strength=7)