
class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'
        for _ in range(n-1):
            s=''.join(str(len(list(group)))+digit for digit,group in itertools.groupby(s))
        return s

###alt
class Solution:
    def countAndSay(self, n: int) -> str:
        def countn(s):
            temp=''
            count=1
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    count+=1
                else:
                    temp+=str(count)+s[i]
                    count=1
            temp+=str(count)+s[-1]
            return temp
        result='1'
        for _ in range(n-1):
            result= countn(result)
        return result