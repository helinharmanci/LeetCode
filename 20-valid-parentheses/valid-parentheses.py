class Solution:
    def isValid(self, s: str) -> bool:
        length= len(s)
        stack = []
        index = 0
        if s[0] in [')', '}', ']']:
            return False
        if len(s) == 1 :
            return False

        stack.append('d')
        while (index < len(s)):
            if (s[index] in ['(', '[', '{']):
                stack.append(s[index])
            else:
                if (stack[-1]=='(' and s[index]==')'):
                    stack.pop()
                elif stack[-1]=='{' and s[index]=='}':
                    stack.pop()
                elif (stack[-1]=='[' and s[index]==']'):
                    stack.pop()
                else:
                    return False
            index +=1
        
        if len(stack) !=1:
            return False
        return True
