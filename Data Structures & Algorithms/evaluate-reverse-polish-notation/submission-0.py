class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mapping = ['+', '*', '-', '/']

        for num in tokens:
            if num not in mapping:
                stack.append(int(num))

            if num in mapping:
                a = stack.pop()
                b = stack.pop()
                if num == '+':
                    stack.append(b + a)
                elif num == '*':
                    stack.append(b * a)
                elif num == '-':
                    stack.append(b - a)
                else:
                    stack.append(int(b / a))
        
        return stack[-1]



