class Solution:
    def isValid(self, s):

        if len(s) == 1:
            return False

        if len(s) % 2 != 0:
            return False

        listNormal = s.count('(')
        listEndNormal = s.count(')')

        listBracketStart = s.count('[')
        listBracketEnd = s.count(']')

        listObjectStart = s.count('{')
        listObjectEnd = s.count('}')

        if listNormal != listEndNormal:
            return False

        if listBracketStart != listBracketEnd:
            return False

        if listObjectStart != listObjectEnd:
            return False

        stack = []
        for i in s:

            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            if i == ')' or i == ']' or i == '}':
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()

                if i == ']' and stack[-1] == '[':
                    stack.pop()

                if i == '}' and stack[-1] == '{':
                    stack.pop()

        if len(stack) > 0:
            return False

        return True