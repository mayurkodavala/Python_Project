import random


def play_game():
    print("=" * 40)
    print("   NUMBER GUESSING GAME - v1 Basic")
    print("=" * 40)

    # --- setup ---
    low, high = 1, 100
    max_attempts = 7
    secret = random.randint(low, high)
    print(secret)
    attempts = 0

    print(f"\nI've picked a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    # --- game loop ---
    while attempts < max_attempts:
        attempts_left = max_attempts - attempts

        # get input
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("  Please enter a valid number.\n")
            continue

        # validate range
        if guess < low or guess > high:
            print(f"  Out of range! Guess between {low} and {high}.\n")
            continue

        attempts += 1

        # check guess
        if guess == secret:
            print(f"\n  Correct! The number was {secret}.")
            print(f"  You won in {attempts} attempt{'s' if attempts > 1 else ''}!")
            break
        elif guess < secret:
            print(f"  Too low!  ({attempts_left - 1} attempt{'s' if attempts_left - 1 != 1 else ''} left)\n")
        else:
            print(f"  Too high! ({attempts_left - 1} attempt{'s' if attempts_left - 1 != 1 else ''} left)\n")

    else:
        # loop exhausted without a correct guess
        print(f"\n  Out of attempts! The number was {secret}.")
        print("  Better luck next time!")

    print()


# --- play again loop ---
while True:
    play_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("\nThanks for playing. Goodbye!")
        break
    print()