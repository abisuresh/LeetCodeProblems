import bisect
import typing


class Solution:
    def searchInsert(self, nums: typing.List[int], target: int) -> int:
        if len(nums) == 1 and target < nums[0]:
            return 0

        if len(nums) == 1 and target > nums[0]:
            return 1

        if target not in nums:
            next_index = bisect.bisect(nums, target)
            index = next_index

        else:
            index = nums.index(target)

        return index

