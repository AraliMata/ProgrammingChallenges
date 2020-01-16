class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set_list = set(arr)
        numOccurr = []
        
        for i in set_list:
            numOccurr.append(arr.count(i))
            
        for i in numOccurr:
            if numOccurr.count(i) > 1:
                return False
    
    
        return True
    