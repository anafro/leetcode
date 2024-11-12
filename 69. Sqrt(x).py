# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/sqrtx/
# ----------------------------

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        middle = 0

        while left <= right:
            middle = (left + right) // 2
            square = middle ** 2

            if square == x:
                return middle

            if square > x:
                right = middle - 1

            if square < x:
                if (middle + 1) ** 2 > x:
                    return middle

                if (middle + 1) ** 2 == x:
                    return middle + 1

                left = middle + 1

        return middle

print(Solution().mySqrt(1))