from random import randint

task = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def check_prime(number):

    if number < 2:
        return False

    is_prime = 2
    while is_prime <= abs(number) ** 0.5:
        if number % is_prime == 0:
            return False
        is_prime += 1

    return True


def get_round_data():
    question = randint(-100, 100)
    if check_prime(question):
        true_answer = 'yes'
    else:
        true_answer = 'no'

    return question, true_answer
