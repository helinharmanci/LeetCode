class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(': ')',
            '[': ']',  
            '{': '}'
        }
        stack = []
        stack.append(s[0])
        i = 1 
        
        while (i<len(s)):
            current = s[i]
            if (current in [')', ']', '}']) :
                if len(stack)==0:
                    return False
                
                topElement = stack[-1]
                if dic.get(topElement)!= current:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(current)
            i+=1

        if(len(stack)!=0):
            return False

        return True
        


        