# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/search-insert-position
# ----------------------------
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            element = nums[middle]

            if element < target:
                left = middle + 1

            if element > target:
                right = middle - 1

            if element == target:
                index = middle

                while nums[index] == target:
                    if index == 0:
                        return 0

                    index -= 1

                return index + 1

        return (left + right) // 2 + 1