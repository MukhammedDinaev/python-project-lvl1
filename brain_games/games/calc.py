import prompt
from random import randint, choice
from brain_games import cli

name = cli.welcome_user()
print("What is the result of the expression?")


def calc(username=name, rec_count=0):
    if rec_count == 3:
        print('Congratulations, {}!'.format(username))
        return
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    operator = choice(['+', '-', '*'])
    print('Question:{} {} {}'.format(num1, operator, num2))
    answer = prompt.string("Your answer: ")

    if operator == '+':
        true_ans = num1 + num2
    elif operator == '-':
        true_ans = num1 - num2
    else:
        true_ans = num1 * num2

    if operator == '+' and str(true_ans) == answer:
        print('Correct!')
        return calc(name, rec_count + 1)
    elif operator == '-' and str(true_ans) == answer:
        print('Correct!')
        return calc(name, rec_count + 1)
    elif operator == '*' and str(true_ans) == answer:
        print('Correct!')
        return calc(name, rec_count + 1)
    else:
        print('\'{}\' is wrong answer ;(.'.format(answer), end='')
        print(' Correct answer was \'{}\'.'.format(str(true_ans)))
        print('Let\'s try again, {}!'.format(username))
        return
