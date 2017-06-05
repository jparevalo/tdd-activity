
class Game(object):
    def record_roll(self, num_pins_knocked):
        if num_pins_knocked not in range(0, 11):
            raise InvalidNumberError("The given number must be between 0 and 10")



class InvalidNumberError(Exception):
    pass