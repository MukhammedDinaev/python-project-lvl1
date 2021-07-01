from random import randint


def ask_task():
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    return


def ask_question():
    number = randint(-100, 100)
    return number, number


def start_prime(number, user_answer):
    true_answer = 'yes'

    if number == 0:
        true_answer = 'no'
        if true_answer == user_answer:
            return true_answer, True
        else:
            return true_answer, False

    is_prime = 2

    while is_prime <= abs(number) ** 0.5:
        if number < 2:
            true_answer = 'no'
            break
        if number % is_prime == 0:
            true_answer = 'no'
            break
        is_prime += 1

    if true_answer == user_answer:
        return true_answer, True
    else:
        return true_answer, False
