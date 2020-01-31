class Solution:
    def convertToBase7(self, num: int) -> str:
        n = -1
        div = 2
        baseSeven = ''
        
        if(num == 0):
            return '0'
        
        if(num < 0):
            baseSeven = str(num)
            baseSeven = baseSeven [1::]
            num = int(baseSeven)
            baseSeven = '-'
        
        while(div > 0):
            n += 1
            div = num // pow(7, n)
        
        for i in range(n - 1, -1, -1):
            div = num // pow(7, i)
            num = num % pow(7, i)
            baseSeven += str(div)
            
        return baseSeven