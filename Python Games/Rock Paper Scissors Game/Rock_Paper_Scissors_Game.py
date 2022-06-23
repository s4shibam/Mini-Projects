"""
• Project Name - "ROCK PAPER SCISSORS" GAME
• Author - Shibam Saha (B.Tech CSE)'24
• Dated - 19.12.21
• Details - This game has been created by using basic function calling, if-else statement, infinite while loop.
            Few in-built header file was used like: random, time, cls etc. for convenience.
"""

import random           # To get a Random integer number
from time import sleep  # To add a delay for few secs before printing next line
import cls              # To clear screen

user_name = ''          # This global variable is used to store the player name

# Function to display the rules of this game and to take the user_name input
def game_rule():
    print("Read and try to remember the rules!!\n")
    print("Game Rules:")
    print("-----------")
    print("1. Rock wins against Scissors.\n"
          "2. Scissors win against Paper.\n"
          "3. Paper wins against rock.\n")
    print("Basic Rules:")
    print("-----------")
    print("1. You will get only 10 rounds in a session!")
    print("2. Whoever wins more time will Conqueror!")
    print("3. Error input will lead to disqualification!\n")
    print("Indications:")
    print("------------")
    print("1. Rock -----> 'r'")
    print("2. Paper ----> 'p'")
    print("3. Scissor --> 's'")
    print("\n------------------")
    global user_name    # Permitting the function to rename the global variable
    user_name = input("What is your name? --> ")
    print("It's all!!!")
    sleep(1)
    print("•••••••••••••••••••••••••••")
    start_num = input("Enter 's' to start! --> ")
    return start_num

