class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle is "":
            return 0

        if haystack.find(needle) != -1:
            index = haystack.find(needle)
            return index

        return -1
