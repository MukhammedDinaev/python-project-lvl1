from random import randint as rdt
import prompt
from brain_games.games import cli

def answers():
    answer = prompt.string("Your answer: ")
    return answer


def numbers():
    number = rdt(2, 100)
    return number


def random_task():
    var = numbers()
    n = 2
    while n <= var ** 0.5:
        if var % n == 0:
            return (var, 'no')
        n += 1
    return (var, 'yes')


def logic(true_ans, ans):
    if true_ans == ans:
        print("Correct!")
        return True
    return False

def wrong(true_ans, ans, name):
    print("'" + ans+ "'" + " is wrong answer ;(. Correct answer was, " + true_ans, '\n' +
    "Let's try again, " + name + "!")
    return


def chek(name, rec_deep=0):

    if rec_deep == 4:
        print('Congratulations, ' + name + '!')
        return

    task, true_ans = random_task()
    print("Question:", task)
    ans = answers()

    if logic(true_ans, ans):
        return chek(name, rec_deep + 1)
    else:
        wrong(true_ans, ans, name)
        return


def gameprime():
    print("Welcome to the Brain Games!,")
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.", "\n")
    name = cli.welcome_user()
    print()
    chek(name)


