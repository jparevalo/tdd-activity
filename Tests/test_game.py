import unittest
from BowlingGame.game import Game
from BowlingGame.game import InvalidNumberError

class BowlingGameTests(unittest.TestCase):
    def test_record_roll__given_a_negative_number__raise_invalid_number_exception(self):
        # Arrange
        any_negative_number = -1
        bowling_game = Game()

        # Assert
        with self.assertRaises(InvalidNumberError):
            # Act
            _ = bowling_game.record_roll(num_pins_knocked=any_negative_number)

    def test_record_roll__given_a_number_bigger_than_10__raise_invalid_number_exception(self):
        # Arrange
        any_number_bigger_than_10 = 15
        bowling_game = Game()

        # Assert
        with self.assertRaises(InvalidNumberError):
            # Act
            _ = bowling_game.record_roll(num_pins_knocked=any_number_bigger_than_10)

    def test_record_roll__given_a_number_between_0_and_10__does_not_raise_any_exception(self):
        # Arrange
        any_valid_number = 7
        bowling_game = Game()
        raised_exception = False
        expected_result = False

        # Act
        try:
            bowling_game.record_roll(num_pins_knocked=any_valid_number)
        except:
            raised_exception = True

        # Assert
        self.assertEqual(expected_result, raised_exception)




