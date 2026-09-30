import random
import re

from Chat_response import RESPONSES


class AutoChat:

    def __init__(self, name="AutoChat"):
        self.name = name
        self.responses = RESPONSES
        self.exit_keywords = self.responses["bye"]["keywords"]

    def clean_input(self, user_input):
        text = user_input.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text) 
        text = re.sub(r"\s+", " ", text).strip() 
        text = re.sub(r"'", "", text)            
        return text

    def _contains_word(self, text, keyword):
        pattern = r"\b" + re.escape(keyword) + r"\b"
        return re.search(pattern, text) is not None

    def detect_category(self, text):
        for category, data in self.responses.items():
            for keyword in data["keywords"]:
                if self._contains_word(text, keyword):
                    return category
        return

    def _is_exit(self, text):
        return any(self._contains_word(text, keyword) for keyword in self.exit_keywords)

    def is_exit_command(self, user_input):
        return self._is_exit(self.clean_input(user_input))

    def get_response(self, user_input):
        text = self.clean_input(user_input)

        if not text:
            return "It looks like your message was empty. Say 'hello' or type 'help'!"
        if self._is_exit(text):
            return random.choice(self.responses["bye"]["responses"])

        category = self.detect_category(text)

        return random.choice(self.responses[category]["responses"])