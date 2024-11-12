# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/climbing-stairs
# ----------------------------
def factorial(number: int) -> int:
    factorial = 1

    while number >= 1:
        factorial *= number
        number -= 1

    return factorial


def ways_out_of(steps_length_1: int, steps_length_2: int) -> int:
    return factorial(steps_length_1 + steps_length_2) // (factorial(steps_length_1) * factorial(steps_length_2))


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        max_steps_length_2 = n // 2

        steps_length_1 = n % 2
        steps_length_2 = max_steps_length_2

        while steps_length_2 >= 0:
            ways += ways_out_of(steps_length_1, steps_length_2)

            steps_length_2 -= 1
            steps_length_1 += 2

        return ways