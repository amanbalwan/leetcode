s="III"
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
n=len(s)
print(n,"#1")
i=0
a=0

        

while i<n:
    if(i<n-1):

        if ((s[i]=='I' and (s[i+1]=='V'or s[i+1]=='X'))  or (s[i]=='X'and (s[i+1]=='L'or s[i+1]=='C'))) or (s[i]=='C'and (s[i+1]=='D' or s[i+1]=='M')):
            print(d[s[i+1]],"#2")
            a=a+d[s[i+1]] - d[s[i]]
            print(a,'#3')
            i=i+2
            print(i,"#4.1")
        else:
            a=a+d[s[i]]
            print("yes","#4.2",a,i)
            i=i+1
    else:
        a=a+d[s[i]]
        print("yes","#4.2",a,i)
        i=i+1

                
    
    
print(a,"#5")