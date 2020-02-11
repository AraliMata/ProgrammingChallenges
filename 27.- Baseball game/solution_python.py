class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        
        for i in ops:
            if i == '+':
                points.append(points[-1] + points[-2])
            elif i == 'D':
                points.append(points[-1] * 2)
            elif i == 'C':
                points.pop(-1)
            else:
                points.append(int(i))
            
         
            
        return sum(points)
                