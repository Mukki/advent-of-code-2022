# https://adventofcode.com/2022/day/2

import sys


def main():
    if len(sys.argv) != 2:
        print("Please provide the data file for the challenge.")
        print("usage: rock-paper-scissors.py data.txt")
        exit()

    # part 1
    strategy_guide = []

    with open(sys.argv[1], "r") as data:
        strategy_guide = data.readlines()

    strategy_guide = map(str.strip, strategy_guide)
    strategy_guide = map(replace_rock_paper_scissor, strategy_guide)
    strategy_guide = map(lambda s: s.split(" "), strategy_guide)

    score = 0

    strategy_guide = list(strategy_guide)  # this is necessary for part 2

    for strategy in strategy_guide:
        # score for type of moves
        if strategy[1] == "rock":
            score += 1
        if strategy[1] == "paper":
            score += 2
        if strategy[1] == "scissors":
            score += 3

        # score for draw
        if strategy[0] == strategy[1]:
            score += 3

        # score for winning
        if (
            ((strategy[1] == "rock") and (strategy[0] == "scissors"))
            or ((strategy[1] == "paper") and (strategy[0] == "rock"))
            or ((strategy[1] == "scissors") and (strategy[0] == "paper"))
        ):
            score += 6

    print("The answer for part 1 is:", score)

    # part 2
    strategy_guide = map(replace_win_draw_lose, strategy_guide)

    score = 0

    for strategy in strategy_guide:
        # score for strategy
        if strategy[1] == "win":
            score += 6
        if strategy[1] == "draw":
            score += 3
        if strategy[1] == "lose":  # does nothing ¯\_(ツ)_/¯
            score += 0

        # score for type of moves
        # i know i could have put this in the if block above, but its more readable this way
        if strategy[1] == "win":
            if strategy[0] == "rock":  # win with paper
                score += 2
            if strategy[0] == "paper":  # win with scissors
                score += 3
            if strategy[0] == "scissors":  # win with rock
                score += 1
        if strategy[1] == "draw":
            if strategy[0] == "rock":  # draw with rock
                score += 1
            if strategy[0] == "paper":  # draw with paper
                score += 2
            if strategy[0] == "scissors":  # draw with scissors
                score += 3
        if strategy[1] == "lose":
            if strategy[0] == "rock":  # lose with scissors
                score += 3
            if strategy[0] == "paper":  # lose with rock
                score += 1
            if strategy[0] == "scissors":  # lose with paper
                score += 2

    print("The answer for part 2 is:", score)


def replace_rock_paper_scissor(strategy):
    strategy = strategy.replace("A", "rock")
    strategy = strategy.replace("B", "paper")
    strategy = strategy.replace("C", "scissors")
    strategy = strategy.replace("X", "rock")
    strategy = strategy.replace("Y", "paper")
    strategy = strategy.replace("Z", "scissors")

    return strategy


def replace_win_draw_lose(strategy):
    strategy[1] = strategy[1].replace("rock", "lose")
    strategy[1] = strategy[1].replace("paper", "draw")
    strategy[1] = strategy[1].replace("scissors", "win")

    return strategy


if __name__ == "__main__":
    main()
