from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Hey", "Hello", "Sup"):
        return "Hello there! Nice to meet you."
