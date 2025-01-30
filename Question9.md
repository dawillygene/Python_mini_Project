

#### Algorithm Steps

1. Start
2. Initialize:
   - Load high scores from a file (if it exists).
   - Display the welcome message and prompt the user for their name.
3. Select Difficulty:
   - Display the difficulty options:
     - Easy: Numbers between 1 and 50, 10 attempts.
     - Medium: Numbers between 1 and 100, 7 attempts.
     - Hard: Numbers between 1 and 200, 5 attempts.
     - Custom: User-defined range and attempts.
   - Prompt the user to select a difficulty level.
4. Set Game Parameters:
   - Based on the selected difficulty, set the range of numbers (`min_num`, `max_num`) and the number of attempts.
5. Generate Target Number:
   - Randomly generate a number within the selected range.
6. Game Loop:
   - For each attempt:
     - Prompt the user to guess the number.
     - If the guess is correct:
       - Display a success message.
       - Calculate the score based on the number of attempts and difficulty.
       - Update the high scores.
       - Break out of the loop.
     - If the guess is incorrect:
       - Provide a hint ("too high" or "too low").
       - Decrement the remaining attempts.
   - If all attempts are exhausted, display the correct number and end the game.
7. Update High Scores:
   - If the user scored points, add their name and score to the high scores list.
   - Sort the high scores in descending order.
   - Save the updated high scores to a file.
8. Display Leaderboard:
   - Show the top 3 high scores.
9. Play Again:
   - Ask the user if they want to play again.
   - If yes, restart the game.
   - If no, end the program.
10. End

---

#### Pseudocode


1. Start
2. Load high scores from file
3. Display welcome message
4. Prompt user for name
5. Display difficulty options:
   - Easy
   - Medium
   - Hard
   - Custom
6. Prompt user to select difficulty
7. Set game parameters based on difficulty:
   - min_num, max_num, attempts
8. Generate target_number = random number between min_num and max_num
9. Initialize score = 0
10. For each attempt from 1 to attempts:
    11. Prompt user to guess the number
    12. If guess == target_number:
        13. Display success message
        14. Calculate score = calculate_score(attempt, difficulty)
        15. Update high scores with name and score
        16. Break loop
    17. Else if guess < target_number:
        18. Display "Too low!"
    19. Else if guess > target_number:
        20. Display "Too high!"
21. If no correct guess after all attempts:
    22. Display "Sorry, the number was target_number."
23. Save updated high scores to file
24. Display leaderboard
25. Prompt user to play again
26. If user chooses to play again:
    27. Go to step 5
28. Else:
    29. Display "Thanks for playing! Goodbye!"
30. End




Example Walkthrough

1. User Input:
   - Name: Alice
   - Difficulty: Medium (1-100, 7 attempts)

2. Gameplay:
   - Target number: 42 (randomly generated)
   - Guess 1: 50 → "Too high!"
   - Guess 2: 25 → "Too low!"
   - Guess 3: 37 → "Too low!"
   - Guess 4: 42 → "Congratulations! You guessed the number in 4 attempts!"

3. Score Calculation:
   - Score = 100 - (4 * 10) = 60 points (Medium difficulty)

4. Leaderboard Update:
   - Alice's score is added to the high scores list.

5. Output:
   
   --- Leaderboard ---
   1. Alice: 60 points
   

6. Play Again:
   - User chooses "no" → Program ends.
