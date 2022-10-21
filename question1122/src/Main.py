
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
# f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = False  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    # we are defining seperate boards for both of the players
    my_list_p1 = [['-' for a in range(board_size)] for b in range(board_size)], [['-' for a in range(board_size)] for b
                                                                                 in range(board_size)]
    my_list_p2 = [['-' for a in range(board_size)] for b in range(board_size)], [['-' for a in range(board_size)] for b
                                                                                 in range(board_size)]
    # we are defining lists of ships, lowercased one is for input controlling
    ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    ships_lower = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
    # we will adjust the list for player 1 in a while loop which works when it is not confirmed
    non_confirmation = True
    while non_confirmation:
        # when there are no ships left in the list this loop will stop working and the player will be sent to confirmation stage
        while ships != []:
            print_3d_list(my_list_p1)
            print_ships_to_be_placed()
            # with this for loop we are printing the ships left on the list
            for ship in ships:
                print_single_element(ship)
            # this part takes the input from player and shows their ships left etc.
            print_empty_line()
            print_player_turn_to_place(1)
            print_to_place_ships()
            inp = input().lower()
            inp_list = inp.split()
            # the try makes sure that the coordinates given are in correct format, otherwise it gives error
            try:
                int(inp_list[1])
                int(inp_list[2])
                # this if statement makes sure that we are provided with sufficient input
                if len(inp_list) >= 4:
                    # this if statement makes sure that the coordinates given exist on the board
                    if 0 < int(inp_list[1]) <= 10 and 0 < int(inp_list[2]) <= 10:
                        # this if statement makes sure that the ship name given is legal
                        if inp_list[0] in ships_lower:
                            # this if statement checks which are we working with, in this case it is carrier
                            if inp_list[0] == 'carrier':
                                # this if statement makes sure that the ship is not placed yet
                                if 'Carrier' in ships:
                                    # this if statement makes sure that the orientation written is legal
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        # this if statement checks which orientation we are working with, in this case it is horizontal
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            # this is statement makes sure there are no ships on the points that player wants to put their ship
                                            if column + 3 <= 9:
                                                if '#' not in my_list_p1[0][line - 1][column - 1:column + 4]:
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line - 1][column] = '#'
                                                    my_list_p1[0][line - 1][column + 1] = '#'
                                                    my_list_p1[0][line - 1][column + 2] = '#'
                                                    my_list_p1[0][line - 1][column + 3] = '#'
                                                    # with this remove statement we are deleting the placed ship from our list, so they cannot be out more than once
                                                    ships.remove('Carrier')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Carrier')
                                            else:
                                                print_ship_cannot_be_placed_outside('Carrier')
                                        # we are doing the same things we did for horizontal, this time for vertical
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 3 <= 9:
                                                if my_list_p1[0][line - 1][column - 1] != '#' and my_list_p1[0][line][
                                                    column - 1] != '#' and my_list_p1[0][line + 1][
                                                    column - 1] != '#' and my_list_p1[0][line + 2][
                                                    column - 1] != '#' and my_list_p1[0][line + 3][column - 1] != '#':
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line][column - 1] = '#'
                                                    my_list_p1[0][line + 1][column - 1] = '#'
                                                    my_list_p1[0][line + 2][column - 1] = '#'
                                                    my_list_p1[0][line + 3][column - 1] = '#'
                                                    ships.remove('Carrier')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Carrier')
                                            else:
                                                print_ship_cannot_be_placed_outside('Carrier')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Carrier')
                            # we are doing the same things we did for carrier, this time for battleship
                            elif inp_list[0] == 'battleship':
                                if 'Battleship' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 2 <= 9:
                                                if '#' not in my_list_p1[0][line - 1][column - 1:column + 3]:
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line - 1][column] = '#'
                                                    my_list_p1[0][line - 1][column + 1] = '#'
                                                    my_list_p1[0][line - 1][column + 2] = '#'
                                                    ships.remove('Battleship')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Battleship')
                                            else:
                                                print_ship_cannot_be_placed_outside('Battleship')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 2 <= 9:
                                                if my_list_p1[0][line - 1][column - 1] != '#' and my_list_p1[0][line][
                                                    column - 1] != '#' and my_list_p1[0][line + 1][
                                                    column - 1] != '#' and my_list_p1[0][line + 2][column - 1] != '#':
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line][column - 1] = '#'
                                                    my_list_p1[0][line + 1][column - 1] = '#'
                                                    my_list_p1[0][line + 2][column - 1] = '#'
                                                    ships.remove('Battleship')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Battleship')
                                            else:
                                                print_ship_cannot_be_placed_outside('Battleship')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Battleship')
                            # we are doing the same things we did for carrier, this time for submarine
                            elif inp_list[0] == 'submarine':
                                if 'Submarine' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 1 <= 9:
                                                if '#' not in my_list_p1[0][line - 1][column - 1:column + 2]:
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line - 1][column] = '#'
                                                    my_list_p1[0][line - 1][column + 1] = '#'
                                                    ships.remove('Submarine')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Submarine')
                                            else:
                                                print_ship_cannot_be_placed_outside('Submarine')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 1 <= 9:
                                                if my_list_p1[0][line - 1][column - 1] != '#' and my_list_p1[0][line][
                                                    column - 1] != '#' and my_list_p1[0][line + 1][column - 1] != '#':
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line][column - 1] = '#'
                                                    my_list_p1[0][line + 1][column - 1] = '#'
                                                    ships.remove('Submarine')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Submarine')
                                            else:
                                                print_ship_cannot_be_placed_outside('Submarine')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Submarine')
                            # we are doing the same things we did for carrier, this time for cruiser
                            elif inp_list[0] == 'cruiser':
                                if 'Cruiser' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 1 <= 9:
                                                if '#' not in my_list_p1[0][line - 1][column - 1:column + 2]:
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line - 1][column] = '#'
                                                    my_list_p1[0][line - 1][column + 1] = '#'
                                                    ships.remove('Cruiser')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Cruiser')
                                            else:
                                                print_ship_cannot_be_placed_outside('Cruiser')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 1 <= 9:
                                                if my_list_p1[0][line - 1][column - 1] != '#' and my_list_p1[0][line][
                                                    column - 1] != '#' and my_list_p1[0][line + 1][column - 1] != '#':
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line][column - 1] = '#'
                                                    my_list_p1[0][line + 1][column - 1] = '#'
                                                    ships.remove('Cruiser')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Cruiser')
                                            else:
                                                print_ship_cannot_be_placed_outside('Cruiser')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Cruiser')
                            # we are doing the same things we did for carrier, this time for destroyer
                            elif inp_list[0] == 'destroyer':
                                if 'Destroyer' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column <= 9:
                                                if '#' not in my_list_p1[0][line - 1][column - 1:column + 1]:
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line - 1][column] = '#'
                                                    ships.remove('Destroyer')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Destroyer')
                                            else:
                                                print_ship_cannot_be_placed_outside('Destroyer')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line <= 9:
                                                if my_list_p1[0][line - 1][column - 1] != '#' and my_list_p1[0][line][
                                                    column - 1] != '#':
                                                    my_list_p1[0][line - 1][column - 1] = '#'
                                                    my_list_p1[0][line][column - 1] = '#'
                                                    ships.remove('Destroyer')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Destroyer')
                                            else:
                                                print_ship_cannot_be_placed_outside('Destroyer')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Destroyer')
                        else:
                            print_incorrect_ship_name()
                    else:
                        print_incorrect_coordinates()
                else:
                    print_incorrect_input_format()
            except:
                print_incorrect_input_format()
        print_3d_list(my_list_p1)
        # this is the confirmation stage
        temp = True
        while temp:
            print_confirm_placement()
            conf = input().lower()
            # when input is 'y' we are getting out of this loop, and moving to player 2
            if conf == 'y':
                temp = False
                non_confirmation = False
            # when input is 'n' we are sending the player back to placement stage by changing the non_confirmation
            elif conf == 'n':
                temp = False
                non_confirmation = True
                # we are redefining the ships and the board because they were changed
                ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                my_list_p1 = [['-' for a in range(board_size)] for b in range(board_size)], [
                    ['-' for a in range(board_size)] for b in range(board_size)]
            # we are asking for confirmation again in case the input is not correct
            else:
                temp = True
    # we are doing the exact same things we did for player 1
    # the differences are the name of the list and the first index of the list on placement stage because player 2 uses the right side of the board
    ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    ships_lower = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
    non_confirmation = True
    while non_confirmation:
        while ships != []:
            print_3d_list(my_list_p2)
            print_ships_to_be_placed()
            for ship in ships:
                print_single_element(ship)
            print_empty_line()
            print_player_turn_to_place(2)
            print_to_place_ships()
            inp = input().lower()
            inp_list = inp.split()
            try:
                int(inp_list[1])
                int(inp_list[2])
                if len(inp_list) >= 4:
                    if 0 < int(inp_list[1]) <= 10 and 0 < int(inp_list[2]) <= 10:
                        if inp_list[0] in ships_lower:
                            if inp_list[0] == 'carrier':
                                if 'Carrier' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 3 <= 9:
                                                if not '#' in my_list_p2[1][line - 1][column - 1:column + 4]:
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line - 1][column] = '#'
                                                    my_list_p2[1][line - 1][column + 1] = '#'
                                                    my_list_p2[1][line - 1][column + 2] = '#'
                                                    my_list_p2[1][line - 1][column + 3] = '#'
                                                    ships.remove('Carrier')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Carrier')
                                            else:
                                                print_ship_cannot_be_placed_outside('Carrier')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 3 <= 9:
                                                if my_list_p2[1][line - 1][column - 1] != '#' and my_list_p2[1][line][
                                                    column - 1] != '#' and my_list_p2[1][line + 1][
                                                    column - 1] != '#' and my_list_p2[1][line + 2][
                                                    column - 1] != '#' and my_list_p2[1][line + 3][column - 1] != '#':
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line][column - 1] = '#'
                                                    my_list_p2[1][line + 1][column - 1] = '#'
                                                    my_list_p2[1][line + 2][column - 1] = '#'
                                                    my_list_p2[1][line + 3][column - 1] = '#'
                                                    ships.remove('Carrier')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Carrier')
                                            else:
                                                print_ship_cannot_be_placed_outside('Carrier')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Carrier')
                            elif inp_list[0] == 'battleship':
                                if 'Battleship' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 2 <= 9:
                                                if not '#' in my_list_p2[1][line - 1][column - 1:column + 3]:
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line - 1][column] = '#'
                                                    my_list_p2[1][line - 1][column + 1] = '#'
                                                    my_list_p2[1][line - 1][column + 2] = '#'
                                                    ships.remove('Battleship')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Battleship')
                                            else:
                                                print_ship_cannot_be_placed_outside('Battleship')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 2 <= 9:
                                                if my_list_p2[1][line - 1][column - 1] != '#' and my_list_p2[1][line][
                                                    column - 1] != '#' and my_list_p2[1][line + 1][
                                                    column - 1] != '#' and my_list_p2[1][line + 2][column - 1] != '#':
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line][column - 1] = '#'
                                                    my_list_p2[1][line + 1][column - 1] = '#'
                                                    my_list_p2[1][line + 2][column - 1] = '#'
                                                    ships.remove('Battleship')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Battleship')
                                            else:
                                                print_ship_cannot_be_placed_outside('Battleship')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Battleship')
                            elif inp_list[0] == 'submarine':
                                if 'Submarine' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 1 <= 9:
                                                if not '#' in my_list_p2[1][line - 1][column - 1:column + 2]:
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line - 1][column] = '#'
                                                    my_list_p2[1][line - 1][column + 1] = '#'
                                                    ships.remove('Submarine')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Submarine')
                                            else:
                                                print_ship_cannot_be_placed_outside('Submarine')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 1 <= 9:
                                                if my_list_p2[1][line - 1][column - 1] != '#' and my_list_p2[1][line][
                                                    column - 1] != '#' and my_list_p2[1][line + 1][column - 1] != '#':
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line][column - 1] = '#'
                                                    my_list_p2[1][line + 1][column - 1] = '#'
                                                    ships.remove('Submarine')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Submarine')
                                            else:
                                                print_ship_cannot_be_placed_outside('Submarine')
                                else:
                                    print_ship_is_already_placed('Submarine')
                            elif inp_list[0] == 'cruiser':
                                if 'Cruiser' in ships:
                                    if inp_list[3] == 'h' or inp_list[3] == 'v':
                                        if inp_list[3] == 'h':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if column + 1 <= 9:
                                                if not '#' in my_list_p2[1][line - 1][column - 1:column + 2]:
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line - 1][column] = '#'
                                                    my_list_p2[1][line - 1][column + 1] = '#'
                                                    ships.remove('Cruiser')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Cruiser')
                                            else:
                                                print_ship_cannot_be_placed_outside('Cruiser')
                                        elif inp_list[3] == 'v':
                                            column = int(inp_list[1])
                                            line = int(inp_list[2])
                                            if line + 1 <= 9:
                                                if my_list_p2[1][line - 1][column - 1] != '#' and my_list_p2[1][line][
                                                    column - 1] != '#' and my_list_p2[1][line + 1][column - 1] != '#':
                                                    my_list_p2[1][line - 1][column - 1] = '#'
                                                    my_list_p2[1][line][column - 1] = '#'
                                                    my_list_p2[1][line + 1][column - 1] = '#'
                                                    ships.remove('Cruiser')
                                                else:
                                                    print_ship_cannot_be_placed_occupied('Cruiser')
                                            else:
                                                print_ship_cannot_be_placed_outside('Cruiser')
                                    else:
                                        print_incorrect_orientation()
                                else:
                                    print_ship_is_already_placed('Cruiser')
                            elif inp_list[0] == 'destroyer':
                                if 'Destroyer' in ships:
                                    if inp_list[3] == 'h':
                                        column = int(inp_list[1])
                                        line = int(inp_list[2])
                                        if column <= 9:
                                            if not '#' in my_list_p2[1][line - 1][column - 1:column + 1]:
                                                my_list_p2[1][line - 1][column - 1] = '#'
                                                my_list_p2[1][line - 1][column] = '#'
                                                ships.remove('Destroyer')
                                            else:
                                                print_ship_cannot_be_placed_occupied('Destroyer')
                                        else:
                                            print_ship_cannot_be_placed_outside('Destroyer')
                                    elif inp_list[3] == 'v':
                                        column = int(inp_list[1])
                                        line = int(inp_list[2])
                                        if line <= 9:
                                            if my_list_p2[1][line - 1][column - 1] != '#' and my_list_p2[1][line][
                                                column - 1] != '#':
                                                my_list_p2[1][line - 1][column - 1] = '#'
                                                my_list_p2[1][line][column - 1] = '#'
                                                ships.remove('Destroyer')
                                            else:
                                                print_ship_cannot_be_placed_occupied('Destroyer')
                                        else:
                                            print_ship_cannot_be_placed_outside('Destroyer')
                                else:
                                    print_ship_is_already_placed('Destroyer')
                        else:
                            print_incorrect_ship_name()
                    else:
                        print_incorrect_coordinates()
                else:
                    print_incorrect_input_format()
            except:
                print_incorrect_input_format()
        print_3d_list(my_list_p2)
        # the same confirmation procedure for player 2
        temp = True
        while temp:
            print_confirm_placement()
            conf = input().lower()
            if conf == 'y':
                temp = False
                non_confirmation = False
            elif conf == 'n':
                temp = False
                non_confirmation = True
                ships = ['Carrier', 'Battleship', 'Submarine', 'Cruiser', 'Destroyer']
                my_list_p2 = [['-' for a in range(board_size)] for b in range(board_size)], [
                    ['-' for a in range(board_size)] for b in range(board_size)]
            else:
                temp = True
    # we are moving to battle phase
    # we are defining numbers of hits for the players as 0
    # the while loop will keep working unless game_on is defined as False
    hit1 = 0
    hit2 = 0
    game_on = True
    while game_on:
        turn1 = True
        # while turn1 is true, this loop will keep working and the attacker will be player 1
        while turn1:
            print_3d_list(my_list_p1)
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            target = input().split()
            # this try statement makes sure that the first 2 parts of the input given are in correct format
            try:
                for num in target[:2]:
                    s_column = int(target[0])
                    s_line = int(target[1])
                # this if statement makes sure that we are provided with coordinates that exist on our board
                if 0 < s_column <= 10 and 0 < s_line <= 10:
                    # this is statement works if the attacked place is empty
                    if my_list_p2[1][s_line - 1][s_column - 1] == '-':
                        print_miss()
                        my_list_p2[1][s_line - 1][s_column - 1] = 'O'
                        my_list_p1[1][s_line - 1][s_column - 1] = 'O'
                        temp = True
                        # with this while loop we are asking the player to yield
                        while temp:
                            print_type_done_to_yield(2)
                            yielder = input().lower().strip()
                            # this if statement works if the player confirms and it gives the turn to other player
                            if yielder == 'done':
                                turn2 = True
                                turn1 = False
                                temp = False
                                break
                            # this else statement asks the player again to yield
                            else:
                                temp = True
                    # this elif statement works if the attacked place is occupied and it increases the number of hits by 1
                    elif my_list_p2[1][s_line - 1][s_column - 1] == '#':
                        print_hit()
                        my_list_p2[1][s_line - 1][s_column - 1] = '!'
                        my_list_p1[1][s_line - 1][s_column - 1] = '!'
                        hit1 += 1
                        # this if statement works when the player hits all the 17 spots that is occupied by the other player and wins, prints player won and breaks out of the loop
                        if hit1 == 17:
                            print_3d_list(my_list_p1)
                            print_player_won(1)
                            print_thanks_for_playing()
                            game_on = False
                            break
                    # this elif statement works when the player tries to strike a point that they have already struck
                    elif my_list_p2[1][s_line - 1][s_column - 1] == 'O' or my_list_p2[1][s_line - 1][
                        s_column - 1] == '!':
                        print_tile_already_struck()
                else:
                    print_incorrect_coordinates()
            except:
                print_incorrect_input_format()
        # we are doing the exact same thing that we did for player 1 to strike
        while turn2:
            print_3d_list(my_list_p2)
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            target = input().split()
            try:
                for num in target[:2]:
                    s_column = int(target[0])
                    s_line = int(target[1])
                if 0 < s_column <= 10 and 0 < s_line <= 10:
                    if my_list_p1[0][s_line - 1][s_column - 1] == '-':
                        print_miss()
                        my_list_p1[0][s_line - 1][s_column - 1] = 'O'
                        my_list_p2[0][s_line - 1][s_column - 1] = 'O'
                        temp = True
                        while temp:
                            print_type_done_to_yield(1)
                            yielder = input().lower().strip()
                            if yielder == 'done':
                                turn1 = True
                                turn2 = False
                                temp = False
                                break
                            else:
                                temp = True
                    elif my_list_p1[0][s_line - 1][s_column - 1] == '#':
                        print_hit()
                        my_list_p2[0][s_line - 1][s_column - 1] = '!'
                        my_list_p1[0][s_line - 1][s_column - 1] = '!'
                        hit2 += 1
                        if hit2 == 17:
                            print_3d_list(my_list_p2)
                            print_player_won(2)
                            print_thanks_for_playing()
                            game_on = False
                            break
                    elif my_list_p1[0][s_line - 1][s_column - 1] == 'O' or my_list_p1[0][s_line - 1][
                        s_column - 1] == '!':
                        print_tile_already_struck()
                else:
                    print_incorrect_coordinates()
            except:
                print_incorrect_input_format()


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

