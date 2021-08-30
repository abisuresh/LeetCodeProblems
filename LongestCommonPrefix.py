
# Longest Common Prefix problem
# Input list of strings
# Goal is to find longest common prefix of strings in list
class LongestPrefix:
    def longestCommonPrefix(self, strs):

        longest_prefix = ""

        # if list is empty
        if len(strs) == 0:
            return longest_prefix

            # if only one word
        # set whole word as prefix and return
        if len(strs) == 1:
            longest_prefix = strs[0]
            return longest_prefix

            # sort list
        sorted_list = strs.sort()

        # compare first and last elements of array
        first_word = strs[0]
        last_word = strs[-1]

        if first_word == last_word:
            longest_prefix = first_word
            return longest_prefix

        count = 0

        for i in first_word:
            if count > (len(last_word) - 1):
                return longest_prefix

            if (i != last_word[count]):
                return longest_prefix

            if i == last_word[count]:
                # print(i)
                longest_prefix += i

            count = count + 1

        return longest_prefix



