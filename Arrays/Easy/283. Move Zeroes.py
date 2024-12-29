from typing import List


class Solution1:
    # My solution
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        cur_index = 0
        last_index = len(nums) - 1
        while cur_index < last_index:
            if nums[cur_index] == 0:
                nums = self.bubble(nums, cur_index)
                last_index -= 1
            else:
                cur_index += 1
        return

    def bubble(self, nums: List[int], index):
        for i in range(index, len(nums) - 1):
            temp = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = temp
        return nums


### Optimized solution by chat ###
"""
Problem: Move Zeroes (https://leetcode.com/problems/move-zeroes/)
Difficulty: Easy

Approach:
- Use a two-pointer technique to move non-zero elements forward.
- Place zeros at the end of the list in place.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
