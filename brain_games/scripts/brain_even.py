from brain_games import game_even as ge
from brain_games import cli


def main():
    print("Welcome to the Brain Games!,")
    print("Answer ""yes"" if number even otherwise answer ""no""", "\n")
    name = cli.welcome_user()
    var = ge.numbers()
    print()
    print("Question:", var)
    ans = cli.answers()
    bull =  ge.game(var, ans, name)
    n = 0    
    if bull == 1:
        while n != 3:
            var = ge.numbers()
            print("Question:", var)
            ans = cli.answers()
            bull =  ge.game(var, ans, name)
            n += 1
        print('Congratulations, ' + name + '!')  


if __name__ == "__main__":
    main()
