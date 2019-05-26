import sys
import re

def print_table(table):
    #
    # Show Board
    #
    print('-------')
    for i in range(3):
        line = " "
        for j in range(3):
            line = line + str(table[i][j]) + " "

        print(line)
        print('-------')


def input_command(table, turn):
    #
    # Caught user's input
    #
    reg = re.compile('^\s*([0-2]),([0-2])')

    while True:

        command_number = 0

        if turn % 2 == 0:
            print(">>> The First Move's " + str(turn + 1) + " Turn:")
            command_number = 1
        else:
            print(">>> The Second Move's " + str(turn + 1) + " Turn:")
            command_number = 2

        print(">>> Input your command as address.(e.g. 0,2 )：")

        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not line:
            break

        match = reg.search(line)

        if(match):

            if int(match.group(1)) < 0 or 2 < int(match.group(1)):
                print(">>> Error. Invalid first number.")
                continue

            if int(match.group(2)) < 0 or 2 < int(match.group(2)):
                print(">>> Error. Invalid secnod number.")
                continue

            if table[int(match.group(1))][int(match.group(2))] != 0:
                print(">>> Error. Invalid address.")
                continue

            table[int(match.group(1))][int(match.group(2))] \
                = command_number

            break

        print('===')
        print(line)
        print('===')
        if line.rstrip() == 'Quit':
            if turn % 2 == 0:
                print(">>> The First Move quits. The Second Move won in " + str(turn + 1) + " turn.")
            else:
                print(">>> The Second Move quits. The First Move won in " + str(turn + 1) + " turn.")

            sys.exit()

        print(">>> Input Error. Try again..")


def win_or_lose(table, turn):

    for i in range(3):
        if table[i][0] == table[i][1] and table[i][1] == table[i][2] \
           and table[i][0] != 0:
            return table[i][0]

        if table[0][i] == table[1][i] and table[1][i] == table[2][i] \
           and table[0][i] != 0:
            return table[0][1]

    if table[0][0] == table[1][1] and table[1][1] == table[2][2] \
       and table[0][0] != 0:
        return table[0][0]

    if table[0][2] == table[1][1] and table[1][1] == table[2][0] \
       and table[0][2] != 0:
        return table[0][2]

    return 0


def print_state(game_state, turn):

    print(">>> Game is ended.")

    if game_state == 1:
        print(">>> The First Move won in " + str(turn+1) + " turns.")

    elif game_state == 2:
        print(">>> The Second Move won in " + str(turn+1) + " turns.")

    else:
        print(">>> Draw.")


def game(table):

    # Initialize board
    table = []
    for i in range(3):
        table.append([0]*3)

    # Process turns
    for turn in range(9):

        input_command(table, turn)

        print_table(table)

        result = win_or_lose(table, turn)
        if result != 0:
            return result, turn

    # Draw
    return 0, None

# Board Data
table = None

# Run game and got status 0:Draw 1:The first won 2:The second won
game_state, turn = game(table)

# Show result
print_state(game_state, turn)
