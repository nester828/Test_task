#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
m=sys.argv[1]
nums=[]
with open(m, "r") as file:
    for line in file:
        nums.append(int(line.strip()))
    a= round(sum(nums)/len(nums))
    count=0
    for i in range(len(nums)):
        while nums[i] != a:
            if nums[i]<a:
                nums[i]+=1
                count+=1
            elif nums[i]>a:
                nums[i]-=1
                count+=1
    print(count)

