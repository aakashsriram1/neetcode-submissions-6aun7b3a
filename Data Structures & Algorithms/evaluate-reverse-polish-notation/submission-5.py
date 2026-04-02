class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i in ("+", "-", "/", "*"): 
                y = int(stack.pop())
                x = int(stack.pop())
                if i == '+':
                    stack.append(x+y)
                elif i == "-":
                    stack.append(x-y)
                elif i == "*":
                    stack.append(x*y)
                else:
                    stack.append(x/y)
            else:
                stack.append(i)
        return int(stack[-1])