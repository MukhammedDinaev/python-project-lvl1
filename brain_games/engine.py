import prompt


def say_hi_question():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def start_engine(game_funk):
    user_name = say_hi_question()
    task = game_funk.ask_task()
    print(task)
    steps = game_funk.game_steps

    round = 0
    while steps != round:
        question, true_answer = game_funk.start_game()
        print('Question: {}'.format(question))
        user_answer = prompt.string("Your answer: ")

        if true_answer == user_answer:
            print('Correct!')
            round += 1
            continue
        else:
            print('\'{}\' is wrong answer ;(.'.format(user_answer), end='')
            print(' Correct answer was \'{}\'.'.format(true_answer))
            print('Let\'s try again, {}!'.format(user_name))
            return
    print('Congratulations, {}!'.format(user_name))
