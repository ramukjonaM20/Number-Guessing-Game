# Number-Guessing-Game

A simple number guessing game where the computer randomly selects a number, and the player tries to guess it within a limited number of attempts. This project is created using Python and can be run in a console or optionally with a graphical user interface (GUI) using Tkinter.

## Table of Contents
* [**Project Description**](#project-description)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [How to Play](#how-to-play)
* [Future Enhancements](#future-enhancements)

## Project Description
In this game, the computer selects a random number within a specified range, and the player has to guess the number in a limited number of attempts. The game provides feedback on whether the player’s guess is too high, too low, or correct. This project was initially developed as a console-based game and can be enhanced with a graphical interface using Tkinter or PyQt.

## Features
* **Random Number Generation:** The game generates a random number within a specified range, making it challenging and replayable.
* **Player Input:** Allows the player to input guesses through the console. Optionally, a GUI input box can be used.
* **Hint System:** Provides hints to the player if the guess is too high, too low, or correct.
* **Attempts Tracking:** Limits the number of attempts and displays the remaining attempts after each guess.
* **Optional GUI:** If desired, a graphical interface can be created using Tkinter or PyQt for easier user interaction and visual feedback.

## Technologies Used
* **Python:** For the game logic and core functionality.
* **Tkinter/PyQt (Optional):** For creating an optional GUI version of the game.

## How to Play
1. When the game starts, the computer will select a random number within a predefined range (e.g., 1 to 100).
2. You will have a limited number of attempts to guess the number correctly.
3. Enter your guess. After each guess, the game will provide feedback:
    * If the guess is too high, it will prompt you to try a lower number.
    * If the guess is too low, it will prompt you to try a higher number.
    * If the guess is correct, you win the game!
4. If you run out of attempts, the game will reveal the correct number.

## Future Enhancements
Some possible improvements for future iterations of this project include:

* **Difficulty Levels:** Allow the user to select difficulty levels with different number ranges and attempts.
* **Score System:** Implement a scoring system based on the number of attempts taken.
* **Additional Hints:** Provide additional hints, like if the guess is within a certain range of the correct answer.
* **Leaderboard:** Maintain a leaderboard of high scores for each difficulty level.
