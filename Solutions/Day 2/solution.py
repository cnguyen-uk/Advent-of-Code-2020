# -*- coding: utf-8 -*-
"""
Day 2: Password Philosophy
https://adventofcode.com/2020/day/2
"""

# Initially it looks like a clean solution could be created to this
# problem using a dictionary.  Unfortunately some lines in input.txt
# are repeated, so instead we have to deal with nested list indexing.

with open('input.txt') as input:
    input_list = input.read().splitlines()

formatted_list = []
for line in input_list:
    formatted_list.append(line.split(": "))

# This section solves Part One.
valid_password_count = 0
for pair in formatted_list:
    min_letter = int(pair[0][:pair[0].find("-")])
    max_letter = int(pair[0][pair[0].find("-") +1:pair[0].find(" ")])
    letter = pair[0][-1]
    password = pair[1]

    if min_letter <= password.count(letter) <= max_letter:
        valid_password_count += 1

print(valid_password_count)

# This section solves Part Two.
valid_password_count = 0
for pair in formatted_list:
    position1 = int(pair[0][:pair[0].find("-")]) - 1
    position2 = int(pair[0][pair[0].find("-") +1:pair[0].find(" ")]) - 1
    letter = pair[0][-1]
    password = pair[1]

    if (password[position1] == letter) ^ (password[position2] == letter):
        valid_password_count += 1

print(valid_password_count)
