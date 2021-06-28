#!/usr/bin/env python
from brain_games import engine
from brain_games.games import calc


def main():
    engine.start_engine(calc.start_calc, calc.ask_task, calc.ask_question)


if __name__ == '__main__':
    main()
