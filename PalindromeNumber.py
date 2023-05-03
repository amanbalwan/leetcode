x=1221
x=str(x)
n=len(x)
        
for i in range(0,n):
    if x[i]==x[n-i-1]:
        continue
    else:
        print("false")
        quit()
print("true")