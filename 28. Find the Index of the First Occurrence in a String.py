# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# ----------------------------

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        for index in range(len(haystack) - len(needle) + 1):
            begin = index
            end = index + len(needle)
            substring = haystack[begin:end]

            if substring == needle:
                return index

        return -1

Solution().strStr("abc", "c")