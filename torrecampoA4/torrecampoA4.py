# Assignment 4
# CS7 - Section D01
# September 21, 2023,
# Gavin Torrecampo
def part1():
    print('\n*** PART 1 ***')
    for i in range(1, 11):
        if i != 7:
            print('Number:', i, 'Squared:', i ** 2, 'Square root:', i ** 0.5)
        else:
            print('7 skipped')


def part2():
    print('\n*** PART 2 ***')
    lower = int(input('Enter an integer (lower bound): '))
    upper = int(input('Enter a larger integer (upper bound): '))
    # uses the same structure as part1()
    i_sum = 0
    for i in range(lower, upper + 1):
        i_sum += i
    print('Sum from integers', lower, 'through', upper, ':', i_sum)


def part3():
    print('\n*** PART 3 ***')
    order = ''
    num_sum = 0
    count = 0
    while order != 'STOP':
        x = input('Enter an integer OR enter STOP to end the loop: ')
        if x == 'STOP':
            order = 'STOP'
        else:
            num_sum += int(x)
            count += 1
    print('Loop stopped. Average of list: ', num_sum / count)


def part4():
    print('\n*** PART 4 ***')
    order = ''
    name_count = 0
    marked_name_count = 0
    while order != 'STOP':
        new_name = input('Enter a name OR enter STOP to end the loop: ')
        if new_name == 'STOP':
            order = 'STOP'
        elif len(new_name) > 0:
            name_count += 1
        if new_name == 'Ada' or new_name == 'Bob' or new_name == 'Cal':
            marked_name_count += 1
    print('Loop stopped.')
    print('Number of non-blank names: ', name_count)
    print('Number of names Ada, Bob, and Cal: ', marked_name_count)


def part5():
    print('\n*** PART 5 ***')
    x = 0
    while x != -1:
        number = int(input('Enter an integer (enter -1 to stop the loop): '))
        x = number
        if number < 0:
            number *= -1
        square = 0
        for i in range(0, number):
            square += number
        print('Square of', x, ':', square)
    print('Loop stopped.')


if __name__ == '__main__':
    part1()
    part2()
    part3()
    part4()
    part5()
