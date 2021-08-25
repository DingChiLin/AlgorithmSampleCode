class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if not s:
            return True
        
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue

            end = stack[-1]
            if (end == '(' and c == ')') or \
               (end == '[' and c == ']') or \
               (end == '{' and c == '}'):
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
