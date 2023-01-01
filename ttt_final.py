
"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Juraj Batoška
email: juraj.batoska@gmail.com
discord: juraj.batoska#9280

"""


import os
import time
import platform
import random
import copy


class Var(): 
    player1_name = ""
    player2_name = ""
    player1_score = 0
    player2_score = 0
    dificulty = 0
    victories = str
    player1_moves = []
    player2_moves = []
    board_window = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    OPTIONS_TO_WIN = {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5 ,8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}
    first_start = True
    round = 1
    turn = 0
    number_of_players = int
    choosed_language = "eng"
    start_round_measure = True
    time_measure = True
    time_text = str
    

class Color():
    W = "\033[0m"
    G = "\033[32m"
    Y = "\033[33m"
    R = "\033[31m"


class Txt:
    text1, text2, text3, text4, text5, text6, text7, text8, text9, text10 = str, str, str, str, str, str, str, str, str, str
    text11, text12, text13, text14, text15, text16, text17, text18, text19, text20 = str, str, str, str, str, str, str, str, str, str
    text21, text22, text23, text24, text25, text26, text27, text28, text29, text30 = str, str, str, str, str, str, str, str, str, str


def clrscr():
    if platform.system() == "Darwin" or platform.system() == "Linux":
        os.system('clear')
    else :
        os.system('cls')


def write_text_dynamic(text: str):
    PAUSE = 0.05
    for letter in text:
        print(letter, end="")
        if letter == " ":
            continue
        else:
            time.sleep(PAUSE)    


def end_or_restart(option: str):
    if option == "q":
        print()
        write_text_dynamic(Txt.text27)
        time.sleep(2)
        clrscr()
        quit()
    
    if option == "r":
        main()


def show_intro():
    PAUSE = 2
    clrscr()
    print()
    write_text_dynamic(f"{Color.G}JB{Color.W} SOFTWARE PRESENTS")
    time.sleep(PAUSE)
    clrscr()
    print()
    write_text_dynamic(f"{Color.R}T{Color.W}IC {Color.R}T{Color.W}AC {Color.R}T{Color.W}OE")
    time.sleep(PAUSE)
    

def show_tittle():
    clrscr()
    print(f"\n{Color.R}T{Color.W}IC {Color.R}T{Color.W}AC {Color.R}T{Color.W}OE\n")


def show_me_short_dynamic_text(text: str) -> str:
    print(text)
    time.sleep(1)
    

def reset_stats_of_game():
    Var.player1_score = 0
    Var.player2_score = 0
    Var.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Var.player1_moves = []
    Var.player2_moves = []
    Var.round = 1
    Var.time_text = str


def set_random_turn():
    Var.turn = random.randint(0,10)


def select_language():
    switch = False
    while switch != True:
        show_tittle()
        print(f"SELECT LANGUAGE :\n({Color.R}1{Color.W}) English\n({Color.R}2{Color.W}) German\n({Color.R}3{Color.W}) Slovak\n")
        language = input()
        
        if language == "r":
            continue

        elif language == "q":
            select_english_language()
            end_or_restart(language)

        elif language == "1":
            Var.choosed_language = "eng"
            select_english_language()
            switch = True

        elif language == "2":
            Var.choosed_language = "de"
            select_german_language()
            switch = True

        elif language == "3":
            Var.choosed_language = "sk"
            select_slovak_language()
            switch = True

        else:
            show_me_short_dynamic_text("WRONG OPTION !")


def select_english_language():
    Txt.text1 = f"CHOOSE YOUR OPTION :\n({Color.R}1{Color.W}) Player\n({Color.R}2{Color.W}) Players\n\nYOU CAN ALSO EVERYTIME USE :\n({Color.R}r{Color.W}) - to restart\n({Color.R}q{Color.W}) - to quit\n"
    Txt.text2 = "WRONG OPTION !"
    Txt.text3 = "ENTER A NAME OF PLAYER 1 : "
    Txt.text4 = "WORNG NAME, OLNY LETTERS !"
    Txt.text5 = "MAX. 10 CHARACTERS !"
    Txt.text6 = "ENTER A NAME OF PLAYER 2 : "
    Txt.text7 = "THE PLAYER 1 ALREADY USES THIS NAME !"
    Txt.text8 = "Enter a number of victories ( 1 - 10 ) : "
    Txt.text9 = "Only number 1 - 10 !"
    Txt.text10 = "ENTER YOUR NAME : "
    Txt.text11 = "YOU PLAY AGAINST COMPUTER !"
    Txt.text12 = f"Choose your dificulty :\n({Color.R}1{Color.W}) Easy\n({Color.R}2{Color.W}) Hard\n\n"
    Txt.text13 = "ROUND"
    Txt.text14 = "TO WIN"
    Txt.text15 = "TIED GAME !"
    Txt.text16 = "WINS THIS ROUND ! "
    Txt.text17 = "it's your turn !"
    Txt.text18 = "ENTER A NUMBER OF POSITION : "
    Txt.text19 = "THE POSITION"
    Txt.text20 = "IS ALREADY OCCUPIED"
    Txt.text21 = "victory"
    Txt.text22 = "victories"
    Txt.text23 = "CONGRATULATION"
    Txt.text24 = "YOU HAVE REACHED"
    Txt.text25 = "YOU WIN !"
    Txt.text26 = f"\n({Color.R}y{Color.W}) - REPEAT THE SAME GAME\n({Color.R}ENTER{Color.W}) - MAIN MENU\n\n"
    Txt.text27 = "Thank you for playing."
    Txt.text28 = "Round time"
    Txt.text29 = "seconds"


def select_german_language():
    Txt.text1 = f"WäHLE EINE OPTION :\n({Color.R}1{Color.W}) Ein Spieler\n({Color.R}2{Color.W}) Zwei Spieler\n\nDU KANNST JEDERZEIT DAS SPIEL NEU STARTEN ODER BEENDEN :\n({Color.R}r{Color.W}) - Neustart\n({Color.R}q{Color.W}) - Spiel beenden\n"
    Txt.text2 = "FALSCHE EINGABE!"
    Txt.text3 = "NAME SPIELER 1 : "
    Txt.text4 = "FALSCHE EINGABE, NUR BUCHSTABEN ERLAUBT !"
    Txt.text5 = "MAX. 10 ZEICHEN !"
    Txt.text6 = "NAME SPIELER 2 : "
    Txt.text7 = "DER SPIELER 1 BENUTZT SCHON DIESEN NAME !"
    Txt.text8 = "ANZAHL SIEGE, UM DAS SPIEL ZU GEWINNEN ( 1 - 10 ) : "
    Txt.text9 = "WäHLE 1 - 10 !"
    Txt.text10 = "NAME SPIELER : "
    Txt.text11 = "DU SPIELST GEGEN DEN COMPUTER !"
    Txt.text12 = f"WäHLE DIE SCHWIERIGKEITSTUFFE :\n({Color.R}1{Color.W}) Einfach\n({Color.R}2{Color.W}) Schwierig\n\n"
    Txt.text13 = "RUNDE"
    Txt.text14 = "ZUM GEWINNEN"
    Txt.text15 = "REMISE !"
    Txt.text16 = "GEWINNT DIESE RUNDE ! "
    Txt.text17 = "du bist dran !"
    Txt.text18 = "GIB EINE FELDNUMMER EIN : "
    Txt.text19 = "DAS FELD"
    Txt.text20 = "IST SCHON BESETZT"
    Txt.text21 = "Sieg"
    Txt.text22 = "Siege"
    Txt.text23 = "GRATULIERE"
    Txt.text24 = "DU HAST ERREICHT"
    Txt.text25 = "DU GEWINNST !"
    Txt.text26 = f"\n({Color.R}y{Color.W}) - SPIEL WIEDERHOLEN\n({Color.R}ENTER{Color.W}) - MAIN MENU\n\n"
    Txt.text27 = "Vielen Dank fürs spielen."
    Txt.text28 = "Rundenzeit"
    Txt.text29 = "Sekunden"


def select_slovak_language():
    Txt.text1 = f"VYBER MOŽNOSŤ :\n({Color.R}1{Color.W}) Hráč\n({Color.R}2{Color.W}) Hráči\n\nKEDYKOĽVEK MôŽEŠ POUŽIŤ :\n({Color.R}r{Color.W}) - pre reštart\n({Color.R}q{Color.W}) - pre ukončenie\n"
    Txt.text2 = "NESPRÁVNA VOĽBA !"
    Txt.text3 = "ZADAJ MENO PRVÉHO HRÁČA : "
    Txt.text4 = "NESPRÁVNE MENO, IBA PÍSMENÁ !"
    Txt.text5 = "MAX. 10 ZNAKOV !"
    Txt.text6 = "ZADAJ MENO DRUHÉHO HRÁČA : "
    Txt.text7 = "PRVÝ HRÁČ UŽ POUŽÍVA TOTO MENO !"
    Txt.text8 = "Zadaj počet výhier ( 1 - 10 ) : "
    Txt.text9 = "Iba čísla od 1 - 10 !"
    Txt.text10 = "ZADAJ MENO HRÁČA : "
    Txt.text11 = "TY HRÁŠ PROTI COMPUTER !"
    Txt.text12 = f"Vyber obtiažnosť :\n({Color.R}1{Color.W}) Jednoduchá\n({Color.R}2{Color.W}) Ťažká\n\n"
    Txt.text13 = "KOLO"
    Txt.text14 = "POTREBNÝCH NA VÝHRU"
    Txt.text15 = "REMÍZA !"
    Txt.text16 = "VYHRÁVA TOTO KOLO ! "
    Txt.text17 = "si na rade !"
    Txt.text18 = "ZADAJ POZÍCIU : "
    Txt.text19 = "POZÍCIA"
    Txt.text20 = "JE UZ OBSADENÁ"
    Txt.text21 = "víťazstvo"
    Txt.text22 = "víťazstvá"
    Txt.text23 = "GRATULUJEME"
    Txt.text24 = "DOSIAHOL / DOSIAHLA SI"
    Txt.text25 = "VYHRAL SI !"
    Txt.text26 = f"\n({Color.R}y{Color.W}) - OPAKOVAŤ HRU\n({Color.R}ENTER{Color.W}) - MAIN MENU\n\n"
    Txt.text27 = "Ďakujeme za hranie."
    Txt.text28 = "Čas trvania kola"
    Txt.text29 = "sekúnd"


def select_game():    
    while True:
        show_tittle()
        print(Txt.text1)        
        option = input()
        end_or_restart(option)
                        
        if option == "1":
            Var.number_of_players = 1
            set_parameter_one_player()                                   
        
        if option == "2":
            Var.number_of_players = 2
            set_parameter_two_players()

        else:      
            show_me_short_dynamic_text(Txt.text2)
            continue


def set_parameter_one_player():
    player1_name_defined = False

    while not player1_name_defined:        
        show_tittle()        
        Var.player1_name = input(Txt.text10)  
        end_or_restart(Var.player1_name)  

        if Var.player1_name.lower() == "computer":
            show_me_short_dynamic_text(Txt.text11)
            continue

        if not Var.player1_name.isalpha():
            show_me_short_dynamic_text(Txt.text4)
            continue

        else: 
            if len(Var.player1_name) > 10:
                show_me_short_dynamic_text(Txt.text5)
                continue
            else:
                Var.player1_name = Var.player1_name.capitalize()
                Var.player2_name = "Computer"
                player1_name_defined = True
        
    while Var.dificulty not in ["1", "2"]:
        show_tittle()
        Var.dificulty = input(Txt.text12)
        end_or_restart(Var.dificulty)

    while True:
        show_tittle()
        Var.victories = input(Txt.text8)
        end_or_restart(Var.victories) 
        
        try :
            Var.victories = int(Var.victories)

        except:
            show_me_short_dynamic_text(Txt.text2)
            continue

        if not 0 < Var.victories < 11:
            show_me_short_dynamic_text(Txt.text2)
            continue

        set_random_turn()
        play_one_player()


def set_parameter_two_players():
    player1_name_defined, player2_name_defined = False, False
    while not player1_name_defined or not player2_name_defined:
        show_tittle()

        if not player1_name_defined:
            Var.player1_name = input(Txt.text3)
            end_or_restart(Var.player1_name)  
            
            if not Var.player1_name.isalpha():
                show_me_short_dynamic_text(Txt.text4)
                continue

            elif len(Var.player1_name) > 10:
                show_me_short_dynamic_text(Txt.text5)
                continue

            else:                            
                player1_name_defined = True
        else:
            print(f"{Txt.text3}{Var.player1_name}")
            
        if not player2_name_defined:
            Var.player2_name = input(Txt.text6)
            end_or_restart(Var.player2_name)  

            if not Var.player2_name.isalpha():
                show_me_short_dynamic_text(Txt.text4)
                continue

            else:

                if Var.player2_name == Var.player1_name:
                    show_me_short_dynamic_text(Txt.text7)
                    continue
                elif len(Var.player2_name) > 10:
                    show_me_short_dynamic_text(Txt.text5)
                    continue

                else:
                    player2_name_defined = True

    Var.player1_name = Var.player1_name.capitalize()
    Var.player2_name = Var.player2_name.capitalize()
    
    while True:
        show_tittle()
        Var.victories = input(Txt.text8)
        end_or_restart(Var.victories) 
        
        try:
            Var.victories = int(Var.victories)

        except:
            show_me_short_dynamic_text(Txt.text9)
            continue

        if 0 < Var.victories < 11:
            set_random_turn()
            play_two_players()

        else:
            show_me_short_dynamic_text(Txt.text9)
            continue
    

def show_difficulty():
    if Var.choosed_language == "eng":
        if Var.dificulty == "1":
            return "\n( Difficulty : EASY )"
        else:
            return "\n( Difficulty : HARD )"
    elif Var.choosed_language == "de":
        if Var.dificulty == "1":
            return "\n( Schwierigkeitstuffe : EINFACH )"
        else:
            return "\n( Schwierigkeitstuffe : SCHWIERIG )"
    else:
        if Var.dificulty == "1":
            return "\n( Obtiažnosť : JEDNODUCHÁ )"
        else:
            return "\n( Obtiažnosť : ŤAŽKÁ )"
    

def show_stats_and_board():
    clrscr()

    if Var.number_of_players == 1:
        difficulty_text = show_difficulty()

    else:
        difficulty_text = ""

    print(f"""\n{Color.R}T{Color.W}IC {Color.R}T{Color.W}AC {Color.R}T{Color.W}OE\n\n{Txt.text13}: {Var.round} / {Txt.text14} ({Var.victories}){difficulty_text}

