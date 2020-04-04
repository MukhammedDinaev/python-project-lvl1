from random import randint as rdt


def numbers():
    number = rdt(0, 100)
    return number


def game(var, answer, name):
    if var % 2 == 0:
        correctanswer_is = "'yes'"
    else:
        correctanswer_is = "'no'"
    if var % 2 == 0 and answer == 'yes':
        print("Correct!")
        return int(1)
    elif var % 2 == 1 and answer == 'no':
        print("Correct!")
        return int(1)
    else:
        print("'" + answer+ "'" + " is wrong answer ;(. Correct answer was, " + correctanswer_is, '\n' + 
"Let's try again, " + name + "!")
        return int(0)
