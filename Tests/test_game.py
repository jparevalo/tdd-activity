import unittest
from BowlingGame.game import Game
from BowlingGame.game import InvalidNumberError

class StringOperationTests(unittest.TestCase):
    def test_record_roll__given_a_negative_number__raise_invalid_number_exception(self):
        # Arrange
        any_negative_number = -1
        bowling_game = Game()

        # Assert
        with self.assertRaises(InvalidNumberError):
            # Act
            _ = bowling_game.record_roll(num_pins_knocked=any_negative_number)