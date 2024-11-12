# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/plus-one/
# ----------------------------
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits.copy()
        index = len(digits) - 1
        overflow = 0

        while index >= 0:
            digit = digits[index]
            sum = digit + (1 if index == len(digits) - 1 else 0) + overflow

            if sum // 10 != 0:
                overflow = sum // 10
                sum %= 10
            else:
                overflow = 0

            result[index] = sum
            index -= 1

        if overflow != 0:
            result.insert(0, overflow)

        return result