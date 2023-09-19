# Assignment 2
# CS7 - Section D01
# September 18, 2023,
# Gavin Torrecampo
def part1():
    print('\n*** PART 1 ***')
    i = 1
    while i <= 10:
        if i != 7:
            print('Number:', i, 'Squared:', i**2, 'Square root:', i**0.5)
        else:
            print('7 skipped')
        i += 1


def part2():
    print('\n*** PART 2 ***')
    i = 10
    i_sum = 0
    while i <= 20:
        i_sum += i
        i += 1
    print('Sum from integers 10 through 20:', i_sum)


def part3():
    print('\n*** PART 3 ***')
    lower = 1
    upper = 0
    # this first while loop makes sure that the lower bound is less than the upper bound
    while lower > upper:
        lower = int(input('Enter an integer (lower bound): '))
        upper = int(input('Enter a larger integer (upper bound): '))
    # uses the same structure as part1()
    i = lower
    i_sum = 0
    while i <= upper:
        i_sum += i
        i += 1
    print('Sum from integers', lower, 'through', upper, ':', i_sum)


def part4():
    print('\n*** PART 4 ***')
    is_success = False
    while is_success == False:
        name = input('Enter a name: ')
        if name == 'Dagny' or name == 'Hank' or name == 'Francisco':
            print('Success!')
            is_success = True
        else:
            print('Error: incorrect name, try again.')


def part5():
    print('\n*** PART 5 ***')
    number = int(input('Enter a number: '))
    while number >= 0:
        if number == 1:
            print('Abigail')
        elif number == 2:
            print('Bobby')
        elif number == 3:
            print('Charmaine')
        else:
            print('error')
        number = int(input('Enter a number: '))
    print('Negative, loop stopped.')


def part6():
    print('\n*** PART 6 ***')
    # used the same structure as with part4()
    is_success = False
    while is_success == False:
        name = input('Enter a name: ')
        if name == 'Frank' or name == 'Betty':
            print('You did well!')
            is_success = True
        else:
            print('Error: incorrect name, try again.')


if __name__ == '__main__':
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()