# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/merge-sorted-array/
# ----------------------------
from typing import List


def insert_and_shift(number_list: List[int], new_element: int, insertion_index: int) -> None:
    shift_source_index = len(number_list) - 2
    shift_target_index = len(number_list) - 1

    while shift_source_index >= insertion_index:
        number_list[shift_target_index] = number_list[shift_source_index]

        shift_source_index -= 1
        shift_target_index -= 1

    number_list[insertion_index] = new_element


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sum_index = 0
        addend_index = 0
        first_trailing_zero_index = m

        while addend_index < len(nums2):
            sum_element = nums1[sum_index]
            addend_element = nums2[addend_index]

            if sum_element >= addend_element or sum_index >= first_trailing_zero_index:
                insert_and_shift(nums1, addend_element, sum_index)
                addend_index += 1
                first_trailing_zero_index += 1

            sum_index += 1


if __name__ == '__main__':
    ref = [1, 2, 3, 0, 0, 0]
    Solution().merge(ref, 3, [2, 5, 6], 3)
    print(ref)
