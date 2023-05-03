import math as m
x=9

# s=int(m.sqrt(x))
# print(s)

  
r=x

while(r*r>x):
    r=int((r+x/r)/2)
print(int(r))



