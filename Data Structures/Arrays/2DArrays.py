#!/bin/python3


# https://www.hackerrank.com/challenges/2d-array

import sys

ARRAY_SIZE = 6


def sum_of_hourglass(i, j):
    hrglass_sum = 0
    for adder in range(-1, 2):
        hrglass_sum += (arr[i+adder][j+adder] +
                        arr[i+adder][j-adder] +
                        arr[i+adder][j])
    hrglass_sum -= (2 * arr[i][j])
    return hrglass_sum

max_sum = -100000
arr = []
for arr_i in range(ARRAY_SIZE):
    arr.append(list(map(int, input().strip().split(' '))))


for i in range(1, ARRAY_SIZE-1):
    for j in range(1, ARRAY_SIZE-1):
        max_sum = max(max_sum, sum_of_hourglass(j, i))
print(max_sum)