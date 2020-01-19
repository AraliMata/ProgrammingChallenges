class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        
        for i in s:
            value += romanNum.get(i)
        
        for j in range (len(s) - 1):
            
            if s[j] == 'I' and (s[j+1] == 'V' or s[j+1] == 'X'):
                value -= 2
            if s[j] == 'X' and (s[j+1] == 'L' or s[j+1] == 'C'):
                value -= 20
            if s[j] == 'C' and (s[j+1] == 'D' or s[j+1] == 'M'):
                value -= 200
        
        return value