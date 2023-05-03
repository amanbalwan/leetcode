class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        maxc=0
        f=0
        a=[]
        p=0
        while p<l:
            i=p
            while i<l:
                if s[i] not in a:
                    maxc+=1
                    a.append(s[i])
                    if maxc>f:
                        f=maxc

                else:
                    
                    maxc=0
                    a=[]
                    i=l
                i+=1
            p+=1

           
                
        return f

###other
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        maxl=start=0
        for i,c in enumerate(s):
            if c in a and start <= a[c]:
                start=a[c]+1
            else:
                maxl=max(maxl,i-start+1)
            a[c]=i
        return maxl
                