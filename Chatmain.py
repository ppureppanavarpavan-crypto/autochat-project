
from ChatBot import AutoChat

BANNER = """
========================================
              A U T O C H A T
        Your friendly Python chatbot
========================================
 Type 'help' to see what I can do.
 Type 'bye', 'exit' or 'quit' to leave.
========================================
"""


def show_welcome():
    """Print the welcome banner."""
    print(BANNER)


def main():
    """Start AutoChat and run the chat loop."""
    chatbot = AutoChat(name="AutoChat")

    show_welcome()
    print(f"{chatbot.name}: Hello! I'm AutoChat. Type 'bachav' to see what I can do.\n")

    while True:
        # Ask the user for input (Ctrl+C or Ctrl+D ends the chat politely).
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{chatbot.name}: Goodbye! Thanks for chatting with me. Be my guest again soon...!")
            break

        # Ignore empty input (just pressing Enter).
        if not user_input.strip():
            continue

        # Send the input to the chatbot and print the reply.
        response = chatbot.get_response(user_input)
        print(f"{chatbot.name}: {response}")

        # Stop the loop when the user typed an exit command.
        if chatbot.is_exit_command(user_input):
            break

    print("\n[Chat ended. Run 'python main.py' to start again!]")


if __name__ == "__main__":
    main()