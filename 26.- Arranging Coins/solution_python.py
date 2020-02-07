class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
       
        while True:
            count += i
            
            if(count > n):
                return i - 1
            
            i += 1
    
        return 0