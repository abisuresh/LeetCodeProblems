class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        array_nums1_without_zeros = nums1[:len(nums1) - n]
        joint_array = array_nums1_without_zeros + nums2
        joint_array.sort()

        for i in range(len(array_nums1_without_zeros) + len(nums2)):
            nums1[i] = joint_array[i]