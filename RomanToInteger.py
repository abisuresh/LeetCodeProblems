# This problem entailed converting Roman Integers to Decimal Integers
class Solution:
    def romanToInt(self, s):

        int_value = 0
        new_string = s
        has_exceptions = False

        # check for I before V or X
        if "IV" in s:
            int_value += 4
            new_string = new_string.replace('IV', '')
            has_exceptions = True
            if len(s) == 2:
                return int_value

        if "IX" in s:
            int_value += 9
            new_string = new_string.replace('IX', '')
            has_exceptions = True
            if len(s) == 2:
                return int_value

                # check for X before L or C
        if 'XL' in s:
            int_value += 40
            new_string = new_string.replace('XL', '')
            has_exceptions = True
            if len(s) == 2:
                return int_value

        if 'XC' in s:
            print("In XC")
            int_value += 90
            new_string = new_string.replace('XC', '')
            print(new_string)
            has_exceptions = True
            if len(s) == 2:
                return int_value

                # check for C before D or M
        if 'CD' in s:
            int_value += 400
            new_string = new_string.replace('CD', '')
            has_exceptions = True
            if len(s) == 2:
                return int_value

        if 'CM' in s:
            int_value += 900
            new_string = new_string.replace('CM', '')
            has_exceptions = True
            if len(s) == 2:
                return int_value

                # Normal calculations

        # For I
        if has_exceptions:
            list_I = new_string.count('I')
        else:
            list_I = s.count('I')

        for i in range(list_I):
            int_value += 1
            print(int_value)

        # For. V
        if has_exceptions:
            list_V = new_string.count('V')
        else:
            list_V = s.count('V')

        for i in range(list_V):
            int_value += 5
            print(int_value)

        # For X
        if has_exceptions:
            list_X = new_string.count('X')
        else:
            list_X = s.count('X')

        for i in range(list_X):
            int_value += 10
            print(int_value)

        # For L
        if has_exceptions:
            list_L = new_string.count('L')
        else:
            list_L = s.count('L')

        for i in range(list_L):
            int_value += 50
            print(int_value)

        # For C
        if has_exceptions:
            list_C = new_string.count('C')
        else:
            list_C = s.count('C')

        for i in range(list_C):
            int_value += 100
            print(int_value)

        # For D

        if has_exceptions:
            list_D = new_string.count('D')
        else:
            list_D = s.count('D')

        for i in range(list_D):
            int_value += 500
            print(int_value)

        # For M

        if has_exceptions:
            list_M = new_string.count('M')
        else:
            list_M = s.count('M')

        for i in range(list_M):
            int_value += 1000
            print(int_value)

        return int_value