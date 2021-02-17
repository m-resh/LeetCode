class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if (char in dict): stack.append(dict.get(char))
            elif (not stack): return False
            elif (char != stack.pop()): return False

        return not stack