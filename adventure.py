
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
with open(filename, "r") as f:
    game_map = json.load(f)


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
        print(f"items : {items}")


def handle_input(input_str):
    input_str = input_str.lower().strip()
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print(input_str)
    print('@@@@@@@@@@@@@@@@@@@@@@')

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
        print("""
        You can run the following commands:
        go 
        get 
        look 
        inventory 
        quit 
        help 
        """)
    else:
        print('I don\'t understand.')


# demon lord ascii art
demon = """
    DEMON LORD LEVIATHAN
           ,^^^^^,
          #_   _#
         |a ` ` a|
         |  u  |         
         \  =  /
         |\___/|
  ___ ___/:     :\___ ___
/   '   \|` `'"`/|   `   \\
|        |      |        |
 \       \.  ,  /       /
  `\     /`~( )~`\     /'
    `\_/'   `"`   `\_/'  
"""


# Start the game loop
while True:
    print_location()
    if 'boss' in current_location:
        print(demon)
        if len(player_inventory) >= 6:
            print(
                "The Demon Lord attacked you! but you used the power of the 6 orbs and defeated him!!!\n")
            print("You Win!")
            break
        else:
            print(
                "The Demon Lord attacked you! since you didn't have the power of the 6 orbs he kills you :(")
            print("You Lose!")
            break
    try:
        action = input('What would you like to do? ')
        if re.match(re.compile(r'quit', re.IGNORECASE), action.lower().strip()):
            break
        new_location = handle_input(action)
        if new_location:
            current_location = new_location

    except (KeyboardInterrupt, EOFError):
        print("\nUse 'quit' to exit.")
        pass


print("Good Bye!")
