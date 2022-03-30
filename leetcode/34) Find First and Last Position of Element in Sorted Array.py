class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output=[]
        if target not in nums:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    output.append(i)
            if len(output)==1:
                output.append(output[0])
            if len(output)>2:
                return [output[0],output[-1]]
            return output
