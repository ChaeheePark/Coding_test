class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        
        nums=list(sorted(set(nums)))
        
        for i in range(len(nums)):
            if nums[i] >= 2**31-1 or nums[i] <= -2**31:
                nums[i] = 0
        
        for i in range(len(nums)-1):
            if nums[i]<=0:
                continue
            if nums[i]+1==nums[i+1]:
                continue
            else:
                return nums[i]+1
                
        return nums[len(nums)-1]+1
        
