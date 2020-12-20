# -*- coding: utf-8 -*-
"""
Day 5: Binary Boarding
https://adventofcode.com/2020/day/5
"""

# Knowledge of binary space partitioning algorithms would produce a
# better complexity solution to this problem, but given the small size
# of the puzzle input, this solution is more than good enough.

with open('input.txt') as input:
    input_list = input.read().splitlines()

# This section solves Part One.
def seat_id(seat):
    row_code = seat[:7]
    column_code = seat[7:]
    
    row = [i for i in range(128)]
    for character in row_code:
        if character == "F":
            row = row[:(len(row)//2)]
        else:
            row = row[(len(row)//2):]
    
    column = [i for i in range(8)]
    for character in column_code:
        if character == "L":
            column = column[:(len(column)//2)]
        else:
            column = column[(len(column)//2):]
    
    return row[0] * 8 + column[0]

highest_seat_id = 0
for seat in input_list:
    if seat_id(seat) > highest_seat_id:
        highest_seat_id = seat_id(seat)
print(highest_seat_id)

# This section solves Part Two.
lowest_seat_id = 1000
for seat in input_list:
    if seat_id(seat) < lowest_seat_id:
        lowest_seat_id = seat_id(seat)

possible_seats = [i for i in range(lowest_seat_id, highest_seat_id + 1)]
for seat in input_list:
    possible_seats.remove(seat_id(seat))
print(possible_seats[0])
