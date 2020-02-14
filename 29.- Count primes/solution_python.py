class Solution:
    def countPrimes(self, n: int) -> int:
        countPri = 0
        count = 0
        
        if(n <= 0):
            return 0
        
        for i in range(1, n):
            for j in range(1, i):
                if i % j == 0:
                    count += 1
            if(count == 1):
                countPri += 1
            count = 0
            
        return countPri