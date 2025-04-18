#!/usr/bin/env python
"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order.
If no four numbers sum up to the target sum, the function should return an empty array.

Sample Input
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

Sample Output
[17, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
"""

from typing import List

# Time Complexity O(n^3) and Space Complexity is O(1)
def four_sum(arr: List[int], targetSum: int) -> List[List[int]]:
    sorted_array = sorted(arr)
    start_pos = 0
    result = []
    while start_pos < len(arr):
        level_one_start_pos = start_pos + 1
        while level_one_start_pos < len(arr):
            level_two_start_pos = level_one_start_pos + 1
            end_pos = len(arr) - 1
            while level_two_start_pos < len(arr) and level_two_start_pos < end_pos:
                current_sum = (
                    sorted_array[start_pos]
                    + sorted_array[level_one_start_pos]
                    + sorted_array[level_two_start_pos]
                    + sorted_array[end_pos]
                )
                if current_sum == targetSum:
                    result.append(
                        [
                            sorted_array[start_pos],
                            sorted_array[level_one_start_pos],
                            sorted_array[level_two_start_pos],
                            sorted_array[end_pos],
                        ]
                    )
                    level_two_start_pos += 1
                    end_pos -= 1
                elif current_sum > targetSum:
                    end_pos -= 1
                else:
                    level_two_start_pos += 1
            level_one_start_pos += 1
        start_pos += 1

    return result

if __name__ == "__main__":
    response = four_sum([7, 6, 4, -1, 1, 2], 16)
    print(response)
