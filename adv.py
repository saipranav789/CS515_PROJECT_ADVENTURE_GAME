import os


# Display starting menu
def prompt():
    print("\t\tWelcome to my game\n\n\
You must collect all six items before fighting the boss.\n\n\
Moves:\t'go {direction}' (travel north, south, east, or west)\n\
\t'get {item}' (add nearby item to inventory)\n")

    input("Press any key to continue...")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = [
    {
        "name": "Liminal Space",
        "desc": "You are at a liminal space of a demon's layer",
        # {'North': 'Mirror Maze', 'South': 'Bat Cavern', 'East': 'Bazaar'},
        "exits":  {'North': 1, 'South': 2, 'East': 3},
        "items": ["White Stone"]
    },
    {
        "name": "Mirror Maze",
        "desc": "You are in a room with mirrored walls.",
        "exits": {'South': 0},  # {'South': 'Liminal Space'},
        "items": ["Clear Stone"]
    },
    {
        "name": "Bat Cavern",
        "desc": "This room looks like a dark cave with bats hanging from the ceiling.",
        # {'North': 'Liminal Space', 'East': 'Volcano'},
        "exits": {'North': 0, 'East': 6},
        "items": ["Shadow Stone"]
    },
    {
        "name": "Bazaar",
        "desc": "You are in a empty market which sells magical weapons.",
        # {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo'},
        "exits": {'West': 0, 'North': 4, 'East': 7},
        "items": ["Time stone"]
    },
    {
        "name": "Meat Locker",
        "desc": "This room is fancy. It's red!",
        # {'South': 'Bazaar', 'East': 'Quicksand Pit'},
        "exits": {'South': 3, 'East': 5},
        "items": ["Life orb"]
    },
    {
        "name": "Quicksand Pit",
        "desc": "You are in a room, with quick sand pits be careful!",
        "exits": {'West': 4},  # {'West': 'Meat Locker'},
        "items": ["Earth stone"]
    },
    {
        "name": 'Volcano',
        "desc": "You are in a active volcano and it is very hot!",
        "exits": {'West': 2},  # {'West': 'Bat Cavern'},
        "items": ["volcanic orb"]
    },
    {
        "name": 'Dojo',
        "desc": "You are in the demon lord's dojo and he attacks!",
        "exits": {'West': 3},  # {'West': 'Bazaar'},
        "Boss": 'Demon Lord Leviathan'
    },
]


# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = rooms[0]  # "Liminal Space"
current_room_name = current_room.get("name")

# Tracks last move
msg = ""

clear()
prompt()
# Gameplay loop
while True:

    clear()

    # Display player info
    print(
        f"You are in the {current_room_name}\nInventory : {inventory}\n{'-' * 27}")

    # Display msg
    print(msg)

    # Item indicator
    if "item" in current_room.keys():

        nearby_item = current_room["item"]

        if nearby_item not in inventory:

            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            else:
                print(f"You see a {nearby_item}")

    # Boss encounter
    if "Boss" in current_room.keys():

        if len(inventory) < 6:
            print(f"You lost a fight with {current_room['Boss']}.")
            break

        else:
            print(f"You beat {current_room['Boss']}!")
            break

    # Accepts player's move as input
    user_input = input("What would you like to do?\n")
    user_input = user_input.lower().strip()

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0]

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1]

        item = " ".join(item)

    # Moving between rooms
    if action == "go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"

        except:
            msg = "You can't go that way."

    # Picking up items
    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"

            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"

    # Exit program
    elif action == "quit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command"
