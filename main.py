import sys
import floors

inventory = ()
position = floors.get_floor(1).get_room('cell')


def main():
    print('Welcome to Bork')

    while(True):
        print(position.description())
        command = sys.stdin.readline()
        print('you said: ' + command)
        # parseCommand(command)

if __name__ == "__main__":
    main()
