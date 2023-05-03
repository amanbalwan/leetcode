# strs = [""]
# n=len(strs)
# strs.sort()
# a=strs[0][0]

# i=0
# j=0
# strs.sort()
# s=""
# b=""

# while i<len(strs):
#     if(i<1):
#         v1=len(strs[0])
#         v2=len(strs[1])
#         if (v1>v2):
#             v=v2
#         else:
#             v=v1
#         for j in range (v):
#             if(strs[0][j]==strs[1][j]):
#                 s+=(strs[0][j])
#                 print(s,"1")
#         i=i+1
#         print(i)
    
#     elif(s!=""):
#         print(i)
#         v1=len(s)
#         v2=len(strs[i])
#         if (v1>v2):
#             v=v2
#         else:
#             v=v1
#         print(v1,"v1")
#         print(v2,"v2")
#         print(v)    

#         for j in range (v):   
#             print(strs[i][j])    
#             if(s[j]==strs[i][j]):
#                 b+=s[j]
                
#             elif(b==""):
#                 print(b,"2")
                
#                 exit()
#         i+=1
#         s=b
#         b=""
# print(s,"f1")

##2
strs=["geeksforgeeks", "geeks","geek", "geezer"]
strs.sort()
l=len(strs)
i=0

if l==0:
    print("return #1")
elif l==1:
    print(strs[0])

n=min(len(strs[0]),len(strs[l-1]))
while i < n and strs[0][i]==strs[l-1][i]:
    i+=1
a=strs[0][0:i]
print(a)