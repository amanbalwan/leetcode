from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        k=m
        for i in range(n):
            nums1[k]=nums2[i]
            k+=1
        for i in range(m+n):
            for j in range(i,m+n):
                if nums1[i]>nums1[j]:
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp
        return nums1

s=Solution()
nums1=[4,5,6,0,0,0]
m=3
nums2=[1,2,3]
n=3
k=s.merge(nums1,m,nums2,n)
print(k)
                    
            
            
        