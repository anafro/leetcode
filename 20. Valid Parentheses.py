# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/valid-parentheses/description/
# ----------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        curve_level = 0
        square_level = 0
        parenthesis_level = 0
        scope_stack = []

        for character in s:
            if character == '[':
                square_level += 1
                scope_stack.append(character)

            if character == ']':
                square_level -= 1

                if len(scope_stack) == 0 or scope_stack.pop() != '[':
                    return False

            if character == '(':
                parenthesis_level += 1
                scope_stack.append(character)

            if character == ')':
                parenthesis_level -= 1

                if len(scope_stack) == 0 or scope_stack.pop() != '(':
                    return False

            if character == '{':
                curve_level += 1
                scope_stack.append(character)

            if character == '}':
                curve_level -= 1

                if len(scope_stack) == 0 or scope_stack.pop() != '{':
                    return False

            if square_level < 0 or parenthesis_level < 0 or curve_level < 0:
                return False

        return square_level == 0 and parenthesis_level == 0 and curve_level == 0