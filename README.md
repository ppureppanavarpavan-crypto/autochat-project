# AutoChat

AutoChat is a lightweight, rule-based chatbot built in pure Python. It reads incoming user messages, normalizes the text (handling punctuation, case, and contractions), matches intent against a structured rule dictionary, and picks a randomized response from the appropriate category.

## Features

- **Pure Python**: Zero external dependencies or heavy frameworks.
- **Robust Input Cleaning**: Cleans whitespace, handles contractions (e.g., `what's` -> `whats`), and strips special characters.
- **Dynamic Fallbacks**: Gracefully responds to unmapped queries using default help prompts without throwing errors.
- **Customizable Knowledge Base**: Easily add keywords, responses, and new categories in `Chat_response.py`.
- **Automated Tests**: Unit test suite verifying input normalization, category detection, and edge cases.

## Project Structure

```text
autochat-project-v2/
├── ChatBot.py          # AutoChat engine and intent detection logic
├── Chat_response.py    # Response dictionary and category definitions
├── Chatmain.py         # Interactive CLI terminal loop
├── main.py             # Standard entrypoint
├── test_chatbot.py     # Unit test suite
└── README.md           # Documentation
```

## Quick Start

### 1. Run the Chatbot
Launch the chat session with either command:

```bash
python main.py
```
or:
```bash
python Chatmain.py
```

### 2. Available Sample Commands
- Type `hello`, `hi`, or `hey` to greet AutoChat.
- Type `what is python` or `what is ai` for informational responses.
- Type `tell me a joke` to hear a programming joke.
- Type `help` to list what AutoChat can do.
- Type `bye`, `exit`, or `quit` to end the session.

### 3. Run Automated Tests

```bash
python -m unittest test_chatbot.py
```

## Customizing Responses

To add or modify responses, open [`Chat_response.py`](Chat_response.py) and update the `RESPONSES` dictionary:

```python
"new_category": {
    "keywords": ["keyword1", "keyword2"],
    "responses": [
        "First reply variant.",
        "Second reply variant."
    ],
}
```
