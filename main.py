import sys

# this is the file that will hande which floor you are on
import floors

# This is the game state, your characters inventory, and your position in the world
inventory = ()
position = floors.get_floor(1).get_room('cell')


def main():
    print('Welcome to Bork')

    # The game loop, this will run over and over
    while True:
        # tells you the details of your room
        print(position.description())

        # gets a command from the user
        command = sys.stdin.readline()

        # parseCommand(command)


# runs the main function when you run the file
if __name__ == "__main__":
    main()
