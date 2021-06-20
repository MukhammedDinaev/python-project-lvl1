import prompt
from random import randint
from brain_games import cli

name = cli.welcome_user()
print("Find the greatest common divisor of given numbers.")


def check_gcd_def(num1, num2):
    if num1 < num2:
        check_gcd = num1
    else:
        check_gcd = num2

    while check_gcd > 0:
        if num2 % check_gcd == 0:
            if num1 % check_gcd == 0:
                break
        check_gcd -= 1
    return str(check_gcd)


def gcd(username=name, rec_count=0):
    if rec_count == 3:
        print('Congratulations, {}!'.format(username))
        return
    num1 = randint(2, 100)
    num2 = randint(2, 100)
    true_ans = check_gcd_def(num1, num2)

    print('Question:{} {}'.format(num1, num2))
    answer = prompt.string("Your answer: ")

    if true_ans == answer:
        print('Correct!')
        return gcd(name, rec_count + 1)
    else:
        print('\'{}\' is wrong answer ;(.'.format(answer), end='')
        print(' Correct answer was \'{}\'.'.format(str(true_ans)))
        print('Let\'s try again, {}!'.format(username))
        return
