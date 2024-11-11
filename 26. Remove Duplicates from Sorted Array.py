# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# ----------------------------
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        right_cut = 0
        repeats = 1
        unique_count = 1
        index = 1
        number_class = nums[0]

        while 0 <= index < len(nums) - right_cut:
            current_number = nums[index]

            if current_number == number_class:
                repeats += 1
            else:
                unique_count += 1
                number_class = current_number

                if repeats != 1:
                    index_after_shift = index - repeats + 1
                    shift_target_index = index_after_shift
                    shift_source_index = shift_target_index + repeats - 1

                    while shift_source_index < len(nums):
                        nums[shift_target_index] = nums[shift_source_index]
                        shift_source_index += 1
                        shift_target_index += 1

                    index = index_after_shift
                    right_cut += repeats - 1

                repeats = 1

            index += 1

        return unique_count

numbers = [1,1,1,2]
print(Solution().removeDuplicates(numbers), numbers)