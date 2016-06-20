verbs = {
    "go": 'travel',
    "travel": 'travel',
}


def get_action(verb):
    if verb in verbs:
        return verbs[verb]
    else:
        return 'bad_verb'
