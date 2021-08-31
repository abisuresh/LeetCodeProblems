class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = False

        # convert to string
        stringForm = str(x)

        # check simple base cases like 1 digit integers
        if (len(stringForm) == 1):
            print('True')
            return True

            # check for - sign in front of number
        if (stringForm[0] == '-'):
            print('False')
            return False

        lengthString = len(stringForm)
        print('Length of string: ')
        print(lengthString)
        firstPart = ""
        secondPart = ""

        # check whether it is an even length or odd length
        # if even, split string into 2
        if (lengthString % 2 == 0):

            sizeStrings = int(lengthString / 2)

            # reverse second string into forward string
            firstHalf = stringForm[0:sizeStrings]
            print("First half")
            print(firstHalf)
            secondHalf = stringForm[sizeStrings:lengthString]
            print("Second half")
            print(secondHalf)

            for i in range(sizeStrings - 1, -1, -1):
                print('For loop')
                print(i)
                secondPart = secondPart + secondHalf[i]

            print('Second Part')
            print(secondPart)

            # check whether the numbers in 2 strings are the same
            intFormSecond = int(secondPart)

            # if they are, return true
            if (int(firstHalf) == intFormSecond):
                print('True')
                return True

                # if odd, find middle number and split starting after this point
        else:
            sizeCalcLength = lengthString - 1
            sizeStrings = int(lengthString / 2)

            print('Size calc length')
            print(sizeCalcLength)
            firstHalf = stringForm[0:sizeStrings]
            print('Odd first half')
            print(firstHalf)
            secondHalf = stringForm[sizeStrings + 1:lengthString]

            # remove middle number from first string
            newString = stringForm[0:sizeStrings] + stringForm[sizeStrings + 1: lengthString]
            print('New string')
            print(newString)

            # check whether the numbers in 2 strings are the same
            if (int(firstHalf) == int(secondHalf)):
                print('Odd True')
                return True
                # if they are, return true

        return palindrome