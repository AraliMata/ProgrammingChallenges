import math
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        distances = []
        n = 0
         
        for i in range(R):
            for j in range(C):
                distances.append([i,j])
        
        distances = sorted(distances, key = lambda x: abs(r0 - x[0]) + abs(c0 - x[1]))
            
        return distances