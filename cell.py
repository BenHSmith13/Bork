def description():
    return 'You awake in a dimly lit brick cell. There is a barred window to the North, and bars to the south. ' \
           'Against the bars lies a slumped over body'


def go(direction):
    if direction == 'north':
        print('The view out the window is pretty bland')
        return {
            'floor': 1,
            'room': 'cell'
        }
    elif direction == 'east':
        print('This wall is made of faded bricks')
        return {
            'floor': 1,
            'room': 'cell'
        }
    elif direction == 'south':
        print('The door is made of strong iron. There is a body slumped aginst the other side of this door')
        return {
            'floor': 1,
            'room': 'cell'
        }
    elif direction == 'west':
        print('someone must have broken one of the bricks')
        return {
            'floor': 1,
            'room': 'cell'
        }
    else:
        print('Whait, what?')
        return {
            'floor': 1,
            'room': 'cell'
        }


interactables = {
    'body': {
        'inspect': 'You inspect the body, he is dead. You find a key attached to his belt',
        'can_take': False,
        'can_move': False
    },
    'key': {
        'inspect': 'It seems to be made of the same metal as the bars',
        'take' : 'You pick up the key',
        'can_take': True,
        'can_move': False
    },
    'brick': {
        'inspect': '',
    }
}
