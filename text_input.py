import verbs


def parse_command(command):
    words = command.split(' ')

    verb = words[0]
    subject = words[1].rstrip()
    action = verbs.get_action(verb)
    if action == 'bad_verb':
        print("i don't know that verb")
        return
    return action, subject

