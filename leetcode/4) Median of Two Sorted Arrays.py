class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num = sorted(num)
        if len(num)%2==0 : 
            a=len(num)//2
            b=a-1
            return (num[a]+num[b]) / 2
        else:
            return (num[len(num)//2])
