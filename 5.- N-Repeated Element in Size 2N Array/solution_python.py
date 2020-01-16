class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        setL = set()
        
        for i in A:
            if i in setL:
                return i
            setL.add(i)