import unittest
from unittest.mock import patch
from armstrong_number import armstrong_numbers
from website_alarm import run_alarm, validate_time_format
from letter_evolution import guesser

class ExerciseTests(unittest.TestCase):
    def test_three_digit_armstrong_numbers(self):
        self.assertEqual(armstrong_numbers(), [153, 370, 371, 407])

    def test_invalid_alarm_time(self):
        self.assertFalse(validate_time_format("25:61"))
        self.assertTrue(validate_time_format("09:30"))

    @patch("website_alarm.webbrowser.open")
    @patch("website_alarm.time.sleep")
    @patch("website_alarm.time.strftime", side_effect=["09:29", "09:30"])
    def test_alarm_waits_instead_of_busy_looping(self, clock, sleep, browser):
        run_alarm("09:30")
        sleep.assert_called_once_with(1)
        browser.assert_called_once_with("https://google.com")

    @patch("builtins.input", return_value="cannot match spaces")
    def test_unreachable_target_is_rejected(self, user_input):
        with self.assertRaises(ValueError):
            guesser()

if __name__ == "__main__":
    unittest.main()
