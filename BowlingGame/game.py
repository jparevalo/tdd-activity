
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
            raise InvalidNumberError("The number must be between 0 and 10")
        elif self._roll_number % 2 == 0:  # Inside turn
            self._turn_score += num_pins_knocked
            if self._last_roll + num_pins_knocked == 10:
                self._handle_spare(knocked_pins=num_pins_knocked)
            else:
                self._game_score[self._turn_number] = self._turn_score
            if self._in_strike:
                self._previous_turn_score += num_pins_knocked
            self._roll_number += 1
            self._turn_number += 1
        else:  # New turn
            self._first_turn_roll(knocked_pins=num_pins_knocked)

    def _first_turn_roll(self, knocked_pins):
        self._turn_score = knocked_pins
        if self._in_spare:
            self._handle_spare(knocked_pins=knocked_pins)
        elif self._in_strike:
            self._handle_strike(knocked_pins=knocked_pins)
        if knocked_pins == 10:
            self._handle_strike(knocked_pins=knocked_pins)
        self._last_roll = self._turn_score
        self._roll_number += 1

    def _handle_spare(self, knocked_pins):
        if self._roll_number % 2 == 0:
            self._in_spare = True
            self._previous_turn_score = self._turn_score
        else:
            self._previous_turn_score += knocked_pins
            previous_turn = self._turn_number - 1
            self._game_score[previous_turn] = self._previous_turn_score
            self._in_spare = False
            self._previous_turn_score = 0

    def _handle_strike(self, knocked_pins):
        if self._roll_number % 2 == 0:
            self._previous_turn_score += knocked_pins
        else:
            if not self._in_strike:
                self._in_strike = True
                self._previous_turn_score = knocked_pins
            else:
                self._previous_turn_score += knocked_pins
                previous_turn = self._turn_number - 1
                self._game_score[previous_turn] = self._previous_turn_score
                self._in_strike = False
                self._previous_turn_score = 0

    def get_score(self):
        return sum(self._game_score)


class InvalidNumberError(Exception):
    pass