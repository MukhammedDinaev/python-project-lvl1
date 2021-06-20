import prompt
from random import randint
from brain_games import cli

name = cli.welcome_user()
print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


def prime_check(number):
    start_point = 2
    while start_point <= number ** 0.5:
        if number % start_point == 0:
            return 'no'
        start_point += 1
    return 'yes'


def prime(username=name, rec_count=0):
    if rec_count == 3:
        print('Congratulations, {}!'.format(username))
        return
    number = randint(0, 100)
    true_ans = prime_check(number)

    print('Question:{}'.format(str(number)))
    answer = prompt.string("Your answer: ")

    if true_ans != answer:
        print('\'{}\' is wrong answer ;(.'.format(answer), end='')
        print(' Correct answer was \'{}\'.'.format(true_ans))
        print('Let\'s try again, {}!'.format(username))
        return
    else:
        print('Correct!')
        return prime(name, rec_count + 1)
