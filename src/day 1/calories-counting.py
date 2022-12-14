# https://adventofcode.com/2022/day/1

import sys


def main():
    if len(sys.argv) != 2:
        print("Please provide the data file for the challenge.")
        print("usage: calorie-counting.py data.txt")
        exit()

    # part 1
    calories_line = []
    calories_by_elf = []

    with open(sys.argv[1], "r") as data:
        calories_line = data.readlines()

    calories_line = map(str.strip, calories_line)

    calories_by_elf.append(0)  # add a first elf in the list

    for x in calories_line:
        if x != "":  # if it's a calorie count, add it
            calories_by_elf[-1] += int(x)
        else:  # else create a new elf
            calories_by_elf.append(0)

    maximum_caried_calories = max(calories_by_elf)

    print("The answer for part 1 is:", maximum_caried_calories)

    # part 2
    calories_by_elf.sort(reverse=True)  # sort the list from the highest first
    sum_of_3_most_caried_calories = sum(
        calories_by_elf[:3]
    )  # take the first 3 elements

    print("The answer for part 2 is:", sum_of_3_most_caried_calories)


if __name__ == "__main__":
    main()
