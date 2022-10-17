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


def hangman_draw():
    return """
            ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
            ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
            ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
            ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
            ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    """

def option_menu_messages():
    return """
            Welcome to hangman play - You only have seven attempts.
                Please select an option:
                1 - Play.
                2 - Words between 4 and 5 letters. -- Coming soon
                3 - More than 6 letters. -- Coming soon
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
    clearConsole()
    lives = 0
    chosen_word = read_random_word()
    word_underscore = ['_'] * len(chosen_word)
    chosen_letter_player = input('Please, insert a letter: ')
    result = True
    print(list_hangman_attempts(lives))

    while result and lives < 7:
        
        isInWord = 0
        position = 0
        for letter in chosen_word:
            if word_underscore[position] == '_':
                if chosen_letter_player == letter:
                    word_underscore[position] = chosen_letter_player
                    isInWord += 1
                else:
                    word_underscore[position] = '_'
            position += 1
        
        word_to_compare = ''
        for word in word_underscore:
            word_to_compare += word

        if isInWord == 0:
            lives += 1

        if word_to_compare == chosen_word:
            print('='*50)
            print('FELICITACIONES GANASTESSSSS')
            break
        
        if lives > 6:
            clearConsole()
            print('You lost, please try again.')
            break

        clearConsole()
        print(list_hangman_attempts(lives))
        print(word_underscore)
        chosen_letter_player = input('Please, insert a letter: ')


def menu():
    running = True
    while running:
        print(hangman_draw())
        option = input(option_menu_messages())

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