# Main Game Code --> Rock Paper Scissors Code
def rps_game():
    cls.cls()
    print(f"\nMatch between: '{user_name}' And 'PC'")
    pc_win = 0       # Win Counter for PC
    user_win = 0     # Win Counter for User
    round_num = 10   # Max Round = 10

    print()
    while (1):
        pc_rand = random.randint(1, 3)   # Taking a random integer

        # Integer values replaced by strings for game convenience
        if pc_rand == 1:
            pc_choice = 'r'
        elif pc_rand == 2:
            pc_choice = 'p'
        elif pc_rand == 3:
            pc_choice = 's'

        if (round_num > 0): # Continuation till round number 1
            print(f"Round number = {11 - round_num}")
            print("------------------\n")
            round_num -= 1
            user_choice = input("Your choice? --> ") # Taking user input as: r / p / s

            # user_choice = Rock ------------------------------------------------------------------------
            if (user_choice == 'r'):
                if (pc_choice == 'r'):  # pc_choice = Rock (DRAW)

                    print(f"     • '{user_name}' selected 'Rock'\n     • 'PC' selected 'Rock'\n"
                          f"     • Round '{10 - round_num}' Result --> Draw!!\n")
                    # No Point

                elif (pc_choice == 'p'):  # pc_choice = Paper (PC WON)
                    print(f"     Ohh!!\n     • '{user_name}' selected 'Rock'\n"
                          f"     • 'PC' selected 'Paper'\n"
                          f"     • Round {10 - round_num} Result --> 'PC' Won!!\n")
                    pc_win += 1     # Win Counter for PC increases by 1

                elif (pc_choice == 's'):  # pc_choice = Scissor (USER WON)
                    print(f"     Yess!!\n     • '{user_name}' selected 'Rock'\n"
                          f"     • 'PC' selected 'Scissor'\n"
                          f"     • Round {10 - round_num} Result --> '{user_name}' Won!!\n")
                    user_win += 1   # Win Counter for User increases by 1

            # user_choice = Paper -------------------------------------------------------------------------
            elif (user_choice == 'p'):
                if (pc_choice == 'r'):  # pc_choice = Rock (USER WON)

                    print(f"     Yeh!!\n     • '{user_name}' selected 'Paper'\n"
                          f"     • 'PC' selected 'Rock'\n"
                          f"     • Round {10 - round_num} Result --> '{user_name}' Won!!\n")
                    user_win += 1   # Win Counter for User increases by 1

                elif (pc_choice == 'p'):  # pc_choice = Paper (DRAW)

                    print(f"     • '{user_name}' selected 'Paper'\n"
                          f"     • 'PC' selected 'Paper'\n"
                          f"     • Round '{10 - round_num}' Result --> Draw!!\n")
                    # No Point

                elif (pc_choice == 's'):  # pc_choice = Scissor (PC WON)

                    print(f"     Ahh!!\n     • '{user_name}' selected 'Paper'\n"
                          f"     • 'PC' selected 'Scissor'\n"
                          f"     • Round {10 - round_num} Result --> 'PC' Won!!\n")
                    pc_win += 1     # Win Counter for PC increases by 1

            # user_choice = Scissor ------------------------------------------------------------------------
            elif (user_choice == 's'):
                if (pc_choice == 'r'):  # pc_choice = Rock (PC WON)

                    print(f"     Ughh!!\n     • '{user_name}' selected 'Scissors'\n"
                          f"     • 'PC' selected 'Rock'\n"
                          f"     • Round {10 - round_num} Result --> 'PC' Won!!\n")
                    pc_win += 1     # Win Counter for PC increases by 1

                elif (pc_choice == 'p'):  # pc_choice = Paper (USER WON)

                    print(f"     Yay!!\n     • '{user_name}' selected 'Scissors'\n"
                          f"     • 'PC' selected 'Paper'\n"
                          f"     • Round {10 - round_num} Result --> '{user_name}' Won!!\n")
                    user_win += 1   # Win Counter for User increases by 1

                elif (pc_choice == 's'):  # pc_choice = Scissor (DRAW)

                    print(f"     • '{user_name}' selected 'Scissors'\n"
                          f"     • 'PC' selected 'Scissors'\n"
                          f"     • Round '{10 - round_num}' Result --> Draw!!\n")
                    # No Point

            else:  # Error input (PC WON)

                print(f"     Shhh!!! Error input!!\n"
                      f"     • Round {10 - round_num} Result --> 'PC' Won!!\n")
                pc_win += 1     # Win Counter for PC increases by 1

        else:   # Conclusion as well as Winner selection part
            print("All round ended!!")
            sleep(1)
            print("It's result time!!!")
            print("•••", end="")
            sleep(1)
            print("•••••", end="")
            sleep(1)
            print("\b\b\b", end="")
            sleep(1)
            print("••••••••", end="")
            sleep(1)
            print("\b\b\b\b\b\b", end="")
            sleep(1)
            print("••••••••••••••\n")
            sleep(2)

            # Game Stats after the end of a session.
            print("Conclusion:")
            print("-----------")
            print(f"  • 'PC' won = '{pc_win}' Rounds")
            print(f"  • '{user_name}' won = '{user_win}' Rounds")
            print(f"  • DRAW = '{10 - pc_win - user_win}' Rounds")

            if pc_win > user_win:   # PC wining statement
                print("\n--------------------------")
                print("  'PC' is the 'Conqueror'")
                print("--------------------------\n")

            elif user_win > pc_win:     # User wining statement
                print("\n-------------------------------")
                print(f"   '{user_name}' is the 'Conqueror'")
                print("-------------------------------\n")

            else:   # Match Draw statement
                print("\n-----------------------")
                print("  This Match is a Draw!!")
                print("-----------------------\n")

            # Asking statement for Continuation
            desire = input("Press 'X' to Exit\nPress 'C' to Continue\n"
                           "-----------------------\nYour Choice? --> ")
            if (desire == 'x' or desire == 'X'):
                return 1
            else:
                return 0

# Driver Code
# Game Heading Display
print("••••••••••••••••••••••••••••••••••")
print("!! •• ROCK • PAPER • SCISSOR •• !!")
print("••••••••••••••••••••••••••••••••••")

print("           PLAYER vs PC\n"
      "         Who will Conquer?")

print("----------------------------------\n")

# game_rule() function calling
if (game_rule() == 's' or game_rule() == 'S'):
    if (rps_game() == 0):   # rps_game() function calling
        rps_game()
    else:
        exit()  # Exit program, in case of return 1 by rps_game()
else:
    print("Wrong input!!\nTry Again!!")
    game_rule()     # Recalling game_rule() function in case of wrong input by user in start_num

#----END----
