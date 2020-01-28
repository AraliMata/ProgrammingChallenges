class Solution:
    def addDigits(self, num: int) -> int:
        strNum = str(num)
        i = 0
        
        while i != 1:
            summ = 0
            
            for j in range(len(strNum)):
                summ += int(strNum[j])
            
            strNum = str(summ)
            i = len(strNum)
    
        return strNum