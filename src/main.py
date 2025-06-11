#!/usr/bin/env python3

"""Simple interactive shell for Gamex OS.

Provides a few built-in commands and a very small demo game so that
users can try out the environment. This isn't meant to be a fully
featured operating system, just a playground for simple games.
"""


def guess_game():
    """A tiny guessing game used as a demo."""

    import random

    target = random.randint(1, 10)
    tries = 0
    print("I'm thinking of a number between 1 and 10.")
    while True:
        guess = input("Your guess (or 'quit'): ").strip().lower()
        if guess in {"quit", "exit"}:
            print("Exiting game.")
            return
        if not guess.isdigit():
            print("Please enter a number.")
            continue

        tries += 1
        num = int(guess)
        if num == target:
            print(f"Correct! You guessed it in {tries} tries.")
            return
        elif num < target:
            print("Too low!")
        else:
            print("Too high!")


def print_help():
    """Display available commands."""

    print("Available commands:")
    print("  help         - show this help message")
    print("  about        - information about Gamex OS")
    print("  games        - list available games")
    print("  play <game>  - start a game")
    print("  exit         - quit the shell")


def main():
    print("Welcome to Gamex OS!")
    print("Type 'help' for a list of commands.")

    games = {"guess": guess_game}

    while True:
        try:
            cmd = input("Gamex> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()  # newline after ^D/^C
            break

        if not cmd:
            continue

        parts = cmd.split()
        action = parts[0].lower()

        if action in {"exit", "quit"}:
            print("Exiting Gamex OS. Goodbye!")
            break
        elif action == "help":
            print_help()
        elif action == "about":
            print("Gamex OS is a lightweight shell for running small games.")
        elif action == "games":
            print("Available games:")
            for name in games:
                print(f"  {name}")
        elif action == "play":
            if len(parts) < 2:
                print("Usage: play <game>")
                continue
            game = parts[1].lower()
            if game not in games:
                print(f"Unknown game: {game}")
                continue
            games[game]()
        else:
            print(f"Unknown command: {action}")


if __name__ == "__main__":
    main()
