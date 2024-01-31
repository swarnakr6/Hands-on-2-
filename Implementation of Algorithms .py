#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from heapq import heappush, heappop

# -------------------insertion sort-------------------
# ""when we reach to an element we compare that element with others and find the correct place for that""
A = [3, 7, 4, 5, 0, -1, 9, 12, 10, 6, 3, 5, 6, -100]
for i in range(0, len(A)):
    item = A[i]
    k = i
    while k > 0 and A[k - 1] > item:
        A[k] = A[k - 1]
        k -= 1
    A[k] = item
print(A)


# In[2]:


# -------------------selection sort----------------------
# ""chose the element and compare with next element and change that with the smallest one""
A = [3, 7, 4, 5, 0, 9, 12, 10, 6, 3, 5, 6]
num = len(A)
for i in range(num - 1):
    selection = i
    for j in range(i + 1, num):
        if A[j] < A[selection]:
            selection = j
    A[selection], A[i] = A[i], A[selection]
print(A)


# In[4]:


# ---------------------bubble sort---------------------
# ""from end compare each element with the last element if the last one was smaller we change them""
A = [3, 7, 4, 5, 0, -1, 9, 12, 10, 6, 3, 5, 6, -100]
n = len(A)
for j in range(n):
    bubble_found = False
    for i in range(n - 1, j, -1):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            bubble_found = True
    if not bubble_found:
        break
print(A)


# In[ ]:




