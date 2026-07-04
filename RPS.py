#Rock,paper,scissors

print('Select one of the given options:')
print('1. Paper   2. Scissors   3. Rock')
a = int(input('Enter your choice (1/2/3): '))

import random
computer = random.randint(1, 3)
print('Computer chose option', computer)

if a == computer:
    print('It\'s a tie!')
elif (a == 1 and computer == 2) or (a == 2 and computer == 3) or (a == 1 and computer == 3):
    print('You lost the game!')
else:
    print('You won the game.')

i = input('Press y to continue or n to cancel: ')
while i != 'n':
    a = int(input('Enter your choice (1/2/3): '))
    computer = random.randint(1, 3)
    print('Computer chose option', computer)
    if a == computer:
        print('It\'s a tie!')
    elif (a == 1 and computer == 2) or (a == 2 and computer == 3) or (a == 1 and computer == 3):
        print('You lost the game!')
    else:
        print('You won the game.')
    i = input('Press y to continue or n to cancel: ')
