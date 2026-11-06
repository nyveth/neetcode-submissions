class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in mapping:
                stack.append(char)

            elif len(stack) == 0:
                return False

            else:
                last_char = stack.pop()
                if mapping[last_char] != char:
                    return False
        return len(stack) == 0