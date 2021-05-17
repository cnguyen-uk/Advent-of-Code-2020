# -*- coding: utf-8 -*-
"""
Day 6: Custom Customs
https://adventofcode.com/2020/day/6
"""

# This problem is, just like Day 4, mostly about formatting the
# input data into a workable form.  Once again, the nature of
# the reformatting requires a newline after group's answer, so the
# initial input_list has this manually added on, since splitline()
# removes ending newlines.

with open('input.txt') as input:
    input_list = input.read().splitlines() + [""]

def cumulative_group_answers(input_list):
    """Convert a 2D input_list into a 1D list of concatenated group answers."""
    cumulative_group_answers_list = []
    holder_string = ""
    for line in input_list:
        if line != "":
            holder_string += line
        else:
            cumulative_group_answers_list.append(holder_string)
            holder_string = ""
    return cumulative_group_answers_list

# This function converts a list of concatenated answers into a
# list of unique concatenated answers.
def unique_group_answers(concatenated_input_list):
    """Convert a list of concatenated group answers into a unique version."""
    unique_group_answers = []
    for answer in cumulative_group_answers(concatenated_input_list):
        unique_group_answers.append("".join(list(set(list(answer)))))
    return unique_group_answers

# This section solves Part One.
print(sum([len(answer) for answer in unique_group_answers(input_list)]))

# This section solves Part Two.
def group_size(input_list):
    """Return the number of people per group from the input_list."""
    headcount_list = []
    count = 0
    for line in input_list:
        if line != "":
            count += 1
        else:
            headcount_list.append(count)
            count = 0
    return headcount_list

count = 0
for item in zip(cumulative_group_answers(input_list), group_size(input_list)):
    unique_letters_list = unique_group_answers([item[0]] + [""])
    print(unique_letters_list[0])
    for letter in unique_letters_list[0]:
        if item[0].count(letter) == item[1]:
            count += 1

print(count)
