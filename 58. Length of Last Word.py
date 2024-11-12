# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/length-of-last-word/
# ----------------------------
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        word_length = 0
        
        while index >= 0:
            character = s[index]

            if character != ' ':
                word_length += 1

            if character == ' ' and word_length != 0:
                return word_length

            index -= 1


        return word_length