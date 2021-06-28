#!/usr/bin/env python
from brain_games import engine
from brain_games.games import progression


def main():
    engine.start_engine(progression.start_progression,
                        progression.ask_task, progression.ask_question)


if __name__ == '__main__':
    main()
