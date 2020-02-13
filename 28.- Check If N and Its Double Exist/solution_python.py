class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in range (len(arr)):
            
            if arr[i] % 2 == 0 or 2 % arr[i] == 0:
                
                for j in range (len(arr)):
                    if i != j:
                        if arr[j] * 2 == arr[i]:
                            return True
                        elif arr[j] / 2 == arr[i]:
                            return True
        
        return False