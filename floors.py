import _floor1


def get_floor(floor):
    floors = {
        '1': _floor1
    }
    return floors[str(floor)]
