# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/maximum-odd-binary-number/
# ----------------------------
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        zeros = 0
        result = []

        for char in s:
            if char == '1':
                ones += 1

            if char == '0':
                zeros += 1

        while ones > 1:
            result.append('1')
            ones -= 1

        while zeros > 0:
            result.append('0')
            zeros -= 1

        result.append('1')

        return ''.join(result)