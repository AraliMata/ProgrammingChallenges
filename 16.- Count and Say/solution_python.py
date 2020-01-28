class Solution:
    def countAndSay(self, n: int) -> str:
        num0 = '1' 
        count = 1
        
        if(n == 1):
            return '1'
        
        for i in range(n - 1):
            
            num1 = ""
            count = 1
            
            for j in range(len(num0)):
                
                if j+1 < len(num0):
                    
                    if(num0[j] == num0[j + 1]):
                        count += 1
                    else:
                        num1 += (str(count) + num0[j])
                        count = 1
                else:
                    num1 += str(count) + num0[j]
                 
            num0 = num1
            
        return num0    
            