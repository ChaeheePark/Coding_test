from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=list(permutations(nums, len(nums)))
        for i in range(len(ans)):
            ans[i]=list(ans[i])
        return ans
