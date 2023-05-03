class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        i=0
        a=0
        b=0
        if len(s)==len(t):
            
            while(i<len(s)):
                
                if s[i] in d.keys():
                    a+=1
                    if t[i]!=d.get(s[i]):
                        
                        return False
                    
                if t[i] in d.values():
                    b+=1
                    if a-b!=0:
                        return False
                    
                else:
                    
                    d[s[i]]=t[i]
                i+=1
            return True
        else:
            return True 

###alt
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))