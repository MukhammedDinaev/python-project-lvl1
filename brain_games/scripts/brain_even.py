#!/usr/bin/env python
from brain_games import engine
from brain_games.games import even


def main():
    engine.start_engine(even.start_even, even.ask_task, even.ask_question)


if __name__ == '__main__':
    main()
