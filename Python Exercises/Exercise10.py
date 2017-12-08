
# coding: utf-8

# In[47]:


get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plot
import numpy as np
x = np.linspace(0,2)
s= np.sin(x-2) #sin(x-2)
eneg = -x*np.exp(2) # -x^2
e= np.exp(eneg) #e^x

# compose plot
plot.plot(x,s*e) # sin(x)/x
plot.xlim( xmin=0, xmax=2 )
plot.title('F(x)=$sin^2$(x-2)$e^{-x^2}$') 
plot.xlabel('X-axis')
plot.ylabel('Y-axis')
plot.show() 

