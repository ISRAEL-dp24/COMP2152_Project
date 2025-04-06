import function
import random

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Define Boss Monster (Separate attributes for Boss)
boss_monster = {
    "name": "The Dark Lord",
    "combat_strength": 15,  # Stronger than regular monsters
    "health_points": 30,  # More health
}

def encounter_loot():
    loot = random.choice(loot_options)
    print("    ------------------------------------------------------------------")
    print(f"    |    You encounter loot! It's a {loot}!")
    belt.append(loot)  # Add loot to the player's belt
    print(f"    |    Your loot: {belt}")
    if loot == "Health Potion":
        print("    |    You can use this Health Potion before the fight with the monster!")
        print("    |    Choose to drink it if you'd like.")

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                           
     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                 
                                      """
    print(ascii_image4)
    power_roll = random.choice(list(monster_powers.keys()))

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(m_combat_strength) + " using the " + power_roll + " magic power")

    # Fight Sequence with regular monster
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
                # Loot drop after killing monster
                print("    ------------------------------------------------------------------")
                print("    |    The monster is defeated!")
                print("    |    Loot dropped!")
                belt = function.collect_loot("Normal", belt)
                print("    |    Your loot: ", belt)
                # Check if a health potion was dropped
                if "Health Potion" in belt:
                    print("    |    You drink a Health Potion before facing the boss!")
                    belt.remove("Health Potion")
                    health_points += 10  # Increase health by 10 (or desired value)
                    print("    |    Your health is now: ", health_points)


            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                health_points = function.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = function.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                m_health_points = function.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                    # Loot drop after killing monster
                    print("    ------------------------------------------------------------------")
                    print("    |    The monster is defeated!")
                    print("    |    Loot dropped!")
                    belt = function.collect_loot("Normal", belt)
                    print("    |    Your loot: ", belt)
                    # Check if a health potion was dropped
                    if "Health Potion" in belt:
                        print("    |    You drink a Health Potion before facing the boss!")
                        belt.remove("Health Potion")
                        health_points += 10  # Increase health by 10 (or desired value)
                        print("    |    Your health is now: ", health_points)

                else:
                    num_stars = 2

    # Check if player survived the regular monster fight
    if health_points > 0:
        # After defeating the regular monster, introduce boss monster
        print("    ------------------------------------------------------------------")
        print("    |    You encounter a BOSS MONSTER: " + boss_monster["name"] + "!!")
        print("    |    The boss monster has " + str(boss_monster["health_points"]) + " health points!")
        boss_health_points = boss_monster["health_points"]
        boss_combat_strength = boss_monster["combat_strength"]

        # Boss Fight Sequence
        while boss_health_points > 0 and health_points > 0:
            # Boss Fight Sequence
            print("    |", end="    ")

            input("Boss fight begins! (Press enter)")
            attack_roll = random.choice(small_dice_options)
            if not (attack_roll % 2 == 0):
                print("    |", end="    ")
                input("You strike the boss (Press enter)")
                boss_health_points = function.hero_attacks(combat_strength, boss_health_points)
                if boss_health_points == 0:
                    num_stars = 5  # High reward for defeating the boss
                    print("    ------------------------------------------------------------------")
                    print("    |    The Boss is defeated!")
                    print("    |    Loot dropped!")
                    belt = function.collect_loot("Boss", belt)  # Boss loot drop
                    print("    |    Your loot: ", belt)
                else:
                    print("    |", end="    ")
                    print("------------------------------------------------------------------")
                    input("    |    The boss strikes back (Press enter)!!!")
                    health_points = function.monster_attacks(boss_combat_strength, health_points)
                    if health_points == 0:
                        num_stars = 2  # Lower reward for dying to the boss
                    else:
                        num_stars = 3


            else:
                print("    |", end="    ")
                input("The boss strikes first (Press enter)")
                health_points = function.monster_attacks(boss_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    print("    |", end="    ")
                    print("------------------------------------------------------------------")
                    input("You strike the boss! (Press enter)")
                    boss_health_points = function.hero_attacks(combat_strength, boss_health_points)
                    if boss_health_points == 0:
                        num_stars = 5
                        print("    ------------------------------------------------------------------")
                        print("    |    The Boss is defeated!")
                        print("    |    Loot dropped!")
                        belt = function.collect_loot("Boss", belt)  # Boss loot drop
                        print("    |    Your loot: ", belt)

    else:
        print("    |    You have died. The boss encounter is skipped.")

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")

        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
