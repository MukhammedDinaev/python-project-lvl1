import prompt
from random import randint
from brain_games import cli

name = cli.welcome_user()
print("What number is missing in the progression?.")


def build_progression(first_num, step_num, secret_index_num):
    progression_list = []
    true_ans = int()
    for i in range(10):
        if i == secret_index_num:
            progression_list.insert(i, '..')
            true_ans = first_num + step_num
            first_num += step_num
            continue
        else:
            first_num += step_num
            progression_list.append(first_num)
    progression_list = progression_list
    return progression_list, true_ans


def progression(username=name, rec_count=0):
    if rec_count == 3:
        print('Congratulations, {}!'.format(username))
        return
    first_num = randint(0, 10)
    step_num = randint(1, 10)
    secret_index_num = randint(0, 10)

    result = build_progression(first_num, step_num, secret_index_num)
    true_ans = str(result[1])
    progression_list = ''
    for i in result[0]:
        progression_list = progression_list + ' ' + str(i)

    print('Question:{}'.format(progression_list))
    answer = prompt.string("Your answer: ")

    if true_ans == answer:
        print('Correct!')
        return progression(name, rec_count + 1)
    else:
        print('\'{}\' is wrong answer ;(.'.format(answer), end='')
        print(' Correct answer was \'{}\'.'.format(str(true_ans)))
        print('Let\'s try again, {}!'.format(username))
        return
