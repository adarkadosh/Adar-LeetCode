from typing import List


# My solution
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]
        for i in range(1, len(nums)):
            temp ^= nums[i]
        return temp


# Optimized solution - by chat
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the single number in a list where every other number appears twice.

        Args:
        nums (list[int]): The list of integers where every element appears twice except for one.

        Returns:
        int: The single number that appears only once.
        """
        # Initialize result to 0
        # This variable will store the XOR result of all numbers
        result = 0

        # Loop through each number in the list
        for num in nums:
            # XOR the current number with the result
            # If the number has appeared before, it cancels out (num ^ num = 0)
            # If the number hasn't appeared, it gets added to the result
            result ^= num

        # After the loop, the result contains the single number
        return result
