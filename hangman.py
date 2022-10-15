import numbers
import random;
from os import system, name
from turtle import position;


def list_hangman_attempts(attempt):
    hangman_figure = [
        """
            +---+
            |   
            |
            |
            |
            |
        =========
        """,
        """
            +---+
            |   |
            |
            |
            |
            |
        =========
        """,
        """
            +---+
            |   |
            |   O
            |
            |
            |
        =========
        """,
        """
            +---+
            |   |
            |   O 
            |  /|
            |
            |
        =========
        """,
        """
            +---+
            |   |
            |   O
            |  /|\\
            |
            |
        =========
        """,
        """
            +---+
            |   |
            |   O
            |  /|\\
            |  /
            |
        =========
        """,
        """
            +---+
            |   |
            |   O
            |  /|\\
            |  / \\
            |
        =========
        """
    ]
    return hangman_figure[attempt]


def welcome_message():
    return """
            ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
            ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
            ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
            ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
            ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
            Welcome to hangman play - You only have seven attempts.
                Please select an option:
                1 - Play.
                2 - Words between 4 and 5 letters. -- Coming soon
                3 - More than 6 letters. -- Coming soon
                4 - Restart game.
                5 - To quit
    """


def read_random_word():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [ x.strip().lower() for x in f ]
        chosen_word = random.choice(words)
    return chosen_word
       

def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def playing_game():
    attempts = 7
    #chosen_word = read_random_word()
    chosen_word = 'abeja'
    word_underscore = ['_'] * len(chosen_word)
    possitions = {}
    for ind, letter in enumerate(chosen_word):
        if not possitions.get(letter):
            possitions[letter] = []
        possitions[letter].append(ind)
    
    print(word_underscore)

    for k, v in position:
        print(k, v)

    # selected = 'a'
    # for let, pos in possitions:
    #     if selected == let:
    #         word_underscore[pos] = selected
    #     else :
    #         word_underscore[pos] = ['_']
    # print(word_underscore)
    #result = True

    # while result:
    #     print('Adivina la palabra: ')
    #     t = '_ '*count_guess_word
    #     print(t, f'.   Total letters: {count_guess_word}')
    #     input_letter = input('Insert your letter: ')    
    #     result = False


def print_function(word, input_player):
    pass


def menu():
    running = True

    while running:
        option = input(welcome_message())

        if (option == '1' or option == '2' or option == '3'):
            clearConsole()
            playing_game()

        elif option == '4':
            clearConsole()
            print('Restarting Game')

        elif option == '5':
            clearConsole()
            print('Thank you to play this game')
            running = False
        
        else:
            clearConsole()
            print('Please choose a correct option')
        

def run():
    menu()


if __name__ == '__main__':
    run()
