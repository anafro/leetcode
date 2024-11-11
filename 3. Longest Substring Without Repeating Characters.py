# ----------------------------
# Category: Medium
# Leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# ----------------------------
import math


def are_all_chars_unique(string: str) -> bool:
    chars = set(string)
    return all(string.count(char) == 1 for char in chars)


def has_unique_of_length(string: str, length: int) -> bool:
    if len(string) < length:
        return False

    begin = 0
    end = length

    while end <= len(string):
        substring = string[begin:end]

        if are_all_chars_unique(substring):
            return True
        else:
            begin += 1
            end += 1

    return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        if len(s) == 1:
            return 1

        max_length = len(s)
        factor = math.ceil(len(s) / 2)

        while factor != 0:
            has_unique = has_unique_of_length(s, max_length)
            has_unique_upcoming = has_unique_of_length(s, max_length + 1)
            if has_unique and not has_unique_upcoming:
                return max_length

            if has_unique:
                max_length += factor
                factor //= 2
            else:
                max_length -= factor
                factor //= 2

            if factor == 0:
                factor = 1

        return max_length

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("jlygy"))