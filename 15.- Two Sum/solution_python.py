class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        c = 0
        
        while i < len(nums):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [c, c + j]
                
            nums.pop(i)
            c += 1