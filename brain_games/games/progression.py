from random import randint


def ask_task():
    print("What number is missing in the progression?.")
    return


def ask_question():
    first_num = randint(0, 10)
    step_num = randint(1, 10)
    secret_index_num = randint(1, 10)

    progression_list = []
    true_answer = int()
    for i in range(10):
        if i == secret_index_num:
            progression_list.insert(i, '..')
            true_answer = first_num + step_num
            first_num += step_num
            continue
        else:
            first_num += step_num
            progression_list.append(first_num)
    progression_list = ''.join(str(progression_list)).strip('[]').replace(',', '')
    return progression_list, str(true_answer)


def start_progression(true_answer, user_answer):
    if true_answer == user_answer:
        return true_answer, True
    else:
        return true_answer, False
