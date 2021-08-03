from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or path[0] != '/':
            return '/'
        split_path = path.split('/')
        stack = []
        for path in split_path:
            if path == '' or path == '.':
                continue
            elif path == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(path)
        return '/' + '/'.join(stack)