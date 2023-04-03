# CS515_PROJECT_ADVENTURE_GAME

## Name : Sai Bandla

> CWID: 20011577

## Stevens login:

> sbandla@stevens.edu

## Github Repo:

> https://github.com/saipranav789/CS515_PROJECT_ADVENTURE_GAME

## Hours Spent on project:

> Around 12 hours but I spent 8-9 hours just debugging so I can match the autograder.

## How I tested my code:

> I tested my code by creating a map file called prof.map which contains the vanilla map for the testing of the base line functionality of this project. I further used the autograder to match the outputs for the given verbs

## any bugs or issues I could not resolve:

> None I was able to resolve all issues

## an example of a difficult issue or bug and how you resolved

> A issue i resolved while making this project is preventing a infinity loop situation by using proper break and pass statements while running the game.

## a list of the three extensions I have chosen to implement, with appropriate detail on them for the CAs to evaluate them

> ### directional shortcuts/abbreviations:
>
> > Instead of using the go verb i.e: "go east" the player can just type the first letter i.e: "e" to move in that direction.

    Test Sample:
    > A white room

    You are in a simple room with white walls.

    Exits: north east

    What would you like to do? e
    You go east.

    > A red room

    This room is fancy. It's red!

    Items: rose

    Exits: north west

    What would you like to do? w
    You go west.

    > A white room

    You are in a simple room with white walls.

    Exits: north east

    What would you like to do? nw
    There's no way to go northwest.
    What would you like to do?

> ### drop verb:
>
> > I have implemented a drop verb where the player can drop items from their inventory into the room they are currently in.
> > i.e drop [item name] **example: drop clear stone**
> > If a item is dropped the item is added to the room's items after it is removed from the inventory

    Test Sample:
    > A red room

    This room is fancy. It's red!

    Items: rose

    Exits: north west

    What would you like to do? get rose
    You pick up the rose.
    What would you like to do? inv
    Inventory:
    rose
    What would you like to do? look
    > A red room

    This room is fancy. It's red!

    Exits: north west

    What would you like to do? drop rose
    You drop the rose.
    What would you like to do? look
    > A red room

    This room is fancy. It's red!

    Items: rose

    Exits: north west

    What would you like to do?

> ### help verb:
>
> > I have implemented a help verb which displays all the inputs the user can give in the game and the what each input does.

    What would you like to do? help
    You can run the following commands:

    go : this verb is used to move in a direction listed in room exits
    (example: go east)
    Player can also directly enter the direction without using go i.e e for east to go east

    get : used to pick up a item (example: get life orb)

    look : used to understand where the player is currently

    inventory : used to check the items in inventory

    help : provides the commands a player can use in the game

quit : used to exit/end the game

## how to play game:

> The setting of the game takes place in a fantasy magical land which is suffering because of demon lord leviathan (The villain of the story). You are a warrior set out to defeat the demon lord. But as you are now you dont have enough magical powers to defeat him.

> Inorder to defeat him you need to navigate through the game_map and find 6 orbs scattered across the map. Only with the power of the 6 orbs the demon lord can be defeated. In the game you will come across other items which are of no use to defeat the demon lord. A player can carry only 6 items in his inventory. You must only pick up the orbs and drop useless items you pick up on your journey.

## winning / losing conditions:

> The player will navigate blindly through out the map. You will not know what comes next when you select a direction to go. If the player happens to enter the demon lord's dojo before collecting the 6 orbs. The player will be killed by the demon lord instantly causing the player to lose. The player will be given the option to either restart the game from the starting room or quit the game. There will be many items to pick up all over the map but the player must pick up only the orbs and have all 6 orbs in their inventory before going to the demon lords dojo.

> The player's inventory has the capacity to hold only 6 items and they are ment for the orbs. If the player has other items in his inventory he must drop them to be able to pick up other items. These other items are just distractions and will not help in defeating the demon lord.

> If the player has all 6 orbs in their inventory when they enter the demon lord's dojo they win!

## Game Map:

<img width="724" alt="Game_Map" src="https://user-images.githubusercontent.com/113039239/229385223-032f4857-7f0b-450b-8214-6e91c4c47f50.png">

> > Fastest way to lose: go east twice

> > Fastest way to win: There is no fast way to win you must navigate to every room except the dojo using the above map for reference and pick up all orbs.

# Running the game:

### enter the below command in the terminal:

> python3 adventure.py orb6.map

### pick up the following orbs scattered across the map

> "clear orb", "shadow orb" , "time orb", "volcanic orb", "life orb", and "earth orb"

### head to the dojo

> If you have the above 6 orbs you reach the dojo you will win.
> If you dont have the non orb items in your inventory or less than 6 orbs you will lose. You will then be given a chance to restart from liminal space again.(play again)
