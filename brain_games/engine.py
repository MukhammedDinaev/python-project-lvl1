import prompt


def start_engine(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name + '!')

    roundsCount = 3

    task = game.task
    print(task)

    round = 0
    while roundsCount != round:
        question, true_answer = game.get_round_data()
        print('Question: {}'.format(question))
        user_answer = prompt.string("Your answer: ")

        if true_answer == user_answer:
            print('Correct!')
            round += 1
        else:
            print('\'{}\' is wrong answer ;(.'.format(user_answer), end='')
            print(' Correct answer was \'{}\'.'.format(true_answer))
            print('Let\'s try again, {}!'.format(user_name))
            return
    print('Congratulations, {}!'.format(user_name))
