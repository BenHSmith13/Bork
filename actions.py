
def perform_action(command, room, update_position, add_to_inventory):
    # command is a tuple that looks like this ('inspect', 'body')
    action = command[0]
    subject = command[1]

    if action == 'travel':
        move(subject, room, update_position)
        return
    if action == 'inspect':
        inspect(subject, room)
        return
    if action == 'take':
        take(subject, room, add_to_inventory)
        return
    if action == 'drop':
        return
    if action == 'interact':
        return


def move(direction, room, update_position):
    directions = ['north', 'east', 'south', 'west', 'up', 'down']
    if direction not in directions:
        print('How do I even do that?')
        return
    update_position(room.go(direction))


def inspect(subject, room):
    if subject in room.interactables:
        item = room.interactables[subject]
        print(item['inspect'])
    else:
        print('what is that?')


def take(subject, room, add_to_inventory):
    if subject in room.interactables:
        item = room.interactables[subject]
        print(item['take'])
        add_to_inventory({item['name']: item})
    else:
        print('I cant take that')
