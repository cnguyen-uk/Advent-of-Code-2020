# -*- coding: utf-8 -*-
"""
Day 3: Toboggan Trajectory
https://adventofcode.com/2020/day/3
"""

# Since the input conists of 323 lines, if the starting position is
# (0, 0), then the final position from Part One is (322, 966).  Next,
# note that since the grid pattern repeats every 31 x-coordinates,
# the input grid will need to be copied to the right 32 times to cover
# the entire journey.  This creates a 323 x 992 grid.
#
# For Part Two, the shallowest gradient through the grid is defined by
# right 7, down 1.  It follows that the final position with largest
# y-coordinate is (322, 2254).  Following the previous logic, we need
# to copy right 73 times, which creates a 323 x 2263 grid.  To avoid
# needing to create multiple grids, we can instead just use the largest
# needed grid for the entirety of the problem.

with open('input.txt') as input:
    input_list = input.read().splitlines()

# This section creates a matrix, where grid[i][j] calls the ith row,
# jth column entry.
grid = []
for line in input_list:
    copied_line = line*73
    grid.append(copied_line)

# This function returns the trees hit, where the route taken is defined
# by right n, down m.
def trees_hit(m, n):
    tree_count = 0
    for i in range(((len(grid)-1)//m) + 1):
        if grid[m*i][n*i] == "#":
            tree_count += 1
    return tree_count

# This section solves Part One.
print(trees_hit(1, 3))

# This section solves Part Two.
route_list = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
trees_hit_product = 1
for route in route_list:
    trees_hit_product *= trees_hit(route[0], route[1])
print(trees_hit_product)
