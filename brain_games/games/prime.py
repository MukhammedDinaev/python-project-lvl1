from random import randint

game_steps = 3


def ask_task():
    return "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def ask_question():
    number = randint(-100, 100)
    return number


def check_prime(number):

    is_prime = 2
    while is_prime <= abs(number) ** 0.5:
        if number < 2:
            return False
        if number % is_prime == 0:
            return False
        is_prime += 1

    return True


def start_game():
    question = ask_question()

    if check_prime(question):
        true_answer = 'yes'
    else:
        true_answer = 'no'

    return question, true_answer
