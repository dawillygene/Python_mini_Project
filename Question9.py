import random
import json
import os

HIGH_SCORES_FILE = "high_scores.json"


def load_high_scores():
    if os.path.exists(HIGH_SCORES_FILE):
        with open(HIGH_SCORES_FILE, "r") as file:
            return json.load(file)
    return []


def save_high_scores(scores):
    with open(HIGH_SCORES_FILE, "w") as file:
        json.dump(scores, file)


def display_leaderboard(scores):
    print("\n--- Leaderboard ---")
    if not scores:
        print("No high scores yet!")
    else:
        for i, score in enumerate(scores[:3], 1):
            print(f"{i}. {score['name']}: {score['score']} points")

def calculate_score(attempts, difficulty):
    base_score = 100
    if difficulty == "easy":
        return base_score - (attempts * 5)
    elif difficulty == "medium":
        return base_score - (attempts * 10)
    elif difficulty == "hard":
        return base_score - (attempts * 20)
    return 0


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")


    print("\nSelect difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    print("4. Custom (Choose your own range and attempts)")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        min_num, max_num = 1, 50
        attempts = 10
        difficulty = "easy"
    elif choice == "2":
        min_num, max_num = 1, 100
        attempts = 7
        difficulty = "medium"
    elif choice == "3":
        min_num, max_num = 1, 200
        attempts = 5
        difficulty = "hard"
    elif choice == "4":
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
        attempts = int(input("Enter the number of attempts: "))
        difficulty = "custom"
    else:
        print("Invalid choice. Defaulting to Easy mode.")
        min_num, max_num = 1, 50
        attempts = 10
        difficulty = "easy"


    target_number = random.randint(min_num, max_num)
    print(f"\nI'm thinking of a number between {min_num} and {max_num}. Can you guess it?")


    score = 0
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt} of {attempts}")
        guess = int(input("Enter your guess: "))

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            score = calculate_score(attempt, difficulty)
            print(f"Your score: {score} points")
            break
    else:
        print(f"\nSorry, you've run out of attempts. The number was {target_number}.")


    if score > 0:
        high_scores = load_high_scores()
        high_scores.append({"name": name, "score": score})
        high_scores.sort(key=lambda x: x["score"], reverse=True)
        save_high_scores(high_scores)
        display_leaderboard(high_scores)


def main():
    while True:
        number_guessing_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()