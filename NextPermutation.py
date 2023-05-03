class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(a)
        for i in range(l-1,0,-1):
            if a[i]>a[i-1]:
                
                for j in range(l-1,i-1,-1):
                    if a[j]>a[i-1]:
                        temp=a[j]
                        a[j]=a[i-1]
                        a[i-1]=temp
                        l, r = i, len(a)-1  # reverse the second part
                        while l < r:
                            a[l], a[r] = a[r], a[l]
                            l +=1 ; r -= 1
                        return
        a.reverse()
        return

####
class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=None
        l=len(a)
        for k in range(l-1,0,-1):
            if a[k]>a[k-1]:
                i=k
                break
                
        if i:
            
            for j in range(l-1,i-1,-1):
                if a[j]>a[i-1]:
                    temp=a[j]
                    a[j]=a[i-1]
                    a[i-1]=temp
                    l, r = i, len(a)-1  # reverse the second part
                    while l < r:
                        a[l], a[r] = a[r], a[l]
                        l +=1 ; r -= 1
                    return
        a.reverse()
        return

###fastest with while
class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=None
        l=len(a)
        k=l-1
        while k>0:
            if a[k]>a[k-1]:
                i=k
                break
            k-=1
                
        if i:
            j=l-1
            while j>i-1:
                if a[j]>a[i-1]:
                    temp=a[j]
                    a[j]=a[i-1]
                    a[i-1]=temp
                    l, r = i, len(a)-1  # reverse the second part
                    while l < r:
                        a[l], a[r] = a[r], a[l]
                        l +=1 ; r -= 1
                    return
                j-=1
        a.reverse()
        return
        
###while type 2
class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=None
        l=len(a)
        k=l-1
        while k>0:
            if a[k]>a[k-1]:
                i=k
                break
            k-=1
                
        if i:
            j=l-1
            while j>i-1:
                if a[j]>a[i-1]:
                    temp=a[j]
                    a[j]=a[i-1]
                    a[i-1]=temp
                    l, r = i, len(a)-1  # reverse the second part
                    break
                j-=1
            while l < r:
                        a[l], a[r] = a[r], a[l]
                        l +=1 ; r -= 1
            return
        a.reverse()
        return
        
        