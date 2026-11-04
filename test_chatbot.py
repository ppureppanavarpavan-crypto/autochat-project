# Rollback: delete test_chatbot.py if unit test suite is not desired
"""Unit tests for AutoChat chatbot."""

# Rollback: remove sys.path.insert in test_chatbot.py
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ChatBot import AutoChat
from Chat_response import CREATOR_NAME, RESPONSES


class TestAutoChat(unittest.TestCase):

    def setUp(self):
        self.bot = AutoChat()

    def test_clean_input_lowercase_and_whitespace(self):
        result = self.bot.clean_input("  HELLO   WORLD!  ")
        self.assertEqual(result, "hello world")

    def test_clean_input_apostrophe_contractions(self):
        result = self.bot.clean_input("What's up?")
        self.assertEqual(result, "whats up")

        result_unicode = self.bot.clean_input("How\u2019s it going?")
        self.assertEqual(result_unicode, "hows it going")

    def test_clean_input_punctuation(self):
        result = self.bot.clean_input("Python, AI & Machine-Learning!!")
        self.assertEqual(result, "python ai machine learning")

    def test_exit_command_detection(self):
        self.assertTrue(self.bot.is_exit_command("bye"))
        self.assertTrue(self.bot.is_exit_command("QUIT"))
        self.assertTrue(self.bot.is_exit_command("exit"))
        self.assertFalse(self.bot.is_exit_command("hello"))
        self.assertFalse(self.bot.is_exit_command("tell me about python"))

    def test_detect_category_known(self):
        self.assertEqual(self.bot.detect_category("hello there"), "greeting")
        self.assertEqual(self.bot.detect_category("tell me a joke"), "joke")
        self.assertEqual(self.bot.detect_category("what is python"), "python")

    def test_detect_category_unknown_fallback(self):
        self.assertEqual(self.bot.detect_category("completely random gibberish xyz123"), "unknown")

    def test_get_response_empty_input(self):
        response = self.bot.get_response("   ")
        self.assertIn("empty", response.lower())

    def test_get_response_exit(self):
        response = self.bot.get_response("bye")
        self.assertIn(response, RESPONSES["bye"]["responses"])

    def test_get_response_unrecognized_no_key_error(self):
        response = self.bot.get_response("qwertyuiop asdfghjkl")
        self.assertIn(response, RESPONSES["unknown"]["responses"])

    def test_get_response_contractions_matching(self):
        response = self.bot.get_response("What's up?")
        self.assertIn(response, RESPONSES["how_are_you"]["responses"])

    def test_creator_name_interpolated(self):
        creator_responses = RESPONSES["creator"]["responses"]
        for resp in creator_responses:
            self.assertIn(CREATOR_NAME, resp)

    def test_custom_responses_dict(self):
        custom = {
            "ping": {
                "keywords": ["ping"],
                "responses": ["pong"],
            },
            "unknown": {
                "keywords": [],
                "responses": ["default answer"],
            },
        }
        custom_bot = AutoChat(responses=custom)
        self.assertEqual(custom_bot.get_response("ping"), "pong")
        self.assertEqual(custom_bot.get_response("other"), "default answer")


if __name__ == "__main__":
    unittest.main()
