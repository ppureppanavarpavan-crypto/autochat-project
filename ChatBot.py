import random
import re

from Chat_response import RESPONSES


class AutoChat:

    def __init__(self, name="AutoChat", responses=None):
        # Rollback: restore previous __init__ definition without responses parameter
        self.name = name
        self.responses = responses if responses is not None else RESPONSES
        self.exit_keywords = self.responses.get("bye", {}).get("keywords", ["bye", "exit", "quit"])

    def clean_input(self, user_input):
        # Rollback: revert apostrophe stripping order to after punctuation replacement
        text = user_input.lower()
        text = re.sub(r"['\u2019]", "", text)
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def _contains_word(self, text, keyword):
        pattern = r"\b" + re.escape(keyword) + r"\b"
        return re.search(pattern, text) is not None

    def detect_category(self, text):
        # Rollback: revert detect_category to return bare None on mismatch
        for category, data in self.responses.items():
            if category == "unknown":
                continue
            for keyword in data.get("keywords", []):
                if self._contains_word(text, keyword):
                    return category
        return "unknown" if "unknown" in self.responses else None

    def _is_exit(self, text):
        return any(self._contains_word(text, keyword) for keyword in self.exit_keywords)

    def is_exit_command(self, user_input):
        return self._is_exit(self.clean_input(user_input))

    def get_response(self, user_input):
        # Rollback: revert get_response to direct self.responses[category]["responses"] indexing
        text = self.clean_input(user_input)

        if not text:
            return "It looks like your message was empty. Say 'hello' or type 'help'!"
        if self._is_exit(text):
            bye_responses = self.responses.get("bye", {}).get(
                "responses", ["Goodbye! Have a great day!"]
            )
            return random.choice(bye_responses)

        category = self.detect_category(text)

        if category and category in self.responses and self.responses[category].get("responses"):
            return random.choice(self.responses[category]["responses"])

        fallback_responses = self.responses.get("unknown", {}).get(
            "responses", ["Sorry, I didn't understand that. Type 'help' to see what I can do!"]
        )
        return random.choice(fallback_responses)
