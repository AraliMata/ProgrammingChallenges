class Solution:
    def fib(self, N: int) -> int:
        prev = 0
        curr = 0
        last = 1
        
        for i in range(N):
            prev = curr
            curr = last
            last = prev + curr
        
        return curr