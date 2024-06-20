class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in [')','}',']']:
                if len(stack) == 0:
                    return False
                    
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()

                    else:
                        return False

                if i == '}':
                    if stack[-1] == '{':
                        stack.pop()

                    else:
                        return False

                if i == ']':
                    if stack[-1] == '[':
                        stack.pop()

                    else:
                        return False

            else:
                stack.append(i)

        
        return True if len(stack) == 0 else False