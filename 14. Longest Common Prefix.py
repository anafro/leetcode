# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/longest-common-prefix/
# ----------------------------
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(str) for str in strs)

        for prefix_length in range(min_length + 1):
            prefix = strs[0][:prefix_length]

            for string in strs:
                if not string.startswith(prefix):
                    return prefix[:-1]

        return min(strs, key=len)