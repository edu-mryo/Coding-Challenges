import requests
import random
import configparser
from random_words import RandomWords
rw = RandomWords()


config = configparser.ConfigParser()
config.read('config.ini')  # Read the configuration file
api_key = config['API']['key']  # Access the key from the 'API' section


def starting_point():
    fail_count = 0
    print("Hello, world!")

    while True:
        if(fail_count == 5):
            return False
        difficulty = input("Let's play hangman!. First pick a difficulty level. Type 'easy', 'medium', or 'hard': ").lower()
        if difficulty == "easy":
            print("You picked easy!")
            return difficulty
        elif difficulty == "medium":
            print("You picked medium!")
            return difficulty
        elif difficulty == "hard":
            print("Wow you must be a challenger. You picked medium!")
            return difficulty
        else:
            print("oops you seem have not chosne the correct difficulty")
            fail_count+=1
            print(fail_count)

def get_word():
    difficulty = starting_point()
    if difficulty == False:
        print("I'm sorry you made five mistakes already.Please come back again once you are ready. Bye! ")
    elif difficulty == "easy":
        word_count = random.randint(4,6) 
        while True:
            word = rw.random_word()
            if len(word) == word_count:
                print(word)
                return word
    elif difficulty == "medium":
        word_count = random.randint(7,9) 
        while True:
            word = rw.random_word()
            if len(word) == word_count:
                print(word)
                return word
    elif difficulty == "hard":
        word_count = random.randint(10,15) 
        while True:
            word = rw.random_word()
            if len(word) == word_count:
                print(word)
                return word
    

def set_bars():
    word = get_word() 
    for line in word:
        print("_", end=" ")
    

   
def main():
   set_bars()

        
    

if __name__ == "__main__":
    main()
    