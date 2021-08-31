class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # convert input integer to string

        stringForm = str(x)

        # check some base cases
        if (len(stringForm) == 1):
            intForm = int(stringForm)
            return intForm
        else:

            if (stringForm[-1] == 0):
                stringForm[:-1]

            # split string
            # arrayOfInts = stringForm.split()

            finalVersion = ""
            negative = False

            if (stringForm[0] == '-'):
                negative = True
                stringForm = stringForm[1:]

            # read each string in reverse
            for i in range(len(stringForm) - 1, -1, -1):
                # print("Counter")
                # print(i)
                # finalVersion = finalVersion + str(i)

                currentI = str(stringForm[i])
                finalVersion = finalVersion + currentI

            # convert back to int

        if (negative == True):
            finalVersion = '-' + finalVersion

        output = int(finalVersion)

        if (output > 2147483647 or output < -2147483648):
            output = 0

        return output