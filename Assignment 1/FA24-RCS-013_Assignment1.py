#!/usr/bin/env python
# coding: utf-8

# # REGISTRATION NUMBER :  FA24-RCS-013

# # Task 1

# ### 1.1. Create a list: nums = [3, 5, 7, 8, 12], make another list named ‘cubes’ and append the cubes of the given list ‘nums’ in this list and print it.

# In[1]:


nums = [3, 5, 7, 8, 12]


# In[2]:


cubes = []


# In[3]:


for a in nums:
    cubes.append(a ** 3)


# In[4]:


print("Cubes of nums:", cubes)


# ### 1.2. Create an empty dictionary: dict = {}, add the following data to the dictionary: ‘parrot’: 2, ‘goat’: 4, ‘spider’: 8, ‘crab’: 10 as key value pairs.

# In[5]:


dict = {}


# In[6]:


dict['parrot'] = 2
dict['goat'] = 4
dict['spider'] = 8
dict['crab'] = 10


# ### 1.3. Use the ‘items’ method to loop over the dictionary (dict) and print the animals and their corresponding legs. Sum the legs of each animal, and print the total at the end.

# In[7]:


corresponding_legs = 0


# In[8]:


for animal, legs in dict.items():
    print("%s has %d legs" % (animal, legs))
    corresponding_legs += legs


# In[9]:


print("Total legs of all animals=", corresponding_legs)


# ### 1.4. Create a tuple: A = (3, 9, 4, [5, 6]), change the value in the list from ‘5’ to ‘8’.

# In[10]:


A = (3, 9, 4, [5, 6])


# In[11]:


A[3][0] = 8


# In[12]:


print("tuple A =", A)


# ### 1.5. Delete the tuple A

# In[13]:


del A


# ### 1.6. Create another tuple: B = (‘a’, ‘p’, ‘p’, ‘l’, ‘e’), print the number of occurrences of ‘p’ in the tuple.

# In[14]:


B = ('a', 'p', 'p', 'l', 'e')


# In[15]:


counter = B.count('p')


# In[16]:


print("number of p are=", counter)


# ### 1.7. Print the index of ‘l’ in the tuple.

# In[17]:


index_of_l = B.index('l')


# In[18]:


print("index of l is =", index_of_l)


# # Task 2

# In[19]:


import numpy as np


# ### 2.1 Convert matrix A into numpy array

# In[20]:


A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])


# ### 2.2 Use slicing to pull out the subarray consisting of the first 2 rows and columns 1 and 2. Store it in b which is a numpy array of shape (2, 2).

# In[21]:


Slice = A[:2, :2] 


# In[22]:


print(Slice)


# #### 2.3 Create an empty matrix ‘C’ with the same shape as ‘A’.

# In[23]:


C = np.empty_like(A)


# In[24]:


print(C)


# ### 2.4 Add the vector z to each column of the matrix ‘A’ with an explicit loop and store it in ‘C’.

# In[25]:


z = np.array([1, 0, 1])


# In[26]:


for i in range(A.shape[1]):
    C[:, i] = A[:, i] + z


# In[27]:


print(C)


# ### Create the following:
# #### X = np.array([[1,2],[3,4]])
# #### Y = np.array([[5,6],[7,8]])
# #### v = np.array([9,10])
# 

# In[28]:


X = np.array([[1, 2], [3, 4]])


# In[29]:


Y = np.array([[5, 6], [7, 8]])


# In[30]:


v = np.array([9, 10])


# ### 2.5 Add and print the matrices X and Y.

# In[31]:


addition = X + Y


# In[32]:


print(addition)


# ### 2.6 Multiply and print the matrices X and Y.

# In[33]:


multiply = np.dot(X, Y)


# In[34]:


print(multiply)


# ### 2.7 Compute and print the element wise square root of matrix Y.

# In[35]:


sq_root = np.sqrt(Y)


# In[36]:


print(sq_root)


# ### 2.8 Compute and print the dot product of the matrix X and vector v.

# In[37]:


result = np.dot(X, v)


# In[38]:


print(result)


# ### 2.9 Compute and print the sum of each column of X.

# In[39]:


sum = np.sum(X, axis=0)


# In[40]:


print(sum)


# # task 3

# ### 3.1 Create a function ‘Compute’ that takes two arguments, distance and time, and use it to calculate velocity.

# In[41]:


def Compute(d, t):
    if t == 0:
        return "Time cannot be zero"
    v = d / t
    return v


# In[42]:


d = 34


# In[43]:


t = 10  


# In[44]:


v = Compute(d, t)


# In[45]:


print(f"Velocity is: {v} m/s")


# ### 3.2 Make a list named ‘even_num’ that contains all even numbers up till 12. Create a function ‘mult’ that takes the list ‘even_num’ as an argument and calculates the products of all entries using a for loop.

# In[46]:


even_num = [2, 4, 6, 8, 10, 12]


# In[47]:


def mult(even_num):
    product = 1  
    for i in even_num:
        product *= i
    return product


# In[48]:


entries = mult(even_num)


# In[49]:


print(entries)


# # task 4

# In[50]:


import pandas as pd


# In[51]:


data_frame_data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}


# In[52]:


data_frame = pd.DataFrame(data_frame_data)


# ### 4.1 Print only the first two rows of the dataframe.

# In[53]:


print(data_frame.head(2))


# ### 4.2 Print the second column.

# In[54]:


print(data_frame['C2'])


# ### 4.3 Change the name of the third column from ‘C3’ to ‘B3’.

# In[55]:


data_frame.rename(columns={'C3': 'B3'}, inplace=True)


# In[56]:


print(data_frame)


# ### 4.4 Add a new column to the dataframe and name it ‘Sum’.

# In[57]:


data_frame['Sum'] = 0


# ### 4.5 Sum the entries of each row and add the result in the column ‘Sum’.

# In[58]:


data_frame['Sum'] = data_frame.sum(axis=1)


# In[59]:


print(data_frame)


# ### 4.6 Read CSV file named ‘hello_sample.csv’ (the file is available in the class Google Drive shared folder) into a Pandas dataframe.

# In[60]:


file = 'hello_sample.csv'


# In[61]:


df = pd.read_csv(file)


# ### 4.7 Print complete dataframe.

# In[62]:


print(df)


# ### 4.8 Print only bottom 2 records of the dataframe.

# In[63]:


print(df.tail(2))


# ### 4.9 Print information about the dataframe.

# In[64]:


print(df.info())


# ### 4.10 Print shape (rows x columns) of the dataframe.

# In[65]:


print(df.shape)


# ### 4.11 Sort the data of the dataFrame using column ‘Weight’.

# In[66]:


df_sorted = df.sort_values(by='Weight')


# In[67]:


print(df_sorted)


# ### 4.12 Use isnull() and dropna() methods of the Pandas dataframe and see if they produce any change

# In[68]:


print(df.isnull())


# In[69]:


print(df.dropna())

