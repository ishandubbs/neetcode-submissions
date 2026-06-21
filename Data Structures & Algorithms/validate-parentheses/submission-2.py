class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
        # "({[]})"
        # stack is empty
        # '(' is not in closeToOpen, so it's an opening bracket
        # push '(' to the stack
        # move to next character '{', where we do the same thing along with '[',
        # pushing it to the stack
        # next we move to ']', where it is in closeToOpen
        # we check if stack isn't empty and top element matches
        # stack[-1] == '[' == closeToOpen[']'] == '['
        # we then pop '[' from the stack, and do the same thing to '{' and '('.
        # we then return true

        # "(]"
        # stack is empty
        # '(' is not in closeToOpen, so it's an opening bracket
        # push '(' to the stack
        # move to next character '}', which is in closeToOpen
        # we check if stack isn't empty and top element matches
        # stack isn't empty, but top element is '(', which is not equal to closeToOpen['}'] == '{}'
        # we then return False