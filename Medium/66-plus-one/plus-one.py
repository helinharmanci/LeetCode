class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        carried = 0
        digits[index] += 1
        
        if  digits[index] == 10:
            carried = 1
            digits[index] =0
            index -=1

        while carried > 0 and index >= 0:
            digits[index] += 1
            if  digits[index] == 10:
                carried = 1
                digits[index] =0
            else:
                carried = 0
            index -=1
        
        if carried == 1 :
            digits[0]=0
            digits.insert(0, 1)
                
        return digits
                

        