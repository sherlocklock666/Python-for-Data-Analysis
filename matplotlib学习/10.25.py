#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import matplotlib as mpl
mpl.use('qt4agg')
import matplotlib.pyplot as plt
import numpy as np
import sympy


# In[2]:


x = np.linspace(-5, 2, 100)
y1 = x**3 + 5*x**2 + 10
y2 = 3*x**2 + 10*x
y3 = 6*x + 10


# In[3]:


fig, ax = plt.subplots()
ax.plot(x, y1, color='blue', label='y(x)')
ax.plot(x, y2, color='red', label="y'(x)")
ax.plot(x, y3, color='green', label='y"(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()


# In[10]:


fig = plt.figure(figsize=(8,2.5),facecolor="#FF4500")
ax = fig.add_axes((0.1,0.1,0.8,0.8), facecolor="#90EE90")
x = np.linspace(-2, 2, 1000)
y1 = np.cos(40*x)
y2 = np.exp(-x**2)
ax.plot(x, y1*y2)
ax.plot(x, y2, 'b')
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.suptitle("10.25.22:43 drawing")
fig.savefig("graph.png", dpi=100, facecolor="#f1f1f1",transparent=True)

