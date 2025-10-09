class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str_x = str(x)
        i = len(str_x) - 1 
        for c in str_x:
            if c == str_x[i]:
                i -= 1
            else:
                return False
            if i == len(str_x)/2 - 1:
                break
        return True
        