class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=len(s)

        i=a-1
        k=0
        
        for p in range(a):
            
            if(s[i]!=" "):
                while(i>=0):
                    if(s[i] != " "):

                        k+=1
                        i-=1
                        
                        if (i<0):
                            return k
                    else:
                        return k
            i-=1
                        

s=Solution()
k=s.lengthOfLastWord("s")
print(k)