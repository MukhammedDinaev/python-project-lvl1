from random import randint

task = "Answer yes if the number is even, otherwise answer no."


def is_even(number):
    return number % 2 == 0


def get_round_data():
    question = randint(0, 100)
    if is_even(question):
        true_answer = 'yes'
    else:
        true_answer = 'no'

    return question, true_answer
