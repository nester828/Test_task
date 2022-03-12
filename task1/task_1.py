#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
n=int(sys.argv[1])
m=int(sys.argv[2])
a=[i for i in range(1,n+1)]
i=0
while True:
    print(a[i],end='')
    i+=m-1
    a=a+a
    if a[i]==1:
        break

