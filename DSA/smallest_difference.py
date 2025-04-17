#!/usr/bin/env python
"""
Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.
Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input
arrayone = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output
[28, 26]
"""

from typing import List

# Time complexity O(n^2) and Space complexity O(1)
def smallest_difference_brut_force(array_one: List[int], array_two: List[int]) -> List[int]:
    smallest_pair = []
    smallest_distance = float("inf")

    for element_one in array_one:
        for element_two in array_two:
            current_distance = abs(element_one - element_two)
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                smallest_pair = [element_one, element_two]

    return smallest_pair

# Time complexity O(n) and space complexity O(1)
def smallest_difference_optimal_approach(array_one: List[int], array_two: List[int]) -> List[int]:
    smallest_pair = []
    smallest_distance = float("inf")
    sorted_array_one = sorted(array_one)
    sorted_array_two = sorted(array_two)
    idx_one = 0
    idx_two = 0

    while idx_one < len(array_one) and idx_two < len(array_two):
        element_one = sorted_array_one[idx_one]
        element_two = sorted_array_two[idx_two]

        if element_one > element_two:
            current_distance = element_one - element_two
            idx_two += 1
        elif element_two > element_one:
            current_distance = element_two - element_one
            idx_one += 1
        else:
            return [element_one, element_two]
        
        if current_distance < smallest_distance:
            smallest_distance = current_distance
            smallest_pair = [element_one, element_two]

    return smallest_pair

def smallest_difference_with_recursive_approach(array_one: List[int], array_two: List[int]) -> List[int]:
    sorted_array_one = sorted(array_one)
    sorted_array_two = sorted(array_two)

    def find_smallest(idx_one: int, idx_two: int, smallest_distance: int, smallest_pair: List[int]) -> List[int]:
        if idx_one < len(sorted_array_one) and idx_two < len(sorted_array_two):
            element_one = sorted_array_one[idx_one]
            element_two = sorted_array_two[idx_two]

            if element_one > element_two:
                current_distance = element_one - element_two
                idx_two += 1
            elif element_two > element_one:
                current_distance = element_two - element_one
                idx_one += 1
            else:
                return [element_one, element_two]
            
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                smallest_pair = [element_one, element_two]

            return find_smallest(idx_one, idx_two, smallest_distance, smallest_pair)
        return smallest_pair
    
    return find_smallest(0, 0, float("inf"), [])




if __name__ == "__main__":
    # result = smallest_difference_brut_force([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    # result = smallest_difference_optimal_approach([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    result = smallest_difference_with_recursive_approach([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    print(result)