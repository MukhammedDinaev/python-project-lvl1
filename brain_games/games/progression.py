from random import randint

task = "What number is missing in the progression?."


def get_round_data():
    lenth = 10

    first_num = randint(1, lenth)
    step_num = randint(1, lenth)
    secret_index_num = randint(0, lenth - 1)

    progression = []
    true_answer = 0

    for index in range(0, lenth):
        if index == secret_index_num:
            progression.insert(index, '.. ')
            true_answer = first_num + step_num * index
        else:
            progression.append(str(first_num + step_num * index) + ' ')

    question = ''.join(progression).strip('[]')
    true_answer = str(true_answer)

    return question, true_answer
