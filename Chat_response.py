CREATOR_NAME = "Your Name"

RESPONSES = {

    "greeting": {
        "keywords": [
            "hello", "hi", "hey", "yo",
            "good morning", "good afternoon", "good evening",
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! Type 'help' if you want to see what I can do.",
            "Hey! Great to see you.",
        ],
    },

    "how_are_you": {
        "keywords": [
            "how are you", "how is it going", "hows it going",
            "how do you do", "whats up", "how are you doing",
        ],
        "responses": [
            "I'm doing great, thanks for asking! How are you?",
            "All systems running smoothly! How about you?",
            "I'm just a program, but I feel fantastic today!",
        ],
    },

    "name": {
        "keywords": [
            "your name", "what is your name", "name", "who are you",
        ],
        "responses": [
            "I'm AutoChat, a simple chatbot built with pure Python!",
            "My name is AutoChat - nice to meet you!",
            "You can call me AutoChat!",
        ],
    },

    "creator": {
        "keywords": [
            "who created you", "who made you", "who built you",
            "creator", "developer", "author",
        ],
        "responses": [
            f"I was created by Pavan_p_pureppanavar as an AIML portfolio project.",
            f"Pavan_p_pureppanavar built me using Python - no external APIs needed!",
            f"My creator is Pavan_p_pureppanavar, a student learning AI and Machine Learning.",
        ],
    },


    "python": {
        "keywords": [
            "python", "what is python", "python language", "is python easy",
        ],
        "responses": [
            "Python is a popular, high-level programming language known for its simple, readable syntax.",
            "Python is great for beginners! It is used in web development, data science, AI, and automation.",
            "Python was created by Guido van Rossum and first released in 1991. Its motto: 'Simple is better than complex.'",
        ],
    },

    "ai": {
        "keywords": [
            "ai", "artificial intelligence", "what is ai",
            "machine learning", "deep learning", "nlp",
        ],
        "responses": [
            "Artificial Intelligence (AI) is the ability of computers to do tasks that normally need human intelligence, like understanding language or recognizing images.",
            "Machine Learning is a part of AI where computers learn patterns from data instead of following fixed rules.",
            "AI is everywhere today: voice assistants, recommendation systems, self-driving cars, and chatbots like me!",
        ],
    },

    "joke": {
        "keywords": [
            "joke", "funny", "make me laugh", "laugh", "humor",
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "There are only 10 types of people in the world: those who understand binary and those who don't.",
            "Why was the computer cold? It left its Windows open!",
            "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
        ],
    },

    "thanks": {
        "keywords": [
            "thanks", "thank you", "thx", "ty", "appreciate it", "appreciated",
        ],
        "responses": [
            "You're welcome!",
            "Anytime! Happy to help.",
            "No problem at all!",
        ],
    },


    "bye": {
        "keywords": [
            "bye", "goodbye", "exit", "quit", "see you", "see ya", "good night",
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "Bye! Come back soon.",
            "See you later! It was nice chatting with you.",
        ],
    },

    "help": {
        "keywords": [
            "help", "commands", "what can you do", "options", "menu", "how to use",
        ],
        "responses": [
            (
                "Here is what I can do:\n"
                "- Small talk: say hello, ask me how I am, or say thanks\n"
                "- Info:      ask my name, who created me, or about Python and AI\n"
                "- Fun:       ask me for a programming joke\n"
                "- Exit:      type 'bye', 'exit', or 'quit' to end the chat"
            ),
            (
                "Try one of these:\n"
                "- 'what is python'  -> I explain Python\n"
                "- 'what is ai'      -> I explain Artificial Intelligence\n"
                "- 'tell me a joke'  -> I tell a programming joke\n"
                "- 'bye'             -> I say goodbye and end the chat"
            ),
        ],
    },

    "unknown": {
        "keywords": [],
        "responses": [
            "Sorry, I didn't understand that. Type 'help' to see what I can do!",
            "Hmm, I'm not sure about that. Try asking about Python, AI, or a joke!",
            "I don't know that one yet - but you can teach me! Just add it to responses.py.",
        ],
    },
}