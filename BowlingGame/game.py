
class Game(object):
    _last_roll = 0
    _roll_number = 1
    _turn_number = 0
    _turn_score = 0
    _previous_turn_score = 0
    _game_score = [0] * 10
    _in_spare = False
    _in_strike = False

    def record_roll(self, num_pins_knocked):
        if num_pins_knocked not in range(0, 11):
            raise InvalidNumberError("The given number must be between 0 and 10")
        elif self._roll_number % 2 == 0:  # Inside turn
            self._turn_score += num_pins_knocked
            if self._last_roll + num_pins_knocked == 10:
                self._in_spare = True
                self._previous_turn_score = self._turn_score
            else:
                self._game_score[self._turn_number] = self._turn_score
            if self._in_strike:
                self._previous_turn_score += num_pins_knocked
            self._roll_number += 1
            self._turn_number += 1
        else:  # New turn
            self._turn_score = num_pins_knocked
            if self._in_spare:
                self._previous_turn_score += num_pins_knocked
                self._game_score[self._turn_number - 1] = self._previous_turn_score
                self._in_spare = False
                self._previous_turn_score = 0
            elif self._in_strike:
                self._previous_turn_score += num_pins_knocked
                self._game_score[self._turn_number - 1] = self._previous_turn_score
                self._in_strike = False
                self._previous_turn_score = 0
            if num_pins_knocked == 10:
                self._in_strike = True
                self._previous_turn_score = num_pins_knocked
            self._last_roll = self._turn_score
            self._roll_number += 1

    def get_score(self):
        return sum(self._game_score)



class InvalidNumberError(Exception):
    pass