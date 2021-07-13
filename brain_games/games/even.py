from random import randint

game_steps = 3


def ask_task():
    return "Answer yes if the number is even, otherwise answer no."


def ask_question():
    number = randint(0, 100)
    return number


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def start_game():
    question = ask_question()

    if is_even(question):
        true_answer = 'yes'
    else:
        true_answer = 'no'

    return question, true_answer
