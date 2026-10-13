"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.    
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

while current_room != "exit":
    # 1. Display the current room
    print("You are in the", current_room)

    # 2. Prompt for a movement command or "exit"
    command = input("Enter a direction (north, south, east, west) or 'exit': ").lower()

    # 3. Branch for exit command
    if command == "exit":
        current_room = "exit"

    # 3. Branch for valid movement commands
    elif command in ["north", "south", "east", "west"]:
        # Check if the direction is valid from the current room
        if command in rooms[current_room]:
            # 4. Update the room after a valid movement
            current_room = rooms[current_room][command]
         else:
            print("You can't go that way.")

    # 3. Branch for invalid input
    else:
        print("Invalid command. Try again.")
        
# TODO: Run and debug all milestone cases in prototype/README.md.
print("You have exited the game.")
