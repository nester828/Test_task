#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
a=sys.argv[2]
b=sys.argv[1]
data=[]
data1=[]
with open(a, "r") as file:
    for line in file:
        data.append(line.split())
with open(b, "r") as file1:
    for line in file1:
        data1.append(line.split())
    ox=float(data1[0][0])
    oy=float(data1[0][1])
    r=float(data1[1][0])
    m=[]
    for i in data:
        px=float(i[0])
        py=float(i[1])
        s=(ox-px)**2+(oy-py)**2
        m.append(s)
        r2=r**2
    for i in range(len(m)):
        if m[i]==r2:
            print(0)
        elif m[i]<r2:
            print(1)
        elif m[i]>r2:
            print(2)

