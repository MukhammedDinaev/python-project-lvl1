from random import randint

game_steps = 3


def ask_task():
    return "Find the greatest common divisor of given numbers."


def ask_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    about_question = (number1, number2)
    return '{} {}'.format(number1, number2), about_question


def find_gcd(about_question):
    number1, number2 = about_question

    if number1 < number2:
        true_answer = number1
    else:
        true_answer = number2

    while true_answer > 0:
        if number2 % true_answer == 0 and number1 % true_answer == 0:
            break
        true_answer -= 1

    return str(true_answer)


def start_game():
    question, about_question = ask_question()
    true_answer = find_gcd(about_question)

    return question, true_answer
