class Solution:
    def isHappy(self, n: int) -> bool:
        nStr = str(n)
        numbers = set()
        i = 0
    
        while i != 1:
            i = 0
            
            for j in range(len(nStr)):
                i += pow(int(nStr[j]), 2)
    
            if i == 1:
                return True 
            elif i in numbers:
                return False
            else:
                nStr = str(i)
                numbers.add(i)