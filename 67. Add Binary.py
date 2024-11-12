# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/add-binary/
# ----------------------------
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bits = []
        overflow = 0
        index_for_a = len(a) - 1
        index_for_b = len(b) - 1

        while index_for_a >= 0 or index_for_b >= 0 or overflow != 0:
            digit_from_a = 0 if index_for_a < 0 else int(a[index_for_a])
            digit_from_b = 0 if index_for_b < 0 else int(b[index_for_b])
            sum = digit_from_a + digit_from_b + overflow

            if sum // 2 != 0:
                overflow = 1
                sum %= 2
            else:
                overflow = 0

            bits.insert(0, str(sum))
            index_for_a -= 1
            index_for_b -= 1


        return "".join(bits)
