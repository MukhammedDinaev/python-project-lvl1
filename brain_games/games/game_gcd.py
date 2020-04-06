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
    var1 = numbers()
    var2 = numbers()
    n = 2
    while n <= 50:
        if var1 % n == 0 and var2 % n == 0:
            return (str(var1) + " " + str(var2), n)
        n += 1
    return random_task()


def logic(true_ans, ans):
    if str(true_ans) == ans:
        print("Correct!")
        return True
    return False

def wrong(true_ans, ans, name):
    print("'" + ans+ "'" + " is wrong answer ;(. Correct answer was, " + str(true_ans), '\n' +
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


def gamegcd():
    print("Welcome to the Brain Games!,")
    print("Find the greatest common divisor of given numbers", "\n")
    name = cli.welcome_user()
    print()
    chek(name)

