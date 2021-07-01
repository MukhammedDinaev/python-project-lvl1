from random import randint


def ask_task():
    print("Find the greatest common divisor of given numbers.")
    return


def ask_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    about_question = (number1, number2)
    return '{} {}'.format(number1, number2), about_question


def start_gcd(numbers, user_answer):
    number1, number2 = numbers

    if number1 < number2:
        true_answer = number1
    else:
        true_answer = number2

    while true_answer > 0:
        if number2 % true_answer == 0 and number1 % true_answer == 0:
            break
        true_answer -= 1

    if number1 == 0 or number2 == 0:
        true_answer = 0
        if str(true_answer) == user_answer:
            return true_answer, True
        else:
            return true_answer, False

    if str(true_answer) == user_answer:
        return true_answer, True
    else:
        return true_answer, False
