
import json
import sys
import re

# check if the command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python program_name.py map_file.json")
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
    print("\n")
    print(current_location['name'])
    print("\n")
    print(current_location['desc'])
    print("\n")
    print('Exits:', ', '.join(current_location['exits'].keys()))
    print("\n")
    if "items" in current_location:
        items_in_room = current_location["items"]
        items = ", ".join(items_in_room)
        print(f"Items : {items}")


def handle_input(input_str):
    input_str = input_str.lower().strip()
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print(input_str)
    print('@@@@@@@@@@@@@@@@@@@@@@')

    # valid_verbs = ['go', 'get', 'look', 'inventory', 'help', 'quit']
    valid_verb_dict = {"go": "this verb is used to move in a direction listed in room exits \n(example: go east) \nPlayer can also directly enter the direction without using go i.e e for east to go east", "\nget": "used to pick up a item (example: get life orb)",
                       "\nlook": "used to understand where the player is currently", '\ninventory': "used to check the items in inventory", '\nhelp': "provides the commands a player can use in the game", '\nquit': "used to exit/end the game"}

    if input_str.startswith('go'):
        direction = input_str[3:]
        if len(direction) == 0:
            print("Sorry, you need to 'go' somewhere.\n")
        else:
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")
    # implementing directions as verbs extension
    elif len(input_str) == 1:
        if input_str.startswith('e'):
            direction = 'east'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")
        elif input_str.startswith('w'):
            direction = 'west'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")
        elif input_str.startswith('n'):
            direction = 'north'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")

        elif input_str.startswith('s'):
            direction = 'south'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")
    elif len(input_str) == 2:  # ne nw se sw
        if input_str.startswith('ne'):
            direction = 'northeast'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")
        elif input_str.startswith('nw'):
            direction = 'northwest'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")
        elif input_str.startswith('se'):
            direction = 'southeast'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")

        elif input_str.startswith('sw'):
            direction = 'southwest'
            if direction in current_location['exits']:
                new_location_id = current_location['exits'][direction]
                new_location = game_map[new_location_id]
                print('You go', direction + '.')
                return new_location
            else:
                print(f"There's no way to go {direction}.\n")

    elif input_str.startswith('get'):
        item_name = input_str[4:]
        if len(item_name) == 0:
            print("Sorry, you need to 'get' something.\n")
        else:
            if 'items' in current_location and item_name in current_location['items']:
                current_location['items'].remove(item_name)
                player_inventory.append(item_name)
                print('You pick up the', item_name + '.')
            else:
                print(f"There's no {item_name} anywhere.\n")
    elif input_str == 'inventory' or input_str == 'inv' or input_str == 'i':
        if len(player_inventory) == 0:
            print("You're not carring anything.\n")
        else:
            inv_str = ", ".join(player_inventory)
            print(f"Inventory:\n {inv_str}\n")
    elif input_str.startswith("drop"):
        item_name = input_str[5:]
        if len(item_name) == 0:
            print("Sorry, you need to 'drop' something.\n")
        else:
            if item_name in player_inventory:
                if "items" in current_location:
                    current_location['items'].append(item_name)
                    player_inventory.remove(item_name)
                    print('You drop the', item_name + '.')
                else:
                    current_location['items'] = [item_name]
            else:
                print(f"There's no {item_name} in inventory.\n")
    elif input_str.startswith("look"):
        pass
    elif input_str.startswith("help"):
        print("You can run the following commands: \n")
        # for i in valid_verbs:
        #     print(i, end="\n")

        for key, value in valid_verb_dict.items():
            print(key, ":", value)
    else:
        print('I don\'t understand that enter a valid command.')


# demon lord ascii art
demon = """
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

print("""
Gametitle: Orb6
    
You are in the layer of the demon lord leviathan. His layer is big and unexplored. Your objective is to defeat the demon lord as his curse had been tormenting the land for a decade.
But as you are now your powers are useless against him! 

You need to search his layers for the many orbs of power. You can only defeat the
demon lord if you have the powers of 6 orbs. You must blindly navigate his layer as it is unmapped. 

You must travel blindly on this lonely search for the orbs.
If you happen to enter the room which the demon lord resides without the 6 orbs it will lead to certain defeat. 

You will start your journey at the entance of the layer.
Be careful warrior the future of this land depends on you!
 """)
game_running = True
# start the game loop
while game_running:
    print_location()
    if 'boss' in current_location:
        print(demon)
        if len(player_inventory) >= 6:
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
        action = input('\nWhat would you like to do? ')
        if re.match(re.compile(r'quit', re.IGNORECASE), action.lower().strip()):
            break
        new_location = handle_input(action)
        if new_location:
            current_location = new_location

    except (KeyboardInterrupt, EOFError):
        print("\nUse 'quit' to exit.")
        pass


print("Good Bye!")
