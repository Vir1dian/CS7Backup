def aligner(width, a, b, dollar_sign=None, dollar_space=None):
    if dollar_sign:
        b = dollar_sign + ' '*(dollar_space + 2 - len(b)) + b
        # dollar_sign must be used with dollar_space to create an even line of dollar signs
        # dollar_space designates the space for the characters after the dollar sign $_____X.XX
        # the + 2 after dollar_space here is just to customize how far the dollar sign is from the chosen dollar_space
    if len(a) > width - len(b):
        a = a[:len(b)+4] + '...'
        # hides string overflow within an ellipsis ... if number is too large or width is too small
    return a + ' ' * (width - len(a) - len(b)) + b
    # dynamically creates space between the string a (left side) and the string b (right side)
    # this creates a line that will always have the same width no matter how long a and b are
    # string b will have been processed to include dollar_sign and dollar_space if those arguments are used


def part1():
    principal = float(input('Enter a starting balance (principle) in dollars & cents: '))
    annual_rate = 0.01 * float(input('Enter an annual interest rate: '))
    # annual_rate is converted into percent value upon input
    balance_annual_comp = principal * (1 + annual_rate)
    balance_daily_comp = principal * (1 + annual_rate/365) ** 365
    interest_annual_comp = balance_annual_comp - principal
    interest_daily_comp = balance_daily_comp - principal
    longest_number = len(format(balance_daily_comp, '.2f'))
    # balance compounded daily will always be the longest number
    # this is used as the dollar_space argument in the aligner() function so that the dollar signs lign up cleanly
    print('', '-' * 52, '\n',
          aligner(50, 'Principal', format(principal, '.2f'), '$', longest_number), '\n',
          aligner(50, 'Annual Interest Rate', format(annual_rate * 100, '.2f')), '%', '\n',
          aligner(50, 'Interest Compounded Annually (Y1)', format(interest_annual_comp, '.2f'), '$', longest_number), '\n',
          aligner(50, 'Balance', format(balance_annual_comp, '.2f'),'$', longest_number), '\n',
          aligner(50, 'Interest Compounded Daily (Y1)', format(interest_daily_comp, '.2f'),'$', longest_number), '\n',
          aligner(50, 'Balance', format(balance_daily_comp, '.2f'),'$', longest_number), '\n',
          '-' * 52)
    # used format() instead of round() to accommodate cases such as 130.10, which would display as 130.1
    # even if function was typed as round(130.10, 2)


def part2():
    height = float(input('Enter a height in inches: '))
    width = float(input('Enter a width in inches: '))
    print('Screen size (diagonal): ', round((height**2 + width**2)**0.5), 'inches')


def part3():
    tank_cost = float(input('Enter the cost of the tank of gas: '))
    distance = float(input('Enter the number of miles driven: '))
    cost_rate = tank_cost / distance
    longest_number = len(format(tank_cost, '.2f'))
    print('', '-' * 52, '\n',
          aligner(50, 'Cost of gas', format(tank_cost, '.2f'), '$', longest_number), '\n',
          aligner(50, 'Miles driven', format(distance, '.2f')), '\n',
          aligner(50, 'Cost per mile', format(cost_rate, '.2f'), '$', longest_number),
          '\n',
          '-' * 52)
    # used the same aligner() function used in part1()


def part4():
    x = 1


if __name__ == '__main__':
    print('PART 1')
    part1()
    print('PART 2')
    part2()
    print('PART 3')
    part3()
    print('PART 4')
    part4()