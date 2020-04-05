from random import randint as rdt
import prompt
from brain_games.games import cli

def answers():
    answer = prompt.string("Your answer: ")
    return answer


def numbers():
    number = rdt(0, 100)
    return number


def logic(var, ans):
    if var % 2 == 0 and ans == 'yes':
        print("Correct!")
        return True
    elif var % 2 == 1 and ans == 'no':
        print("Correct!")
        return True
    return False


def wrong(var, ans, name):
    if var % 2 == 0:
        correctanswer_is = "'yes'"
    else:
        correctanswer_is = "'no'"

    print("'" + ans+ "'" + " is wrong answer ;(. Correct answer was, " + correctanswer_is, '\n' + 
    "Let's try again, " + name + "!")
    return


def chek(name, rec_deep=0):

    if rec_deep == 4:
        print('Congratulations, ' + name + '!')
        return

    var = numbers()
    print("Question:", var)
    ans = answers()

    if logic(var, ans):
        return chek(name, rec_deep + 1)
    else:
        wrong(var, ans, name)
        return


def gameeven():
    print("Welcome to the Brain Games!,")
    print("Answer 'yes' if number even otherwise answer 'no'", "\n")
    name = cli.welcome_user()
    print()
    chek(name)

__all__ = ['answers', 'numbers', 'chek', 'gameeven']
