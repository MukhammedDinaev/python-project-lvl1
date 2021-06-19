import prompt
from random import randint
from brain_games import cli

name = cli.welcome_user()
print("Answer yes if the number is even, otherwise answer no.")


def even(username=name, rec_count=0):
    if rec_count == 3:
        print('Congratulations, {}!'.format(username))
        return
    number = randint(0, 100)
    print('Question:{}'.format(number))
    answer = prompt.string("Your answer: ")
    if number % 2 == 0 and answer == 'yes':
        print('Correct!')
        return even(name, rec_count + 1)
    elif number % 2 == 1 and answer == 'no':
        print('Correct!')
        return even(name, rec_count + 1)
    elif number % 2 == 0 and answer != 'yes':
        print('\'{}\' is wrong answer ;(.'.format(answer), end='')
        print(' Correct answer was \'{}\'.'.format('yes'))
        print('Let\'s try again, {}!'.format(username))
        return
    elif number % 2 == 1 and answer != 'no':
        print('\'{}\' is wrong answer ;(.'.format(answer), end='')
        print(' Correct answer was \'{}\'.'.format('no'))
        return
