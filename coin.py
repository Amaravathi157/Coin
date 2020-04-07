
# coding: utf-8

# In[2]:


import random
import sys
def find(w,start,end):
    if(start==end):
        return(start)
    if(sum(w[start:(start+end)//2+1])!=0):
        return(find(w,start,(start+end)//2))
    return(find(w,(start+end)//2+1,end))
try:
    n=int(sys.argv[1])
    counterfeit=random.randint(0,n-1)
    weight=[0 * i for i in range(n)]
    weight[counterfeit]=1
    print("The counterfeit coin is",find(weight,0,n)+1)
except:
	print("invaild input")
	sys.exit()