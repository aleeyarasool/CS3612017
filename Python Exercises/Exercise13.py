
# coding: utf-8

# In[118]:


import re
email = []
with open("C:/Users/Aleeya/Documents/CS361PROG/emails.txt") as file:
    counter = 1
    while line:        
        reg = re.compile("([a-zA-Z0-9]*[@][a-zA-Z]*[.]['com'||'edu'||'co.uk'||'es']*)")
        for line in file:
            email += reg.findall(line)
            print(email)
            line = file.readline() 
            counter += 1           

