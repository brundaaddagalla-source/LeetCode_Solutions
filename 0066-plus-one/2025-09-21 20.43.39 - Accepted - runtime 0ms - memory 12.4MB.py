class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]=digits[-1]+1
        i=len(digits)-1
        while i>=0 and digits[i]>9:
            s=str(digits[i])
            digits[i] = int(s[1])         
            if i == 0:     
                x=int(s[0])              
                digits.insert(0,x)
            else:
                digits[i-1] += int(s[0])  
            i -= 1
        return digits
        