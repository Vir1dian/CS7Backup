# Assignment 9
# CS7 - Section D01
# November 30, 2023,
# Gavin Torrecampo
import random


def roll():
    return random.randint(1, 6) + random.randint(1, 6)


def align_l(item, space):
    return item + ' ' * (space - len(item))  # Align string 'item' to the right inside a string with width 'space'


def align_r(item, space):
    return ' ' * (space - len(item)) + item


def part1():
    print('\n*** PART 1 ***')
    sushi_roll = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    # I really felt like calling this dictionary for rolls a sushi roll, because why not?
    roll_count = int(input('Enter number of rolls:\n'))
    for i in range(0, roll_count):
        sushi_roll[roll()] += 1
    print('-Standard Format-')
    for i in sushi_roll:
        roll_percent = format((sushi_roll[i] / roll_count) * 100, '.2f')
        print('Roll', align_r(str(i), 2), 'count',
              align_r(str(sushi_roll[i]), len(str(roll_count))),
              align_r(roll_percent, 6), '%')
    if roll_count <= 1000:
        print('-Histogram (Vertical) Format-')
        hist_header = '      |'
        for i in sushi_roll:
            hist_header += align_r(str(i), 5)
        hist_header += '  |'
        hist_header_2 = '      |'
        for i in sushi_roll:
            hist_header_2 += align_r('('+str(sushi_roll[i])+')', 5)
        hist_header_2 += '  |'
        print(align_l('Count | Roll Number', len(hist_header) - 2), '|')  # Header titles
        print(hist_header)  # Rolled numbers
        print(hist_header_2)  # Count of rolls for each number
        largest_count = sushi_roll[max(sushi_roll, key=sushi_roll.get)]
        # Get roll number with the largest count, used to get size of the histogram for space efficiency
        incr = 1  # To be used as the scale of the histogram
        if largest_count < 50:
            incr = 1
        elif largest_count < 100:
            incr = 2
        elif largest_count < 250:
            incr = 5
        elif largest_count < 500:
            incr = 10
        for i in range(0, largest_count, incr):
            line = align_r(str(i + 1) if incr == 1 else str(i) if i > 0 else '1', 6) + '|'
            # Scale of counted rolls on the side of the histogram, i + 1 only if incr is 1 due to index starting from 0
            # otherwise, use just incr for 2, 5, and 10, replacing only the starting index 0 with 1
            for j in sushi_roll:
                if sushi_roll[j] > i:
                    line += align_r('*', 5)  # * If the count for sushi_roll[j] reaches this increment
                else:
                    line += align_r(' ', 5)  # Blank space if the count for sushi_roll[j] does not reach this increment
            print(line)


def part2():
    print('\n*** PART 2 ***')


if __name__ == '__main__':
    part1()
    part2()
