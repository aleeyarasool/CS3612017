
# coding: utf-8

# In[12]:


a =[1,2,3,4,5,6]
b=a
b[1]=9
c=a[:]
c
c[2] = 13
a


# In[26]:


def set_first_elem_to_zero(l):
    l[0]=0

def main():
    l = [3,4,5,7]
    set_first_elem_to_zero(l)
    print(l)
    
if __name__== "__main__":
      main()   

