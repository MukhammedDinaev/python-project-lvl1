from random import randint, choice
import operator


def ask_task():
    print("What is the result of the expression?")
    return


def ask_question():
    number1 = randint(0, 10)
    number2 = randint(0, 10)
    operator = choice(['+', '-', '*'])
    about_question = (number1, operator, number2)
    return '{} {} {}'.format(number1, operator, number2), about_question


def start_calc(numbers_operator, user_answer):
    number1, operator, number2 = numbers_operator

    if operator == '+':
        true_answer = str(number1 + numer2)
    elif operator == '-':
        true_answer = str(number1 - number2)
    elif operator == '*':
        true_answer = str(number1 * number2)
    else:
        true_answer = 'didn\'t find true answer'

    if true_answer == user_answer:
        return true_answer, True
    else:
        return true_answer, False
