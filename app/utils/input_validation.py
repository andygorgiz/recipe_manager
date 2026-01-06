def safe_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input får inte vara tom. Försök igen.")