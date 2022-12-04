# https://adventofcode.com/2022/day/3

import sys


def main():
    if len(sys.argv) != 2:
        print("Please provide the data file for the challenge.")
        print("usage: rucksack-reorganization.py data.txt")
        exit()

    # part 1
    rucksacks = []

    with open(sys.argv[1], "r") as data:
        rucksacks = data.readlines()

    priorities = 0

    for items in rucksacks:
        items = items.strip()
        number_of_items_in_compartments = len(items) // 2

        first_compartment = set(items[0:number_of_items_in_compartments])
        second_compartment = set(items[number_of_items_in_compartments:])

        common_letter = first_compartment.intersection(second_compartment).pop()

        # ord() gives the ascii value.
        # the lowercase letters start at 97, so we need to offset each value by 96
        # the uppercase letters start at 65, but are +26 in priorities, so we need to offset by 38
        priorities += ord(common_letter) - (
            (97 - 1) if common_letter.islower() else (65 - 1 - 26)
        )

    print("The answer for part 1 is:", priorities)

    # part 2

    badge_priorities = 0

    # iterate 3 at a time
    for first_rucksack, second_rucksack, third_rucksack in zip(*[iter(rucksacks)] * 3):
        first_rucksack = set(first_rucksack.strip())
        second_rucksack = set(second_rucksack.strip())
        third_rucksack = set(third_rucksack.strip())

        common_letter = (
            first_rucksack.intersection(second_rucksack)
            .intersection(third_rucksack)
            .pop()
        )

        # similar to part 1
        badge_priorities += ord(common_letter) - (
            (97 - 1) if common_letter.islower() else (65 - 1 - 26)
        )

    print("The answer for part 2 is:", badge_priorities)


if __name__ == "__main__":
    main()
