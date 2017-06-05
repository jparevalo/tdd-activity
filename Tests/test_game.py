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

    def test_record_roll__given_10_knocked_pins__does_not_raise_any_exception(self):
        # Arrange
        knocked_pins = 10
        bowling_game = Game()
        raised_exception = False
        expected_result = False

        # Act
        try:
            bowling_game.record_roll(num_pins_knocked=knocked_pins)
        except:
            raised_exception = True

        # Assert
        self.assertEqual(expected_result, raised_exception)

    def test_record_roll__given_0_knocked_pins__does_not_raise_any_exception(self):
        # Arrange
        knocked_pins = 0
        bowling_game = Game()
        raised_exception = False
        expected_result = False

        # Act
        try:
            bowling_game.record_roll(num_pins_knocked=knocked_pins)
        except:
            raised_exception = True

        # Assert
        self.assertEqual(expected_result, raised_exception)

    def test_get_score__given_a_full_game_with_no_spares_or_strikes__return_correct_score(self):
        # Arrange
        any_number = 2
        bowling_game = Game()
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        expected_score = 40

        # Act
        final_score = bowling_game.get_score()

        # Assert
        self.assertEqual(expected_score, final_score)

    def test_get_score__given_a_full_game_with_one_spare_in_the_middle__return_correct_score(self):
        # Arrange
        any_number = 2
        number_for_spare = 8
        bowling_game = Game()
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=number_for_spare)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        expected_score = 48

        # Act
        final_score = bowling_game.get_score()

        # Assert
        self.assertEqual(expected_score, final_score)

    def test_get_score__given_a_full_game_with_one_strike_in_the_middle__return_correct_score(self):
        # Arrange
        any_number = 2
        number_for_strike = 10
        bowling_game = Game()
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        bowling_game.record_roll(num_pins_knocked=any_number)
        expected_score = 50

        # Act
        final_score = bowling_game.get_score()

        # Assert
        self.assertEqual(expected_score, final_score)

    def test_get_score__given_a_full_game_with_only_strikes__return_correct_score(self):
        # Arrange
        number_for_strike = 10
        bowling_game = Game()
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        bowling_game.record_roll(num_pins_knocked=number_for_strike)
        expected_score = 300

        # Act
        final_score = bowling_game.get_score()

        # Assert
        self.assertEqual(expected_score, final_score)



