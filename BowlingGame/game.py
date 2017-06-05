
class Game(object):
    def record_roll(self, num_pins_knocked):
        raise InvalidNumberError("The given number must be between 0 and 10")


class InvalidNumberError(Exception):
    pass