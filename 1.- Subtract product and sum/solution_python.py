class Solution:
    def subtractProductAndSum(n):
        product = 1
        su = 0
        
        for i in n:
            digit = int(i)
            product *= digit
            su += digit
        
        return product - su
    
    n = input()
    print(subtractProductAndSum(n))