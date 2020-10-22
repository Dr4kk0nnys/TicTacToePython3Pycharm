# TODO: Implement the winning / loosing logic
# TODO: Implement the switch player logic
# TODO: Debug and clean the code

# Initialize the field
field = []


# Takes the field array as parameter
def initialize_field(uninitialized_field):
    for i in range(9):
        uninitialized_field.append(' ')


# Get the user input
def get_user_input():
    return input('1 to 9: ')


# Returns True if everything is okay, False, if some error found
def check_user_input(input_=''):
    # '', < 8, > 0, ['X']
    if input_ == '':
        return False

    if not input_.isnumeric():
        return False

    integer_input = int(input_)
    if not 9 >= integer_input >= 1:
        return False

    # -1 is the standard input decrease value
    if field[integer_input - 1] != ' ':
        return False

    return True


def draw_field(field_):
    temp_field = ''

    for i in range(len(field_)):
        temp_field += f'{field_[i]} | '

        if (i + 1) % 3 == 0:
            temp_field += '\n'

    print(temp_field)


def handle_incorrect_user_input():

    while True:
        print('Incorrect user input!')

        new_input = get_user_input()

        if check_user_input(new_input):
            return new_input


if __name__ == '__main__':
    initialize_field(field)

    while True:
        user_input = get_user_input()

        if not check_user_input(user_input):
            user_input = handle_incorrect_user_input()

        field[int(user_input) - 1] = 'X'

        draw_field(field)


# Turn of the other player
