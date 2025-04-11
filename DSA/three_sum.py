"""
Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output
[I-8, 2, 6], [-8, 3, 51, [-6, 1, 5]]
"""

from typing import List

def three_sum_pairs_brute_force(array: List[int], target_sum: int):
    pairs = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                current_sum = array[i] + array[j] + array[k]
                if current_sum == target_sum:
                    pairs.append((array[i], array[j], array[k]))
    
    return pairs


# Time complexity O(n^2) and space complexity O(n)
def three_sum_pairs_optimal(array: List[int], target_sum: int):
    pairs = []
    pivot = 0
    array.sort()
    while pivot < len(array):
        left = pivot + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[pivot] + array[left] + array[right]
            if current_sum == target_sum:
                pairs.append((array[pivot], array[left], array[right],))
                left += 1
                right += 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
        pivot += 1

    return pairs

if __name__ == "__main__":
    result = three_sum_pairs_brute_force([12, 3, 1, 2, -6, 5, -8, 6], 0)
    print(result)