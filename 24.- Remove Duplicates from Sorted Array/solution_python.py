class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            
            if nums.count(nums[i]) > 1:
                j = 0
                count = i + 1
                
                while j < nums.count(nums[i]) - 1:
                    
                    if count < len(nums):
                        nums.pop(count)
                        
                    count += 1   
                    j += 1
                    
                if i != 0:
                    i -= 1 
            else:
                i += 1 
        
        return len(nums)