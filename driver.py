"""
Andrew Lai
Mini-Roulette
"""

import random
from colorama import Fore, Style

wheel = [11, 3, 7, 8, 0, 2, 12, 6, 10, 4, 5, 9, 1, 11, 3, 7, 8, 0, 2, 12, 6]
reds = [1, 3, 5, 8, 10, 12]
string_reds = ['1', '3', '5', '8', '10', '12']
blacks = [2, 4, 6, 7, 9, 11]
string_blacks = ['2', '4', '6', '7', '9', '11']
switch_codes = ['red', 'black', 'high', 'low', 'odd', 'even', 'row1', 'row2', 'row3', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
help_codes = ['codes', 'help', 'odds']


# Prints out the numbers in their appropriate colour. Note that in dark mode, black may come out as white.
# end='' used to print on same line.
def colour_print(num):
    num = str(num)
    if num == '0':
        print(Fore.GREEN + num, end=' ')
    elif num in string_reds:
        print(Fore.RED + num, end=' ')
    else:
        print(Fore.BLACK + num, end=' ')
    return ""


# Checks if given number is within range
def range_check(lower, upper):
    while 1:
        num = input()
        if num.isnumeric() is False:
            print("Please enter in a whole number. ", end='')
        elif int(num) < lower or int(num) > upper:
            print(f"Please try again with a number between {lower} and {upper} inclusive. ", end='')
        else:
            return int(num)


# Prints the betting field
def print_felt():
    print("  ", end='')
    print(f"{colour_print('1')} {colour_print('4')} {colour_print('7')} {colour_print('10')}")
    print(f"{colour_print('0')} {colour_print('2')}  {colour_print('5')}  {colour_print('8')}  {colour_print('11')}")
    print("  ", end='')
    print(f"{colour_print('3')}  {colour_print('6')}  {colour_print('9')}  {colour_print('12')}")
    print(Style.RESET_ALL)


# Prints codes used to bet
def print_betting_codes():
    print("\n[BETTING CODES]")
    print("Red/Black: red / black")
    print("Odd/Even: odd / even")
    print("Low [1-6]: low")
    print("High [7-12]: high")
    print("Rows top to bottom: row1 / row2 / row3")
    print("Straight up number: 0 / 1 / 2...\n")


# Prints the how to play
def print_help():
    print("\n[HELP]")
    print("Playing roulette is fun and easy!")
    print("To place a bet, type in the betting code then Enter. The next prompt will ask for the amount of bet.")
    print("For example, 'red', Enter, '100', Enter would put a bet of ¤100 on red.")
    print("A bet is paid out according to the odds table if the winning number is covered by the bet.")
    print("The only bet that wins on 0 is a straight up bet on 0.")
    print("You can only bet whole numbers of ¤.")
    print("You may not place bets that exceed your current balance.\n")


# Prints the prizing structure
def print_odds():
    print("\n[ODDS]")
    print("Red, Black, Odd, Even, High, Low: 1:1")
    print("Row:                              2:1")
    print("Straight up:                     11:1\n")


# Translates betting codes into indices of the betting array
# [0,1,2,...,12,red,black,odd,even,high,low,r1,r2,r3]
def translate(place):
    if place == 'red':
        return 13
    elif place == 'black':
        return 14
    elif place == 'odd':
        return 15
    elif place == 'even':
        return 16
    elif place == 'high':
        return 17
    elif place == 'low':
        return 18
    elif place == 'row1':
        return 19
    elif place == 'row2':
        return 20
    elif place == 'row3':
        return 21
    else:
        return int(place)


# Translates indices in the array back to betting codes
def reverse_translate(place):
    if 0 <= place <= 12:
        return place
    elif place == 13:
        return 'red'
    elif place == 14:
        return 'black'
    elif place == 15:
        return 'odd'
    elif place == 16:
        return 'even'
    elif place == 17:
        return 'high'
    elif place == 18:
        return 'low'
    elif place == 19:
        return 'row1'
    elif place == 20:
        return 'row2'
    else:
        return 'row3'


# Checks if the menu input is within the list of acceptable inputs
def menu_input():
    # Asks for choice until valid selection
    while 1:
        query = input().lower()
        if query in help_codes:
            if query == 'codes':
                print_betting_codes()
            elif query == 'help':
                print_help()
            else:
                print_odds()
        if query in switch_codes:
            return query
        else:
            if query in help_codes:
                print("Please enter in a betting code, or 'help', 'odds', or 'codes' for help. ", end='')
            else:
                print("Please try again: ", end='')


# returns array of won bets
def win_checker(winning_number, bet_array):
    # straight up bets
    for ind, val in enumerate(bet_array[:13]):
        if ind == winning_number:
            bet_array[ind] *= 12
        else:
            bet_array[ind] = 0

    # 0
    if winning_number == 0:
        for num in range(13, 22):
            bet_array[num] = 0
    else:
        # red/black
        if winning_number in reds:
            bet_array[13] *= 2
            bet_array[14] = 0
        else:
            bet_array[13] = 0
            bet_array[14] *= 2

        # odd/even
        if winning_number % 2 == 1:
            bet_array[15] *= 2
            bet_array[16] = 0
        else:
            bet_array[15] = 0
            bet_array[16] *= 2

        # high/low
        if winning_number > 6:
            bet_array[17] *= 2
            bet_array[18] = 0
        else:
            bet_array[17] = 0
            bet_array[18] *= 2

        # rows
        if winning_number % 3 == 1:
            bet_array[19] *= 3
            bet_array[20] = 0
            bet_array[21] = 0
        elif winning_number % 3 == 2:
            bet_array[19] = 0
            bet_array[20] *= 3
            bet_array[21] = 0
        else:
            bet_array[19] = 0
            bet_array[20] = 0
            bet_array[21] *= 3
    return bet_array


if __name__ == '__main__':

    balance = 10000
    bets = []
    bet_sum = 0
    total_win = 0

    # initialize bet array to all zeroes
    for _ in range(22):
        bets.append(0)

    print("Welcome to Mini Roulette! 92.3% RTP\n")

    # Print out the wheel and the betting layout
    print("The wheel:")
    for nn in wheel[4:-4]:
        colour_print(nn)
    print(Style.RESET_ALL)
    print("")

    print("The betting layout:")
    print_felt()
    print("You've been given ¤10000 to gamble!")

    # main loop. Continuously starts new rounds until broken out of when user wants to quit.

    while 1:
        print("\nPlease enter in a betting code, or 'help', 'odds', or 'codes' for help. ", end='')
        user_choice = menu_input()

        print(f"You have ¤{balance}. How much do you want to bet on {user_choice}? ", end='')
        bet_amount = range_check(0, balance)
        balance -= bet_amount
        bets[translate(user_choice)] = bet_amount
        bet_sum += bet_amount

        # If user has no currency left, forcibly start the game
        if balance == 0:
            stop = 'q'
            print("You're all in. Good luck!")

        # User can place additional bets on a single round
        else:
            stop = input("'q' to stop betting, anything else to bet more: ")

        # Generate the random number, and pay out the bets accordingly.
        # Winning number is computed outside the function so test cases can be created.
        if stop == "q":
            winning_number = random.randrange(0, 13)
            bets = win_checker(winning_number, bets)

            print(f"\nThe winning number is {winning_number}")

            # print the wheel. First find index of winning number, then print out the 4 numbers before and after.
            for index, num in enumerate(wheel[4:]):
                if num == winning_number:
                    win_index = index + 4
                    for num2 in wheel[win_index - 4:win_index]:
                        colour_print(num2)
                    print(Style.RESET_ALL, end='')
                    print("-> ", end='')
                    colour_print(wheel[win_index])
                    print(Style.RESET_ALL, end='')
                    print("<- ", end='')
                    for num3 in wheel[win_index + 1:win_index + 5]:
                        colour_print(num3)
                    print(Style.RESET_ALL, end='')
                    print("\n")
                    break

            # Print out the winning bets.
            for ind, val in enumerate(bets):
                total_win += val
                if val != 0:
                    print(f"Your bet on {reverse_translate(ind)} won ¤{val}!")

            # Add winnings to balance, and display a summary of financial status
            balance += total_win
            print(f"Total bet: ¤{bet_sum} \nTotal won: ¤{total_win}\nYour new balance: ¤{balance}")

            # Go again? Game forcibly ends if balance is 0.
            if balance != 0:
                again = input("Do you want to go again? 'q' to stop, anything else to go again: ")
            else:
                break

            # Clear previous bets
            if again != 'q':
                bet_sum = 0
                total_win = 0

                for i, v in enumerate(bets):
                    bets[i] = 0
                print(f"\nYour balance is ¤{balance}.", end='')

            # If not end
            else:
                break

    if balance != 0:
        print(f"\nYou walked out with ¤{balance}. Please come again!")
    else:
        print("\nYou've been bankrupted! Please come again!")