SCORE :
{Color.Y}{Var.player1_name}{Color.W} : {Var.player1_score}
{Color.G}{Var.player2_name}{Color.W} : {Var.player2_score}""")


    print(f"""
+---+---+---+
| {Var.board_window[0]} | {Var.board_window[1]} | {Var.board_window[2]} |
+---+---+---+
| {Var.board_window[3]} | {Var.board_window[4]} | {Var.board_window[5]} |
+---+---+---+
| {Var.board_window[6]} | {Var.board_window[7]} | {Var.board_window[8]} |
+---+---+---+
""")


def reset_board_and_moves():
    Var.board_window = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Var.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Var.player1_moves = []
    Var.player2_moves = []
    Var.time_measure = True
    Var.start_round_measure = True


def reset_all_settings():
    Var.number_of_players = 0
    Var.player1_name = str
    Var.player2_name = str
    Var.player1_score = 0
    Var.player2_score = 0
    Var.dificulty = 0
    Var.victories = str
    Var.board_window = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Var.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Var.player1_moves = []
    Var.player2_moves = []
    Var.choosed_language = "eng"
    Var.time_measure = True
    Var.start_round_measure = True
    Var.round = 1


def show_tide_game(start_round):
    show_stats_and_board()

    if not Var.moves:
        print(Txt.text15, end="")

        show_time(start_round)
    
        time.sleep(2)
        set_random_turn()
        Var.round += 1
        
        if Var.number_of_players == 1:
            play_one_player()

        else:
            play_two_players()
        

def show_winning_board(win_numbers, player_name, char, start_round): 
    temp = 2

    if player_name == Var.player1_name:
        Var.player1_score += 1
        
    if player_name == Var.player2_name:
        Var.player2_score += 1

    for i in range(5):
        if temp %2 == 0:
            Var.board_window[win_numbers[0]-1] = char
            Var.board_window[win_numbers[1]-1] = char
            Var.board_window[win_numbers[2]-1] = char
        
        else:
            Var.board_window[win_numbers[0]-1] = " "
            Var.board_window[win_numbers[1]-1] = " "
            Var.board_window[win_numbers[2]-1] = " "
    
        show_stats_and_board()

        print(f"{player_name} {Txt.text16}",end="")
        show_time(start_round)

        time.sleep(0.5)
        temp += 1

    time.sleep(0.5)
    Var.round += 1

    win_control()    
    reset_board_and_moves()


def show_time(start_round):
    if Var.time_measure:
        end_round = time.time()
        Var.time_text = round(end_round - start_round, 2)
        
    Var.time_measure = False
    print(f"\n{Txt.text28} : {Var.time_text} {Txt.text29} !")
    

def play_one_player():  
    reset_board_and_moves()

    while True:
        show_stats_and_board()

        if Var.start_round_measure:
            start_round = time.time()
        
        Var.start_round_measure = False
        
        if Var.turn %2 == 0:

            print(f"{Color.Y}{Var.player1_name}{Color.W} ({Color.Y}O{Color.W}), {Txt.text17}")
            
            position_on_board = input(Txt.text18)
            end_or_restart(position_on_board)

            if is_input_correct(position_on_board):
                position_on_board = int(position_on_board)
                
                if is_position_free(position_on_board):
                    Var.board_window[position_on_board-1] = f"{Color.Y}O{Color.W}"
                    Var.moves.remove(position_on_board)
                    Var.player1_moves.append(position_on_board)

                    winner, win_numbers = is_win(Var.player1_moves)

                    if winner:
                        char = f"{Color.Y}O{Color.W}"
                        
                        show_winning_board(win_numbers, Var.player1_name, char, start_round)
                        Var.turn = 0

                    else:
                        if not Var.moves:
                            show_tide_game(start_round)

                else:
                    print(f"{Txt.text19} {position_on_board} {Txt.text20} !")
                    time.sleep(1)
                    continue
            else:
                print(Txt.text2)
                time.sleep(1)
                continue

        else:
            if Var.dificulty == "1":
                position_on_board = play_computer_difficulty1()
                write_computers_turn(position_on_board, start_round)
            else:
                position_on_board = play_computer_difficulty2()
                write_computers_turn(position_on_board, start_round)

        Var.turn += 1

def play_computer_difficulty1():
    position_on_board = random.choice(Var.moves)
    return position_on_board


def play_computer_difficulty2():
    # NAJPRV ZISTI, CI NEMA MOZNOST VYHRAT
    for control_win in Var.OPTIONS_TO_WIN:
        
        inters = control_win.intersection(Var.player2_moves)  

        if len(inters) == 2:    
            two_tunrs_of_three = inters.intersection(control_win)
            position_on_board = list(control_win.symmetric_difference(two_tunrs_of_three))
            position_on_board = position_on_board[0]

            if position_on_board in Var.moves:
                return position_on_board

    # ZISTI CI MOZE ZABRANIT PREHRE
    for control_lose in Var.OPTIONS_TO_WIN:
        inters = control_lose.intersection(Var.player1_moves)

        if len(inters) == 2:
            two_tunrs_of_three = inters.intersection(control_lose)
            position_on_board = list(control_lose.symmetric_difference(two_tunrs_of_three))
            position_on_board = position_on_board[0]

            if position_on_board in Var.moves:         
                return position_on_board

        else:
            continue
    
    # ZISTI KDE MOZE UHRAT DRUHY BOD Z TROCH
    if Var.player2_moves:
    
        option_to_win_copy = list(copy.deepcopy(Var.OPTIONS_TO_WIN))
        option_to_win_copy2 = copy.deepcopy(option_to_win_copy)

        for setik in option_to_win_copy:
            for move in Var.player1_moves:
                if move in setik and setik in option_to_win_copy2:
                    option_to_win_copy2.remove(setik)

        final_list = []

        for setik in option_to_win_copy2:
            for move in Var.player2_moves:
                if move in setik and setik not in final_list:
                    final_list.append(setik)

        if final_list:
            position_on_board = random.choice(final_list)
            position_on_board = (position_on_board.difference(set(Var.player2_moves)))
            position_on_board = random.choice(list(position_on_board))
            return position_on_board

        else:
            return play_computer_difficulty1()

    else:
        return play_computer_difficulty1()
           

def write_computers_turn(position_on_board, start_round):
    print(f"{Color.G}Computer{Color.W} ({Color.G}X{Color.W}), {Txt.text17}")
    print(f"{Txt.text18}",end="")
    time.sleep(1)
    print(position_on_board)
    time.sleep(1)
    Var.board_window[position_on_board-1] = f"{Color.G}X{Color.W}"
    Var.moves.remove(position_on_board)
    Var.player2_moves.append(position_on_board)

    winner, win_numbers = is_win(Var.player2_moves)

    if winner:
        char = f"{Color.G}X{Color.W}"
        show_winning_board(win_numbers, Var.player2_name, char, start_round)
        Var.turn = 1

    else:
        if not Var.moves:
            show_tide_game(start_round)


def play_two_players():
    reset_board_and_moves()
  
    while True:
        show_stats_and_board()

        if Var.start_round_measure:
            start_round = time.time()
        
        Var.start_round_measure = False
        
        if Var.turn %2 == 0:

            print(f"{Var.player1_name} ({Color.Y}O{Color.W}), {Txt.text17}")
            
            position_on_board = input(Txt.text18)
            end_or_restart(position_on_board)

            if is_input_correct(position_on_board):
                position_on_board = int(position_on_board)
                
                if is_position_free(position_on_board):
                    Var.board_window[position_on_board-1] = f"{Color.Y}O{Color.W}"
                    Var.moves.remove(position_on_board)
                    Var.player1_moves.append(position_on_board)

                    winner, win_numbers = is_win(Var.player1_moves)
                    if winner:
                        char = f"{Color.Y}O{Color.W}"
                        show_winning_board(win_numbers, Var.player1_name, char, start_round)
                        Var.turn = 0
                    else:
                        if not Var.moves:
                            show_tide_game(start_round)


                else:
                    print(f"{Txt.text19} {position_on_board} {Txt.text20}")
                    time.sleep(1)
                    continue
            else:
                print(Txt.text2)
                time.sleep(1)
                continue              
          
        else:
            print(f"{Color.G}{Var.player2_name}{Color.W} ({Color.G}X{Color.W}), {Txt.text17}")
            position_on_board = input(Txt.text18)
            end_or_restart(position_on_board)  
            
            if is_input_correct(position_on_board):
                position_on_board = int(position_on_board)
                
                if is_position_free(position_on_board):
                    Var.board_window[position_on_board-1] = f"{Color.G}X{Color.W}"
                    Var.moves.remove(position_on_board)
                    Var.player2_moves.append(position_on_board)
                    winner, win_numbers = is_win(Var.player2_moves)

                    if winner:
                        char = f"{Color.G}X{Color.W}"
                        show_winning_board(win_numbers, Var.player2_name, char, start_round)
                        Var.turn = 1

                    else:
                        if not Var.moves:
                            show_tide_game(start_round)

                else:
                    print(f"{Txt.text19} {position_on_board} {Txt.text20}")
                    time.sleep(1)
                    continue
            else:
                print(Txt.text2)
                time.sleep(1)
                continue

        Var.turn += 1
   

def win_control():
    if Var.player1_score != Var.victories and Var.player2_score != Var.victories:
        return 

    elif Var.player1_score == Var.victories:
        name_of_winner = Var.player1_name

    else:
        name_of_winner = Var.player2_name
    
    if Var.victories == 1:
        victory_or_victories = Txt.text21

    else:
        victory_or_victories = Txt.text22
        

    print(f"\n{Txt.text23} {name_of_winner} !\n{Txt.text24} {Var.victories} {victory_or_victories} !\n{Txt.text25}")
    repeat = input(Txt.text26)
    set_random_turn() 
    
    if repeat == "y":
        reset_stats_of_game()

        if Var.number_of_players == 1:
            play_one_player()

        else:
            play_two_players()

    else:
        end_or_restart("r")


def is_win(player_moves):
    player_moves = set(player_moves)
    for win in Var.OPTIONS_TO_WIN:
        if win.intersection(player_moves) == win:
            win_numbers = list(win)
            winner = True
            return winner, win_numbers
       
    winner = False
    win_numbers = []
    return winner, win_numbers
          

def is_input_correct(player_move):
    if player_move.isnumeric():
        player_move = int(player_move)
        return True if 0 < player_move < 10 else False
    
    else:
        return False

def is_position_free(player_move):
    return True if player_move in Var.moves else False

# MAIN

def main():
    while True:

        if Var.first_start == True:
            show_intro()
        
        Var.first_start = False
        reset_all_settings()
        select_language()
        select_game()
        
main()

