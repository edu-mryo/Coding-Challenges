# Challenge Title: Number Guessing Game

# Description: Create a Python program where the computer randomly selects a number between 1 and 100, and the user has to guess it. The program should provide feedback after each guess, telling the user whether their guess is too high or too low. Keep track of the number of guesses it takes the user to find the correct number.

# Difficulty: Easy

# Estimated Time: 1-2 hours

# Bonus Challenges:

# Add a difficulty setting that allows the user to choose a wider range of numbers.
# Implement a scoring system based on the number of guesses taken.
# Give the user the option to play again without restarting the program.
# Learning Objectives:

# Working with random numbers in Python (random module)
# Using loops (while loop) and conditional statements (if, elif, else)
# Getting user input
# Basic program flow and logic
# This classic beginner project is a fun way to practice fundamental Python concepts! Let me know if you'd like another challenge or have any questions about this one.

import random

def pick_difficulty():
    
    wrong_choice = 0 
    while True:
        if wrong_choice == 5:
            print("I'm sorry you made five mistakes already. Please come back again once you are ready. Bye!")
            break
        difficulty = input("Hi there. `Choose Difficulty by using 'easy' or 'hard' and press Enter: ").lower()
        if difficulty == "easy":
            print("You picked easy!")
            return difficulty
        elif difficulty == "hard":
            print("You picked hard!")
            return difficulty
        else:
            print("Oops! You seem to have not chosen the correct difficulty. Please try again.")
            wrong_choice+=1

def get_number_by_difficulty():
    difficulty = pick_difficulty()
    if difficulty == "easy":
        return random.randint(1, 10), difficulty
    elif difficulty == "hard":
        return random.randint(1, 100),difficulty


def main():
    number,difficulty = get_number_by_difficulty()
    print(type(number))
    print(type(difficulty))
    print(f"number: {number}")
    print(f"difficulty: {difficulty}")
    guess_count =0
    
    while True:
        guess_count+=1
        if difficulty == "easy":
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == number:
                print(f"You got it after {guess_count} guesses!")
                new_game=input("Do you want to play again? Press 'y' for yes and 'n' for no: ")
                if new_game == "y":
                    print(new_game)
                    main()
                else:
                    break
            elif guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Invalid input. Please try again.")
        if difficulty == "hard":
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == number:
                print(f"You got it after {guess_count} guesses!")
                new_game= input("Do you want to play again? Press 'y' for yes and 'n' for no: ")
                if new_game == "y":
                    print(new_game)
                    main()
                else:
                    break
            elif guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Invalid input. Please try again.")
    
    
        
    

if __name__ == "__main__":
    main()
    




