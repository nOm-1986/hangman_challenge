import numbers
import random;
from os import system, name;


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
    return words
       


def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def menu():
    running = True

    while running:
        option = input(welcome_message())

        if (option == '1' or option == '2' or option == '3'):
            clearConsole()
            print(list_hangman_attempts(6))
            print('Iniciamos el proceso limpiando consola')

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
    #run()
    print(read_random_word())
