from random import randint

game_steps = 3


def ask_task():
    return "What number is missing in the progression?."


def ask_question():
    first_num = randint(1, 10)
    step_num = randint(1, 10)
    secret_index_num = randint(1, 9)

    progression_list = []
    true_answer = 0
    for i in range(10):
        if i == secret_index_num:
            progression_list.insert(i, '..')
            true_answer = first_num + step_num
            first_num += step_num
            continue
        else:
            first_num += step_num
            progression_list.append(first_num)
    progression_list = ''.join(str(progression_list)).strip('[]')
    progression_list = progression_list.replace(',', '')
    progression_list = progression_list.replace("'", '')
    return progression_list, str(true_answer)


def start_game():
    question, true_answer = ask_question()
    return question, true_answer
