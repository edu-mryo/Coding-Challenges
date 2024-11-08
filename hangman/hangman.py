import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')  # Read the configuration file

api_key = config['API']['key']  # Access the key from the 'API' section

print(api_key)

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
        api_url = 'https://api.api-ninjas.com/v1/randomword'
        

        
    

   
def main():
    starting_point()

        
    

if __name__ == "__main__":
    main()
    