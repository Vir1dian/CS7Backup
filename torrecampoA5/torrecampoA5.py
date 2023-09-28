# Assignment 5
# CS7 - Section D01
# September 28, 2023,
# Gavin Torrecampo
import random


def display_menu():
    print('\nWhich service are you interested in? (Input the letter)\n'
          '\tA.\tTemperature Conversion, C to K\n'
          '\tB.\tNumber Guessing Game\n'
          '\tC.\tTemperature Table, F to C\n'
          '\tD.\tDraw a Rectangle\n'
          '\tE.\tBaby Names Voting\n'
          '\tX.\tExit\n')


def service_A():  # Temperature Conversion, C to K
    temp = float(input('Enter temperature in Celsius: '))
    print('Your temperature in Kelvin: ', temp + 273.15, '\nDone.')


def service_B():  # Number Guessing Game
    number = random.randint(1, 100)
    print('<< Random number (between 1-100) generated! >>')
    guess_count = 0
    guess = int(input('(!) Guess the number: '))
    while guess != number:
        if guess > number:
            print('* Your guess, ', guess, ', was higher. *')
        if guess < number:
            print('* Your guess, ', guess, ', was lower. *')
        guess_count += 1
        guess = int(input('(!) Guess again: '))
    print('# You guessed the right number! # << ', number, ' >>\nNumber of incorrect guesses: ', guess_count)


def service_C():  # Temperature Table, F to C
    print('| Centigrade | Fahrenheit |')
    for i in range(0, int(100/4) + 1):  # c for centigrade, f for fahrenheit
        c = i*4
        f = (c * 9/5) + 32
        print('|',
              ' '*(len('Centigrade')-len(str(c)) - 1), c,
              '|',
              ' '*(len('Fahrenheit')-len(format(f, '.2f')) - 1), format(f, '.2f'),
              '|')
        # Removed one space from each individual part of the print statement,
        # including the space where the number goes (... - 1)
        # Python seems to add an extra space between each part so this change
        # accounts for that


def service_D():  # Draw a Rectangle
    print('Drawing a rectangle...')
    height = int(input('Enter a height: '))
    width = int(input('Enter a width: '))
    for h in range(0, height):
        print('')
        for w in range(0, width):  # for honor and glory!
            if (w == 0 or w == width - 1) or (h == 0 or h == height - 1):
                print('*', end='')
            else:
                print(' ', end='')


def service_E():  # Baby Names Voting
    print('Voting for baby names...\n<< NAMING PHASE >>')
    name1 = input('Enter name 1: ')
    name2 = input('Enter name 2: ')
    while name1 == name2:
        print('You used that name already!')
        name2 = input('Enter name 2: ')
    name3 = input('Enter name 3: ')
    while name1 == name3 or name2 == name3:
        print('You used that name already!')
        name3 = input('Enter name 3: ')
    print('<< VOTING PHASE >>')
    name1_votes = 0
    name2_votes = 0
    name3_votes = 0
    while name1_votes < 3 and name2_votes < 3 and name3_votes < 3:
        voted_name = input('Enter name to vote for: ')
        if voted_name == name1:
            name1_votes += 1
        elif voted_name == name2:
            name2_votes += 1
        elif voted_name == name3:
            name3_votes += 1
        else:
            print('Invalid name, try again.')
    if name1_votes == 3:
        print('(!) ', name1, 'is the winner!')
    if name2_votes == 3:
        print('(!) ', name2, 'is the winner!')
    if name3_votes == 3:
        print('(!) ', name3, 'is the winner!')
    print(name1, 'had', name1_votes, 'votes.')
    print(name2, 'had', name2_votes, 'votes.')
    print(name3, 'had', name3_votes, 'votes.')


if __name__ == '__main__':  # this would look really nice as a switch case like in JS
    display_menu()
    choice = input()
    while choice.upper() != 'X':  # use of upper() allows for letters to be accepted in either case
        if choice.upper() == 'A':
            service_A()
        elif choice.upper() == 'B':
            service_B()
        elif choice.upper() == 'C':
            service_C()
        elif choice.upper() == 'D':
            service_D()
        elif choice.upper() == 'E':
            service_E()
        else:
            print('No matching service found.')
        display_menu()
        choice = input()
    print('*** Thank you for playing! ***')