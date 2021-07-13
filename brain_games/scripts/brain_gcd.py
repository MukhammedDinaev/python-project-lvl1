#!/usr/bin/env python
from brain_games import engine
from brain_games.games import gcd


def main():
    engine.start_engine(gcd)


if __name__ == '__main__':
    main()
