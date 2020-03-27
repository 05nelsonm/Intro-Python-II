from room import Room
from player import Player
import textwrap

p = print

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Jackie", room['outside'])


def available_moves(position):
    list_of_moves = list()
    if position.n_to is not None:
        list_of_moves.append(("n", position.n_to))
    if position.e_to is not None:
        list_of_moves.append(("e", position.e_to))
    if position.s_to is not None:
        list_of_moves.append(("s", position.s_to))
    if position.w_to is not None:
        list_of_moves.append(("w", position.w_to))
    return list_of_moves


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    p("")
    p(f"    Current Room:     {player.position.name}")
    p(f"    Room Description: {player.position.description}")
    p("")
    p("    Available moves:")
    p("")

    moves = available_moves(player.position)
    for move in moves:
        p(f"        {move[0]} ~~~>  {move[1].name}:")
        p(f"{textwrap.indent(move[1].description, 20 * ' ')}")
        p("")

    while True:

        def check_move(choice):
            for i in range(len(moves)):
                if moves[i].__contains__(choice):
                    return True

            return False

        def move(player_direction_choice):
            if player_direction_choice == "n":
                player.position = player.position.n_to
            elif player_direction_choice == "e":
                player.position = player.position.e_to
            elif player_direction_choice == "s":
                player.position = player.position.s_to
            elif player_direction_choice == "w":
                player.position = player.position.w_to


        direction = input("Choose a direction [n/e/s/w] ('q' to quit): ")
        if check_move(direction):
            move(direction)
            break
        elif direction is "q":
            exit(0)
        else:
            p("    Direction unavailable. Please try again.")
