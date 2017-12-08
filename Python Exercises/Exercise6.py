
# coding: utf-8

# In[11]:


#6a
def is_prime(n):
    if(n == 1):
        return False
    else:
        for i in range(2,n):
            if(n%i == 0):
                return False
        return True
print(is_prime(6))


# In[ ]:


#6b
def is_prime(n):
    plus = 6n+1;
    minus = 6n-1;
    if(n == 1):
        return False
    else:
        for i in range(2,n):
            if(n%i == 0):
                return False
        return True
    for i in range(3,n):
        if()
print(is_prime(6))


# In[ ]:


#6c
def is_prime(n):
    i=5;
    w=2;
    while i*i <= n:
        if(n%i == 0):
                return False
        i= i+w
        w=5-w
    return True    
is_prime(13)                          


# In[ ]:


#6d print the first n primes
def prime(n):
    n=5;
    count=2;
    i=4;
    
    while count <= n:
        for j in range (2,i):
            if(i%j == 0):           
                break
        if(j==i-1):
            print(i)
            count = count +1
        i = i+1
prime(5)

