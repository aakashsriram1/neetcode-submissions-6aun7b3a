class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
        ')' : '(',
        '}' : '{',
        ']' : '['
        }
        stack = []

        for i in s: 
            if i in hashmap: 
                if stack and hashmap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
        