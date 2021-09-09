import typing


class Solution:
    def maxSubArray(self, nums: typing.List[int]) -> int:
        if nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            if (nums[0] + nums[1]) > nums[0] and (nums[0] + nums[1] > nums[1]):
                return nums[0] + nums[1]
            elif nums[0] > nums[1]:
                return nums[0]
            elif nums[1] > nums[0]:
                return nums[1]

        max_value = float('-inf')
        current_value = 0

        for i in nums:
            current_value = max(i, current_value + i)
            max_value = max(max_value, current_value)

        return max_value
