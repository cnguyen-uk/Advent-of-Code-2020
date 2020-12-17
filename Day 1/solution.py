# -*- coding: utf-8 -*-
"""
Day 1: Report Repair
https://adventofcode.com/2020/day/1
"""

# This problem is a special case of the subset sum problem and could
# be solved more elegantly, with a lower complexity solution, or more
# generally, with recursion.

with open('input.txt') as input:
    input_list = input.read().splitlines()

input_list = [int(i) for i in input_list]

# This section solves Part One.
for i in range(len(input_list)):
    for j in range(len(input_list[i+1:])):
        if input_list[i] + input_list[i+j]== 2020:
            print(input_list[i] * input_list[i+j])

# This section solves Part Two.
for i in range(len(input_list)):
    for j in range(len(input_list[i+1:])):
        for k in range(len(input_list[i+j+1:])):
            if input_list[i] + input_list[i+j] + input_list[i+j+k] == 2020:
                print(input_list[i] * input_list[i+j] * input_list[i+j+k])
