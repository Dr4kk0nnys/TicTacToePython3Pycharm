from exceptions import IncorrectUsageException


# TODO: Implement the winning / loosing logic
# TODO: Implement the switch player logic
# TODO: Debug and clean the code

# Initialize the field
field = []
players = ['X', 'O']

# if count is odd,  the player will be 'O'
# if count is even, the player will be 'X'
count = 0


# Takes the field array as parameter
def initialize_field(uninitialized_field):
    for i in range(9):
        uninitialized_field.append(' ')


# Get the user input
def get_user_input():
    return input('1 to 9: ')


# Returns True if everything is okay, raises an exception, if some error found
def check_user_input(input_=''):
    # Possible Error: empty value: ''
    # Possible Error: value is bigger than 8
    # Possible Error: value is smaller than 0
    # Possible Error: value is already filled

    if input_ == '':
        raise IncorrectUsageException('Input cannot be empty!')

    if not input_.isnumeric():
        raise IncorrectUsageException('Input must be a string!')

    integer_input = int(input_)
    if not 9 >= integer_input >= 1:
        raise IncorrectUsageException('Input must be bigger than or equals to 1! \n' +
                                      'Input must be smaller than or equals to 9')

    # -1 is the standard input decrease value
    if field[integer_input - 1] != ' ':
        raise IncorrectUsageException('Input cannot be place in an already filled spot!')

    return True


def draw_field(field_):
    temp_field = ''

    for i in range(len(field_)):
        temp_field += f'{field_[i]} | '

        if (i + 1) % 3 == 0:
            temp_field += '\n'

    print(temp_field)


def handle_user_input():
    input_ = get_user_input()
    while True:
        try:
            check_user_input(input_)
            return input_
        except IncorrectUsageException as e:
            print(e.message)

            input_ = get_user_input()


def get_player(player_count):
    if (player_count % 2) == 0:
        return players[0]
    return players[1]


if __name__ == '__main__':

    initialize_field(field)

    while True:
        user_input = handle_user_input()

        # -1 allows the user to play with 1 ~ 9 index
        field[int(user_input) - 1] = get_player(count)

        count += 1

        draw_field(field)
