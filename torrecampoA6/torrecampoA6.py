# Assignment 6
# CS7 - Section D01
# October 5, 2023,
# Gavin Torrecampo
def part1():
    print('\n*** PART 1 ***')
    order = ''
    temp_list = []
    temp_sum = 0
    while order != 'stop':
        order = input('Enter a temperature, or "stop": ')
        if order.lower() == 'stop':
            order = 'stop'
        else:
            order = float(order)
            temp_list.append(order)
    for i in temp_list:
        print('You entered: ', i)
        temp_sum += i
    if len(temp_list) == 0:
        print('The average temperature is: 0')
    else:
        print('The average temperature is: ', temp_sum / len(temp_list))


def part2():
    print('\n*** PART 2 ***')
    order = input('Enter a grade and number of hours (formatted in letter grade, space, and number of hours), '
                  'or "stop": ')
    transcript = []  # list of lists
    grade_point_sum = 0
    hours_sum = 0
    class_number = 1  # this is purely for numbering the list when it is printed out later
    while order.lower() != 'stop':
        if int(order[2]) > 4 or int(order[2]) < 1:
            transcript.append([order[0], 1])
        else:
            transcript.append([order[0], order[2]])
        order = input('Enter a grade and number of hours, or "stop": ')
    print('The grades you entered were:')
    for i in transcript:
        print('Class', class_number, '| Grade: ', i[0], '| Hours:', i[1])
        class_number += 1
        grade_int = 0
        if i[0].lower() == 'a':
            grade_int = 4
        elif i[0].lower() == 'b':
            grade_int = 3
        elif i[0].lower() == 'c':
            grade_int = 2
        elif i[0].lower() == 'd':
            grade_int = 1
        # I omitted F so that any grade that isn't A, B, C, or D (due to user error) will be counted as 0 as well
        grade_point_sum += grade_int * int(i[1])
        hours_sum += int(i[1])
    print('The GPA is: ', format(grade_point_sum/hours_sum, '.2f'))


def classwork():
    number = int(input('Enter a number: '))
    num_list = []
    num_sum = 0
    while number >= 0:
        num_list.append(number)
        number = int(input('Enter a number: '))
    print(num_list)
    for i in num_list:
        num_sum += i
    print(format(num_sum / len(num_list), '.2f'))


if __name__ == '__main__':
    # classwork()
    part1()
    part2()
