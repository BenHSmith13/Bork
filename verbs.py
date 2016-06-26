verbs = {
    "go": 'travel',
    "travel": 'travel',
    'proceed': 'travel',

    'grab': 'take',
    'take': 'take',

    'drop': 'drop',

    'look': 'inspect',
    'inspect': 'inspect',
    'search': 'inspect',
    'interact': 'interact',
    'use': 'interact',
    'push': 'interact',
    'pull': 'interact',
    'tuch': 'interact',
    'open': 'interact',
    'close': 'interact'

}


def get_action(verb):
    if verb in verbs:
        return verbs[verb]
    else:
        return 'bad_verb'
