import prompt


def say_hi_question():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def start_engine(game_funk, ask_task, ask_question, user_name='', rec_count=0):
    if rec_count == 0:
        user_name = say_hi_question()
        ask_task()

    if rec_count == 3:
        print('Congratulations, {}!'.format(user_name))
        return

    question = ask_question()
    print('Question:{}'.format(question[0]))
    user_answer = prompt.string("Your answer: ")

    true_answer, check_game_step = game_funk(question[1], user_answer)

    if check_game_step:
        print('Correct!')
        return start_engine(game_funk, ask_task,
                            ask_question, user_name, rec_count + 1)

    else:
        print('\'{}\' is wrong answer ;(.'.format(user_answer), end='')
        print(' Correct answer was \'{}\'.'.format(true_answer))
        return
