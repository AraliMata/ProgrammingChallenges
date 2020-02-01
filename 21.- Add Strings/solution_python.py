class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        numbers = {'0':0,'1': 1, '2': 2, '3': 3,'4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        count = 0
        count1 = 0
        
        for i in num1:
            count = numbers[i] + 10 * count
        
        for i in num2:
            count1 = numbers[i] + 10 * count1
            
        
        return str(count + count1)