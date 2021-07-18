from random import randint, choice

task = "What is the result of the expression?"


def make_calc(about_question):

    number1, operator, number2 = about_question
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        return 'didn\'t find true answer'


def get_round_data():
    number1 = randint(0, 10)
    number2 = randint(0, 10)
    operator = choice(['+', '-', '*'])
    about_question = (number1, operator, number2)
    question = '{} {} {}'.format(number1, operator, number2)
    true_answer = str(make_calc(about_question))

    return question, true_answer
