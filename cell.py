def description():
    return 'You awake in a dimly lit brick cell. There is a barred window to the North, and bars to the south. ' \
           'Against the bars lies a slumped over body'


def interactables():
    body = {
        'text': 'You inspect the body, he is dead. You find a key attached to his belt',
        'can_take': False,
        'can_move': False
    }
    key = {
        'text': '',
        'can_take': False,
        'can_move': False
    }
    brick = {}

    return body, key, brick
