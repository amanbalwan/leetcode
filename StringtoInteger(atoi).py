class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        a=""
        
        
        
    
        ls = list(s.strip())
        if len(ls)<1:
            return 0
        z = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        while i < len(ls) and ls[i].isdigit() :
            a+=ls[i]
            i+=1
        try:
            a=int(a)
        except:
            return 0
            
           
         
        return max(-2**31, min(z*a,2**31-1))

####alt
class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        a=0
        
    
        ls = list(s.strip())
        if len(ls)<1:
            return 0
        z = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        while i < len(ls) and ls[i].isdigit() :
            a=a*10+int(ls[i])
            i+=1
       
            
           
         
        return max(-2**31, min(z*a,2**31-1))

###alt
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        #ls = list(s.strip())
        #if len(ls) == 0 : return 0
        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))