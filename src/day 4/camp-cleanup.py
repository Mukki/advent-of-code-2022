# https://adventofcode.com/2022/day/4

import sys


def main():
    if len(sys.argv) != 2:
        print("Please provide the data file for the challenge.")
        print("usage: camp-cleanup.py data.txt")
        exit()

    pairs = []

    # part 1 & 2
    with open(sys.argv[1], "r") as data:
        for pair in data.readlines():
            pair = pair.strip()
            pair = pair.split(",")
            pair[0] = pair[0].split("-")
            pair[1] = pair[1].split("-")
            pairs.append(pair)

    number_of_pair_contains_the_other = 0
    number_of_pair_that_overlap = 0

    for pair in pairs:
        set_one = set(range(int(pair[0][0]), int(pair[0][1]) + 1))
        set_two = set(range(int(pair[1][0]), int(pair[1][1]) + 1))

        if set_two.issubset(set_one) or set_one.issubset(set_two):
            number_of_pair_contains_the_other += 1

        if set_one.intersection(set_two):
            number_of_pair_that_overlap += 1

    print("The answer for part 1 is:", number_of_pair_contains_the_other)
    print("The answer for part 2 is:", number_of_pair_that_overlap)

if __name__ == "__main__":
    main()
