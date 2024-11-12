# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/longest-alternating-subarray/description/
# ----------------------------
from math import copysign, floor
from typing import List


def sign(number: int) -> int:
    return floor(copysign(1, number))


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        index = 1
        previous_difference = 0
        max_length = 0
        current_length = 0

        while index < len(nums):
            current = nums[index]
            previous = current if index == 0 else nums[index - 1]
            current_difference = current - previous

            if previous_difference == 1 and current_difference != -1 or previous_difference == -1 and current_difference != 1:
                max_length = max(max_length, current_length)
                current_length = 0

            if current_difference == -1 and current_length == 0:
                current_length = 1

            if current_difference == 1 and previous_difference != -1:
                current_length = 2
            elif current_difference == 1 and previous_difference == -1 and current_length != 0 or current_difference == -1 and previous_difference == 1:
                current_length += 1

            previous_difference = current_difference
            index += 1

        max_length = max(max_length, current_length)
        return -1 if max_length < 2 else max_length


print(Solution().alternatingSubarray([3,2,3,3,2,1,1]))