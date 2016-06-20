
def perform_action(command, room, update_position):
    action = command[0]
    subject = command[1]

    if action == 'travel':
        move(subject, room, update_position)
        return
    if action == 'inspect':
        return
    if action == 'take':
        return
    if action == 'drop':
        return


def move(direction, room, update_room):
    directions = ['north', 'east', 'south', 'west', 'up', 'down']
    if direction not in directions:
        print('How do I even do that?')
        return
    update_room(room.go(direction))
