# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         l=len(digits)
#         s=1
#         i=l-1
        
#         if(digits[i]+1<10):
#             digits[i]+=1
#             return digits
#         else:
#             while(i>=0):
#                 if(i==0 and digits[i]>8):
#                     digits[i]=(digits[i]+1)%10
#                     digits=[1]+digits
#                     return digits
#                 if digits[i] < 9:
#                     digits[i]=digits[i]+1
#                     return digits
#                 else:
#                     digits[i]=0
#                     i-=1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)-1
        while(digits[l]==9):
            digits[l]=0
            l-=1
        if(l<0):
            digits=[1]+digits
        else:
            digits[l]+=1
        return digits
            
            

            
        
            
digits=[9,9]
s=Solution()
k=s.plusOne(digits)
print(k)