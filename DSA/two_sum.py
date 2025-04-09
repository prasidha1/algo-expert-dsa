#!/usr/bin/env python
"""
Difficulty: Easy
Description: Two Number Sum
    Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.
    Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.
    You can assume that there will be at most one pair of numbers summing up to the target sum.

    Sample Input
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 10
    Sample Output
        [-1, 111 // the numbers could be in reverse order
"""

from typing import List, Tuple

# Time complexity: O(n^2) and Space complexity: O(1)
def find_pairs_brut_force(array: List, target_sum: int) -> List[Tuple]:
    pairs = []
    index = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum_of_pairs = array[i] + array[j]
            if sum_of_pairs == target_sum:
                pairs.append((array[i],array[j]))
                index.append((i,j))
    return pairs

# Time complexity: O(n) and Space complexity: O(n)
def find_pairs_for_optimized_time(array: List, target_sum: int) -> List[Tuple]:
    lookup = {}
    pairs = []
    index = []
    for pos,i in enumerate(array):
        compliment_of_i = target_sum - i
        if compliment_of_i in lookup:
            pairs.append((i, compliment_of_i))
            index.append((pos, lookup.get(compliment_of_i)))
        else:
            lookup[i] = pos
    return pairs
 
# Time complexity: O(nlogn) and Space complexity: O(1)
def find_pairs_for_optimized_space_and_time(array: List, target_sum: int) -> List[Tuple]:
    pairs = []
    index = []
    left = 0
    right = len(array) - 1
    array.sort()
    while left < right:
        sum_of_positional_values = array[left] + array[right]
        if sum_of_positional_values < target_sum:
            left += 1
        elif sum_of_positional_values > target_sum:
            right -= 1
        else:
            pairs.append((array[left], array[right]))
            index.append((left, right))
            left += 1
    
    return pairs
        



if __name__ == "__main__":
    print(find_pairs_for_optimized_space_and_time([1,2,3,4,5], 6))