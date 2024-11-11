# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/palindrome-number/description/
# ----------------------------
def count_digits(number: int) -> int:
    if number == 0:
        return 1

    digits_count = 0

    while number != 0:
        number //= 10
        digits_count += 1

    return digits_count


def digit_at(number: int, index: int):
    return number // (10 ** index) % 10


def reverse_digits(number: int) -> int:
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return reversed_number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = reverse_digits(x)
        return x == reversed_x

if __name__ == '__main__':
    while True:
        print(Solution().isPalindrome(int(input())))