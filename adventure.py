
import json
import sys
import re

# check if the command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python3 program_name.py [map_file]")
    sys.exit()

# get the file name from the command line argument
filename = sys.argv[1]

# read the JSON data from the file
game_map = json.load(open(filename, "r"))

restart_map = game_map
player_inventory = []

# Set the starting location
start_location = game_map[0]
current_location = game_map[0]


def print_location():
    print(f"> {current_location['name']}")
    print(f"\n{current_location['desc']}")
    if "items" in current_location and len(current_location["items"]) > 0:
        items_in_room = current_location["items"]
        items = ", ".join(items_in_room)
        print(f"\nItems: {items}")
    print(f"\nExits: {' '.join(current_location['exits'].keys())}\n")


# Handling user input


def handle_input(input_str):
    input_str = input_str.lower().strip()

    valid_verb_dict = {"go": "this verb is used to move in a direction listed in room exits \n(example: go east) \nPlayer can also directly enter the direction without using go i.e e for east to go east", "\nget": "used to pick up a item (example: get life orb)",
                       "\nlook": "used to understand where the player is currently", '\ninventory': "used to check the items in inventory", '\nhelp': "provides the commands a player can use in the game", '\nquit': "used to exit/end the game"}

    if input_str.startswith('go'):
        direction = input_str[3:]
        if len(direction) == 0:
            print("Sorry, you need to 'go' somewhere.")
        else:
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")
    # implementing directions as verbs extension
    elif len(input_str) == 1:
        if input_str.startswith('e'):
            direction = 'east'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('w'):
            direction = 'west'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('n'):
            direction = 'north'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")

        elif input_str.startswith('s'):
            direction = 'south'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")
    elif len(input_str) == 2:  # ne nw se sw
        if input_str.startswith('ne'):
            direction = 'northeast'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('nw'):
            direction = 'northwest'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('se'):
            direction = 'southeast'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")

        elif input_str.startswith('sw'):
            direction = 'southwest'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print(f'You go {direction}.\n')
                return new_location
            else:
                print(f"There's no way to go {direction}.")

    elif input_str.startswith('get'):
        item_name = input_str[4:]
        if len(player_inventory) == 6:
            print("You cannot carry more than 6 items in your inventory")
            pass
        elif len(item_name) == 0:
            print("Sorry, you need to 'get' something.")
        else:
            if 'items' in current_location and item_name in current_location['items']:
                current_location['items'].remove(item_name)
                player_inventory.append(item_name)
                print(f'You pick up the {item_name}.')
            else:
                print(f"There's no {item_name} anywhere.")
    elif input_str == 'inventory' or input_str == 'inv' or input_str == 'i':
        if len(player_inventory) == 0:
            print("You're not carrying anything.")
        else:
            inv_str = ", ".join(player_inventory)
            # print(f"Inventory:\n  {inv_str}")
            print("Inventory:")
            for item in player_inventory:
                print(f"  {item}")
    elif input_str.startswith("drop"):
        item_name = input_str[5:]
        if len(item_name) == 0:
            print("Sorry, you need to 'drop' something.")
        else:
            if item_name in player_inventory:
                if "items" in current_location:
                    current_location['items'].append(item_name)
                    player_inventory.remove(item_name)
                    print(f'You drop the {item_name}.')
                else:
                    current_location['items'] = [item_name]
            else:
                print(f"There's no {item_name} in inventory.\n")
    elif input_str.startswith("look"):
        print_location()
    elif input_str.startswith("help"):
        print("You can run the following commands: \n")
        for key, value in valid_verb_dict.items():
            print(key, ":", value)
    else:
        print('I don\'t understand that enter a valid command.')


# demon lord ascii art
demon_alive = """
    DEMON LORD LEVIATHAN
           ,^^^^^,
          #_   _#
         |a ` ` a|
         |  u    |         
         \  =   /
         |\___/|
  ___ ___/:     :\___ ___
/   '   \|` `'"`/|   `   \\
|        |      |        |
 \       \.  ,  /       /
  `\     /`~( )~`\     /'
    `\_/'   `"`   `\_/'  
"""
demon_ded = """
    DEMON LORD LEVIATHAN
           ,^^^^^,
          #_   _#
         |x ` ` x|
         |  u    |         
         \  ^   /
         |\___/|
  ___ ___/:     :\___ ___
/   '   \|` `'"`/|   `   \\
|        |      |        |
 \       \.  ,  /       /
  `\     /`~( )~`\     /'
    `\_/'   `"`   `\_/'  
"""
if filename == "orb6.map":
    print("""
    Gametitle: Orb6

    You are in the layer of the demon lord leviathan. His territory is big and unexplored. 
    Your objective is to defeat the demon lord,
    as his curse had been tormenting the land for a decade.
    But as you are now your powers are useless against him!

    You need to search his layers for the many orbs of power. You can only defeat the
    demon lord if you have the powers of 6 orbs. You must blindly navigate through the different rooms as it is unmapped.
    You must travel blindly on this lonely search for the orbs.
    If you happen to enter the room which the demon lord resides without the 6 orbs it will lead to certain defeat.

    You will start your journey at the entance of the layer.
    Be careful warrior the future of this land depends on you!

    (Use the help command warrior to see what you can do in this world.)
    """)
game_running = True
location_count = 0
# start the game loop
while game_running:
    if location_count == 0:
        print_location()
        location_count += 1
    if 'boss' in current_location:
        if len(player_inventory) == 6 and "clear orb" in player_inventory and "shadow orb" in player_inventory and "time orb" in player_inventory and "volcanic orb" in player_inventory and "life orb" in player_inventory and "earth orb" in player_inventory:
            print(demon_ded)
            print(
                "The Demon Lord attacked you! but you used the power of the 6 orbs and defeated him!!!\n")
            print("\nYou Win!")
            play_again = input(
                "\nDo you want to play again from the 1st room? \nPress Y to play again or any other key to quit ").lower().strip()
            if play_again == "y":
                game_map = restart_map
                player_inventory = []
                current_location = start_location
                print_location()
                pass
            else:
                break
        else:
            print(demon_alive)
            print(
                "The Demon Lord attacked you! since you didn't have the power of the 6 orbs he kills you :(")
            print("\nYou Lose!")
            play_again = input(
                "\nDo you want to play again from the 1st room? \nPress Y to play again or any other key to quit ").lower().strip()
            if play_again == "y":
                game_map = restart_map
                player_inventory = []
                current_location = start_location
                print_location()
                pass
            else:
                break

    try:
        action = input('What would you like to do? ')
        if re.match(re.compile(r'quit', re.IGNORECASE), action.lower().strip()):
            break
        new_location = handle_input(action)
        if new_location:
            current_location = new_location
            print_location()

    except (EOFError):
        print("\nUse 'quit' to exit.")
        pass


print("Goodbye!")
