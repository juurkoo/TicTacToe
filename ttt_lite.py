"""

projekt_2.py: Druhý projekt do Engeto Online Python Akademie
author: Juraj Batoška
email: juraj.batoska@gmail.com
discord: juraj.batoska#9280

"""

import os, platform
import random
import time
from copy import deepcopy


def clrscr():
    if platform.system() == "Darwin" or platform.system() == "Linux":
        os.system('clear')
    else :
        os.system('cls')


def intro():
    print("""\nWelcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game\n
Press ENTER to continue ...""")


def show_board(fields):
    clrscr()
    print(f"""
-TIC TAC TOE-

+---+---+---+
| {fields[0]} | {fields[1]} | {fields[2]} |
+---+---+---+
| {fields[3]} | {fields[4]} | {fields[5]} |
+---+---+---+
| {fields[6]} | {fields[7]} | {fields[8]} |
+---+---+---+
""")


def write_text_dynamic(text):
    for letter in text:
        print(letter, end="")
        if letter != " ":
            time.sleep(0.05)
        

def turn_player_o(fields, player_o_moves, player_x_moves):
    while True:
        position = input(f"Player \033[32mO\033[0m | Please enter your move number: ")
        is_ok, fields, text, player_o_moves, player_x_moves = control_turn(position, fields, player_o_moves, player_x_moves, char="O")
        
        if not is_ok:
            print(text)        
        else:
            return "O"


def turn_player_x(fields, player_o_moves, player_x_moves):
    while True:
        position = input(f"Player \033[33mX\033[0m | Please enter your move number: ")
        is_ok, fields, text, player_o_moves, player_x_moves = control_turn(position, fields, player_o_moves, player_x_moves, char="X")
        
        if not is_ok:
            print(text)       
        else:
            return "X"


def control_turn(position, fields, player_o_moves, player_x_moves, char):
    text = ""

    if position.isnumeric():
        position = int(position)
        
        if 0 < position < 10:

            if fields[position-1] == position:

                if char == "O":
                    fields[position-1] = f"\033[32mO\033[0m"
                elif char == "X":
                    fields[position-1] = f"\033[33mX\033[0m"
                if char == "O":
                    player_o_moves.append(position)
                else:
                    player_x_moves.append(position)
                return True, fields, text, player_o_moves, player_x_moves

            else:
                text = "CHOOSED FIELD IS OCCUPIED !"
                return False, fields, text, player_o_moves, player_x_moves
        
        else:
            text = "ENTER A NUMBER 1 - 9 !"
            return False, fields, text, player_o_moves, player_x_moves
    
    else:
        text = "ENTER A NUMBER 1 - 9 !"
        return False, fields, text, player_o_moves, player_x_moves


def check_game_status(player_moves):
    OPTIONS_TO_WIN = {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5 ,8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}
    player_moves = set(player_moves)
    for win in OPTIONS_TO_WIN:
        if win.intersection(player_moves) == win:
            win_numbers = list(win)
            winner = True
            return winner, win_numbers
       
    winner = False
    win_numbers = []
    return winner, win_numbers
            

def show_win(char, fields, winner_numbers):
        changed_fields = deepcopy(fields)
        
        for number in winner_numbers:
            changed_fields[number-1] = " "
        
        i = 2
        for i in range(5):
            if i%2 == 0:
                show_board(fields)
            else:
                show_board(changed_fields)
            if char == "O":
                player = "\033[32mO\033[0m"
            else:
                player = "\033[33mX\033[0m"

            print(f"CONGRATULATION ! Player {player} wins !")
            time.sleep(0.4)
            i += 1

        option()


def option():
    while True:
        option = input("\nPress >>> ENTER <<< to repeat game, or 'q' to QUIT ...")
        
        if option == "":
            main(fields = [1, 2, 3, 4, 5, 6, 7, 8, 9], player_o_moves=[], player_x_moves=[])
        elif option == "q":
            print()
            write_text_dynamic("Thank you for playing.")
            time.sleep(2)
            clrscr()
            quit()
        else:
            write_text_dynamic("\nWRONG OPTION !")          


def main(fields, player_o_moves, player_x_moves):   
    clrscr()
    choice = [1, 2]
    random_turn = random.choice(choice)

    while True:
        clrscr()
        show_board(fields)

        if len(player_o_moves) + len(player_x_moves) == 9:
            print("TIDE GAME !!!")
            option()

        elif random_turn %2 == 0:
            char = turn_player_o(fields, player_o_moves, player_x_moves)
            winner, winner_numbers = check_game_status(player_o_moves)
            if winner:
                show_win(char, fields, winner_numbers)
            
        else:
            char = turn_player_x(fields, player_o_moves, player_x_moves)
            winner, winner_numbers = check_game_status(player_x_moves)
            if winner:
                show_win(char, fields, winner_numbers)
        
        random_turn += 1

clrscr()
intro() 
input()
main(fields = [1, 2, 3, 4, 5, 6, 7, 8, 9], player_o_moves=[], player_x_moves=[])

