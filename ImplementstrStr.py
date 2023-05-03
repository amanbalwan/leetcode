haystack = "hello"
needle = "l"

k=-1       
z=len(haystack)
p=0
l=len(needle)
print(l)
for i in range(z):
    if needle[p] == haystack[i]:
        if(l==1):
            print(i)
            break
        else:
            while(p<l):
                p+=1
                i+=1
                needle[p] == haystack[i]
            if p==(l-1):
                print(k)
                break