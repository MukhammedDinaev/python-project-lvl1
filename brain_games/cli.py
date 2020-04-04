import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name

def answers():
    answer = prompt.string("Your answer: ")
    return answer
