import random
from random_words import RandomWords
rw = RandomWords()


def starting_point():
    fail_count = 0
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
    word_list = list(word)
    under_bar = []
    for line in word:
        # print(word_list)   
        # print("_", end=" ")
        # under_bar = under_bar.append("_")
        under_bar.append("_")
    # print(word_list)
    # print(under_bar)
    return word_list, under_bar,word
    
def guess():
    lives = 6
    answer_list,under_bar,answer_word = set_bars()
    answer_length = len(answer_list)
    while lives > 0 and "_" in under_bar:
        letter_found = False
        guess = input("Guess a letter: ").lower()
            # print(guess)
        for i in range(len(answer_list)):
            if guess == answer_list[i]:
                under_bar[i] = guess
                answer_length -= 1
                letter_found = True
                
        if not letter_found:
            print("Sorry, {guess} is not in the word".format(guess=guess))
            lives -= 1
                # print(under_bar, answer_length)
        
        for i in under_bar:
            print(i, end=" ")
        print("\nLives remaining:", lives)  # Print lives after each guess
    if lives == 0:
        print("You lose! The word was: ", answer_word)

  

def main():
   guess()

        
    

if __name__ == "__main__":
    main()
    