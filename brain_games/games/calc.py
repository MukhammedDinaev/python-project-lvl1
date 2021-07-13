from random import randint, choice

game_steps = 3


def ask_task():
    return "What is the result of the expression?"


def ask_question():
    number1 = randint(0, 10)
    number2 = randint(0, 10)
    operator = choice(['+', '-', '*'])
    about_question = (number1, operator, number2)
    return '{} {} {}'.format(number1, operator, number2), about_question


def make_calc(about_question):

    number1, operator, number2 = about_question
    if operator == '+':
        return str(number1 + number2)
    elif operator == '-':
        return str(number1 - number2)
    elif operator == '*':
        return str(number1 * number2)
    else:
        return 'didn\'t find true answer'


def start_game():
    question, about_question = ask_question()
    true_answer = make_calc(about_question)

    return question, true_answer
