from random import randint as rdt
import prompt
from brain_games.games import cli

def answers():
    answer = prompt.string("Your answer: ")
    return answer


def numbers():
    number = rdt(0, 10)
    return number


def random_task():
    operator =rdt(0, 2)
    var1 = numbers()
    var2 = numbers()
    if operator == 0:
        var3 = var1 + var2
        operator = "+"
    elif operator == 1:
        var3 = var1 - var2
        operator = "-"
    else:
        var3 = var1 * var2
        operator = "*"
    return (str(var1) + " " + operator + " " + str(var2), var3)


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


def gamecalc():
    print("Welcome to the Brain Games!,")
    print("AWhat is the result of the expression?", "\n")
    name = cli.welcome_user()
    chek(name)

