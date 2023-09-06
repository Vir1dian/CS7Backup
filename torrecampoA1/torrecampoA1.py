def print_hi(name):
    print(f'Hi, {name}')


def part1():
    days = -1
    while days > 7 or days < 1:
        days = int(input('Enter number of POSSIBLE days worked last week: '))
    hours_per_week = -1
    while hours_per_week > 7*24 or hours_per_week < 1:
        hours_per_week = float(input('Enter number of POSSIBLE hours worked for the week: '))
    print('You averaged', hours_per_week / days, 'hours per day.')


def part2():
    temp_fahr = float(input('Enter temperature, in F: '))
    temp_cels = (temp_fahr-32) * 5/9
    print(temp_fahr, 'F is', round(temp_cels, 2), 'in C.')


def part3():
    id_num = input('Enter your ID number: ')
    i1type = input('Enter the first item type: ')
    i1cost = float(input('Enter the first item cost: '))
    i2type = input('Enter the second item type: ')
    i2cost = float(input('Enter the second item cost: '))
    i3type = input('Enter the third item type: ')
    i3cost = float(input('Enter the third item cost: '))
    subtotal = round(i1cost + i2cost + i3cost, 2)
    tax = round(subtotal*0.0925, 2)
    total = subtotal + tax
    print('--------', id_num, '--------\n',
          i1type, i1cost, '\n',
          i2type, i2cost, '\n',
          i3type, i3cost, '\n',
          'tax', tax, '\n',
          'total', total, '\n',
          '--------------------------')


if __name__ == '__main__':
    part1()
    part2()
    part3()
