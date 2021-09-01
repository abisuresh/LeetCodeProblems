# determine length of last word in a string that has words separated by a
# variable number of spaces
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitString = s.split(" ")
        print(splitString)

        finalString = []

        for i in splitString:
            print(i)
            if i == " ":
                break
            if i.isalpha():
                finalString.append(str(i))

        print(finalString)

        return len(finalString[-1])