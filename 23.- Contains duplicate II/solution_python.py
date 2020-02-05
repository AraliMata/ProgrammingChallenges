class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums1 = set(nums)
        
        if len(nums) == len(nums1):
            return False
        else:
            if(len(nums) < k):
                return True
            for i in range (len(nums)):
                if nums.count(nums[i]) > 1:
                    count = 1
                    while count <= k:
                        if count + i < len(nums):
                            if nums[i] == nums[i + count]:
                                return True
                        count += 1
        return False