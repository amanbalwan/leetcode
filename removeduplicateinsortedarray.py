nums = [0,0,1,1,1,2,2,3,3,4]
l=len(nums)
print(l)
k=0
for i in range(l):
    if nums[k] != nums[i]:
        k+=1
        nums[k]=nums[i]
print(nums)