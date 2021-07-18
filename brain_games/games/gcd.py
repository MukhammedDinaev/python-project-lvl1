from random import randint

task = "Find the greatest common divisor of given numbers."


def find_gcd(number1, number2):
    if number1 < number2:
        true_answer = number1
    else:
        true_answer = number2

    while true_answer > 0:
        if number2 % true_answer == 0 and number1 % true_answer == 0:
            break
        true_answer -= 1

    return true_answer


def get_round_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = '{} {}'.format(number1, number2)
    true_answer = str(find_gcd(number1, number2))

    return question, true_answer
