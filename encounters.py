import random

def trigger_random_encounter(health_points, combat_strength, belt):
    print("\n--- A random event is happening... ---")
    
    encounter_options = ['Treasure', 'Trap', 'Wild Animal', 'Mysterious Stranger']
    encounter_weights = [0.3, 0.3, 0.3, 0.1]
    
    encounter = random.choices(encounter_options, weights=encounter_weights)[0]
    
    if encounter == 'Treasure':
        reward_options = ['health', 'combat', 'both']
        reward = random.choice(reward_options)
        
        if reward == 'health':
            health_points = min(20, health_points + 5)
            print("You found a magical fruit! +5 Health!")
        elif reward == 'combat':
            combat_strength = min(6, combat_strength + 1)
            print("You found an ancient weapon! +1 Combat Strength!")
        else:
            health_points = min(20, health_points + 3)
            combat_strength = min(6, combat_strength + 1)
            print("You found a hidden treasure! +3 Health, +1 Combat Strength!")
    
    elif encounter == 'Trap':
        damage = random.randint(1, 3)
        health_points = max(0, health_points - damage)
        print(f"You triggered a trap! You lose {damage} health.")
    
    elif encounter == 'Wild Animal':
        if health_points <= 2:
            print("You see a wild animal... but you're too weak to fight. You flee!")
        else:
            health_points = max(0, health_points - 2)
            print("A wild animal attacked you! You lose 2 health fighting it off.")
    
    elif encounter == 'Mysterious Stranger':
        if belt:
            print("A mysterious stranger offers you a deal...")
            
            # List comprehension to filter out unwanted items
            tradable_items = [item for item in belt if item not in ["Poison Potion", "Flimsy Gloves"]]
            
            if tradable_items:
                print(f"Tradeable items: {tradable_items}")
                trade_choice = input("Do you want to trade one item for a reward? (yes/no): ").lower()
                
                if trade_choice == 'yes':
                    chosen_item = input("Enter the item name to trade: ")
                    
                    if chosen_item in tradable_items:
                        belt.remove(chosen_item)
                        if health_points < 20:
                            health_points = min(20, health_points + 2)
                            print("The stranger heals you. +2 Health.")
                        else:
                            combat_strength = min(6, combat_strength + 1)
                            print("The stranger blesses your weapon. +1 Combat Strength.")
                    else:
                        print("That item isn't available for trade.")
                else:
                    print("You ignore the stranger and move on.")
            else:
                print("You have nothing the stranger wants.")
        else:
            print("A stranger appears but your belt is empty. They vanish into the shadows.")
    
    return health_points, combat_strength, belt