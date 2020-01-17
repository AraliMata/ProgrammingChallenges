class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        c = 0
        n_rev = ""
        
        for i in range(len(n) - 1,-1,-1):
            n_rev += n[i]
        
        for i in range(len(n)):
            if n[i] == n_rev[i]:
                c += 1
        
        if c == len(n):
            return True
        
        return False