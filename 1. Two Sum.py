# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/two-sum/
# ----------------------------
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = nums.copy()
        sorted_nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            left_num = sorted_nums[left]
            right_num = sorted_nums[right]
            sum = left_num + right_num

            if sum > target:
                right -= 1

            if sum < target:
                left += 1

            if sum == target:
                return [nums.index(left_num), len(nums) - nums[::-1].index(right_num) - 1]

        return []
