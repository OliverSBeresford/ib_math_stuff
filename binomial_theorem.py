import math

def n_choose_r(n, r) -> int:
    '''
    Gets the number of combinations of r choices in n options
    '''
    return math.comb(n, r)

def print_pascal_triangle(numLines) -> None:
    '''
    Prints numLines lines of the pascal triangle to the terminal
    '''
    # Width that each number will take up, regardless of how many digits it is
    num_width = len(str(math.comb(numLines - 1, numLines // 2)))
    # Total width of the longest line including spaces
    width = (numLines - 1) * (num_width + 1) + 1

    # Printing the first '1' in the center for visual effect
    print('1'.center(width))

    # Used for storing the previous lines to do the math on them (nope I'm not using math.comb deal with it)
    previousLine = []
    currentLine = [1]
    # Prints every line starting after the first, which was just 1
    for line in range(2, numLines + 1):
        previousLine = currentLine

        # Every line has a 1 as the first item
        currentLine = []
        currentLine.append(1)

        # Calculating numbers for the current line
        for col in range(1, line - 1):
            value = previousLine[col - 1] + previousLine[col]
            currentLine.append(value)

        # Making a string with all the numbers fitted into a certain number of characters each
        formatted_line = ''.join([f'{num:<{num_width + 1}}' for num in currentLine])

        # Add a 1 (we didn't count this in the formatting because the last one doesn't need extra spaces)
        currentLine.append(1)
        formatted_line += '1'

        # Putting the formatted string in the middle with regard to the longest line
        print(formatted_line.center(width))


def get_pascal_triangle_row(row) -> list:
    '''
    Returns a single row of the pascal triangle as a list
    '''
    number = row
    result = [0] * number

    for col in range(number):
        result[col] = n_choose_r(number, col)

    return result

def isNaN(string):
    '''Return True if the number is not a number and false if it is a number'''
    try:
        float(string)
        return False
    except:
        return True

def get_number(msg, error):
    '''
    Gets a number
        msg: Message to prompt the use for input
        error: Message given to prompt the user for input after they gave an invalid input
    '''
    num = input(msg + '\n>')
    while isNaN(num):
        num = input(error + '\n>')
    
    return float(num)

def get_char(msg, error):
    '''
    Gets one character
        msg: Message to prompt the use for input
        error: Message given to prompt the user for input after they gave an invalid input
    '''
    char = input(msg + '\n>')
    while type(char) != str or len(char) != 1:
        char = input(error + '\n>')

    return char

def binomial_theorem(power) -> None:
    # All the coefficients we'll need for the final thing using the binomial theorem
    coefficients = get_pascal_triangle_row(power + 1)

    coeff1_1 = get_number('Enter the coefficient for the first variable', 'Must be a number')
    coeff2_1 = get_char('Enter the first variable (1 for nothing)', 'Must be a letter or 1')
    coeff2_1 = '' if coeff2_1 == '1' else coeff2_1

    coeff1_2 = get_number('Enter the coefficient for the second variable', 'Must be a number')
    coeff2_2 = get_char('Enter the first variable (1 for nothing)', 'Must be a letter or 1')
    coeff2_2 = '' if coeff2_2 == '1' else coeff2_2

    # Prints the given equation (like (a + b)^2 = ...)
    print(f'({coeff1_1}{coeff2_1} + {str(coeff1_2)}{coeff2_2})^{power} = ', end='')

    index = 0
    for i in range(power + 1):
        # Coefficient of the element
        coefficient = n_choose_r(power, index) * math.pow(coeff1_1, power - index) * math.pow(coeff1_2, index)
        # Power of first variable (descending)
        power_1 = '' if power - index == 0 or coeff2_1 == '' else coeff2_1 if power - index == 1 else coeff2_1 + '^' + str(power - index)
        power_1 = f'({power_1})' if len(power_1) > 1 else power_1
        # Power of first variable (ascending)
        power_2 = '' if index == 0 or coeff2_2 == '' else coeff2_2 if index == 1 else coeff2_2 + '^' + str(index)
        power_2 = f'({power_2})' if len(power_2) > 1 else power_2

        print(f'{coefficient}{power_1}{power_2}', end='')

        index += 1
        
        # Don't add the + if it's the last element
        if i != power:
            print(' + ', end='')
        else:
            print()


binomial_theorem(6)
