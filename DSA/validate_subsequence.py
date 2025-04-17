#!/usr/bin/env python
"""
Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4] . Note that a single number in an array and the array itself are both valid subsequences of the array.
Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 101
sequence = [1, 6, -1, 10]
"""
from typing import List

# Time Complexity O(n) and Space Complexity O(1)
def validate_subsequence(arr: List, sub_sequence: List) -> bool:
    sub_sequence_idx = 0
    array_idx = 0

    while array_idx < len(arr) and sub_sequence_idx < len(sub_sequence):
        if arr[array_idx] == sub_sequence[sub_sequence_idx]:
            sub_sequence_idx += 1
        array_idx += 1

    return sub_sequence_idx == len(sub_sequence)

# Time Complexity O(n) and Space Complexity O(1)
def validate_sub_sequence_using_for_loop(arr: List, sub_sequence: List) -> bool:
    sub_sequence_idx = 0
    for rec in arr:
        if sub_sequence_idx == len(sub_sequence):
            break

        if rec == sub_sequence[sub_sequence_idx]:
            sub_sequence_idx += 1
    
    return sub_sequence_idx == len(sub_sequence)

if __name__ == "__main__":
    status = validate_sub_sequence_using_for_loop([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    print("Is subsequence valid?")
    print(status)