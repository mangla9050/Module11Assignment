#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''Q1. Create a python program to sort the given list of tuples based on integer value using a  lambda function.  
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)] 
'''
l=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)] 
l.sort(key=lambda x:x[1])
print(l)


# In[7]:


'''Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using  lambda and map functions. 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
'''

l=[1,2,3,4,5,6,7,8,9,10]
list(map(lambda i:i**2,l))


# In[11]:


'''Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and  lambda functions 
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10') 
'''
l=[1,2,3,4,5,6,7,8,9,10]
print(tuple(map(lambda x:str(x),l)))


# In[15]:


'''Q4.  Write a python program using reduce function to compute the product of a list containing numbers  from 1 to 25. 
'''
from functools import reduce
l=list(range(1,26))
l
reduce(lambda x,y:x*y,l)


# In[17]:


'''Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the  filter function. 
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46] 
'''
l=[2,3,6,9,27,60,90,120,55,46]
list(filter(lambda x:x%2==0 and x%3==0,l))


# In[18]:


'''Q6. Write a python program to find palindromes in the given list of strings using lambda and filter  function. 
['python', 'php', 'aba', 'radar', 'level'] 
'''
l=['python','php','aba','radar','level']
list(filter(lambda x:x==x[::-1],l))


# In[ ]:




