#!/usr/bin/env python
# coding: utf-8

# Data Types - int, float, str, list,

# data type - int

# In[1]:


int = 10


# In[7]:


int


# In[3]:


int = 10
int.as_integer_ratio()


# In[6]:


int.bit_count()


# In[8]:


int = 15
int.bit_count()


# In[9]:


int


# In[10]:


int.bit_length()


# In[11]:


int.to_bytes


# In[26]:


int.is_integer()


# data type = float

# In[18]:


float = 10.1


# In[19]:


float


# In[21]:


float.as_integer_ratio()


# In[22]:


float.conjugate()


# In[23]:


float.hex()


# In[24]:


float.is_integer()


# data type = str

# In[29]:


name = "tanmay"


# In[30]:


name.capitalize()


# In[31]:


name.casefold()


# In[38]:


name.count("tanmay")


# data type = list

# In[39]:


help('list')


# In[40]:


list = [ 1 , 2, 3 ,4 ]


# In[43]:


list.append(3)


# In[45]:


list.clear()


# In[46]:


list


# In[47]:


list = [ "tanmay" , 1 , 2 , 3.10]
list.copy()


# In[49]:


list.count(3)


# In[53]:


a = [ 1, 2, 3]
b = [ "pune" , 4 , 5 , 1.3]
list.extend(b)
print(list)


# In[54]:


list.pop()


# In[55]:


print(list)


# In[ ]:




