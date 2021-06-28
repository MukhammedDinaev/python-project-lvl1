from random import randint


def ask_task():
    print("Answer yes if the number is even, otherwise answer no.")
    return


def ask_question():
    number = randint(0, 100)
    return number, number


def start_even(number, user_answer):
    if number % 2 == 0 and user_answer == 'yes':
        return 'yes', True
    elif number % 2 == 1 and user_answer == 'no':
        return 'no', True
    elif number % 2 == 0 and user_answer != 'yes':
        return 'yes', False
    elif number % 2 == 1 and user_answer != 'no':
        return 'no', False
