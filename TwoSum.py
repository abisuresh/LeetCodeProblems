class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i == j and (nums[i] + nums[j] == target):
                    break
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result