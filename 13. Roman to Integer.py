# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/roman-to-integer
# ----------------------------
roman_digits = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        component = 0
        previous_digit = 0

        # MCMXCIV
        for letter in s[::-1]:
            digit = roman_digits[letter]

            if digit >= previous_digit:
                component += digit
                number += component
                component = 0
            else:
                component -= digit

            previous_digit = digit

        if component != 0:
            number += component

        return number

if __name__ == '__main__':
    while True:
        print(Solution().romanToInt(input()))