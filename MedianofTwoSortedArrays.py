class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=nums1+nums2
        num3.sort()
        l=len(num3)
        if l%2!=0:
            m=l//2
            return num3[m]
        else:
            m=l//2
            f=(num3[m]+num3[m-1])/2
            return f
        