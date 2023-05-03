list1 = [1,2,4]
list2 = [1,3,4]
list3=[]
i=0
j=0
# list3=list1+list2
# list3.sort()
# print(list3)
l1=len(list1)
l2=len(list2)
if l1>l2:
    l3=l1
else:
    l3=l2
while i<l3 and j<l3:
    if i==l3 :
        list3+=list2[j]
        j+=1
        
    elif j==l3 :
        list3+=list1[i]
        i+=1

    elif(list1[i]<list2[j]):
        list3+=list1[i]    
        i+=1

    elif(list1[i]>list2[j]):
        list3+=list2[j]
        j+=1
        print("hellp")

print(list3,"1")
    