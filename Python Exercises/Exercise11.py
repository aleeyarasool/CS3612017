
# coding: utf-8

# In[4]:


#iterative method
def iteration(x):
    i= 1;
    element =x[0]
    if len(x)==0:
        return 0
    
    while i < len(x):
        element = element * x[i];
        i= i+1;
    return element
        
print(iteration([1,2,3,4]))        


# In[18]:


#recursive method
def recursion(x):
    if len(x)==1:
        return x[0]
    return recursion([x[0]]) * recursion(x[1:])
print(recursion([1,2,3,4]))    

