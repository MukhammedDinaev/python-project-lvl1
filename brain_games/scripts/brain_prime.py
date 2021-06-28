#!/usr/bin/env python
from brain_games import engine
from brain_games.games import prime


def main():
    engine.start_engine(prime.start_prime, prime.ask_task, prime.ask_question)


if __name__ == '__main__':
    main()
