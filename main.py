import sys
import os

# this is the file that will handle which floor you are on
import floors
import text_input
import actions
import messages

# This is the game state, your characters inventory, and your position in the world
inventory = []
position = {
    'floor': 1,
    'room': 'cell'
}


def update_position(new_position):
    global position
    position = new_position


def game_loop():
    while True:
        global position
        room = floors.get_floor(position['floor']).get_room(position['room'])
        # tells you the details of your room
        print(room.description())
        # gets a command from the user
        command = sys.stdin.readline()
        parsed_input = text_input.parse_command(command)
        print
        actions.perform_action(parsed_input, room, update_position)
        print


def main():
    messages.welcome()
    messages.bork()
    messages.mountains()
    print

    game_loop()


# runs the main function when you run the file. Just don't worry about this bit
if __name__ == "__main__":
    main()
