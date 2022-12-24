'''
Day 1: Calorie Counting
---
Each elf has a list of calories of their
food gathered separated by an empty line.
Find out which elf has the most calories
of food.
'''

import time

with open("/workspaces/advent-of-code/2022/day1.txt", "r", encoding="utf-8") as f:
    day1 = f.read()

def sumCalories(input_list):
    split_elf = input_list.split("\n\n")
    split_food = [list(map(int, item.split())) for item in split_elf]
    return [sum(calories) for calories in split_food]


def findMax(input_list):
    max_calories = max(input_list)
    index_of = input_list.index(max_calories)
    return [index_of, max_calories]


def findTop3(input_list):
    sorted_list = sorted(input_list)
    return sorted_list[-3:]


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Start of Code

    elf_data = sumCalories(day1)
    index_of, max_calories = map(int, findMax(day1))
    
    print(
        f"Elf {index_of+1} carries the most calories with a total of {max_calories} calories"
    )

    print(
        f"The sum of the top 3 calories are {sum(findTop3(elf_data))}"
    )
    # End of Code

    end_time = time.perf_counter()
    print("Elapsed time:", end_time - start_time)
