#Here we are going to learn sth about numpy


#%% Import numpy package
import numpy as np

#%% create an array from a list
Array_11 = np.array([1,2,3,4,5])
Array_12 = np.array([3.14, 4, 2, 3])
Array_13 = np.array([1, 2, 3, 4], dtype='float32')

#%% create an array from Scratch
Array_21 = np.zeros(10, dtype=int)
Array_22 = np.ones((3, 5), dtype=float)
Array_23 = np.arange(0, 20, 2)
Array_24 = np.random.normal(0, 1, (3, 3))



#%% data type , note
# NumPy Array Attributes

np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array 
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array 
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print("x3 ndim: ", x3.ndim) 
print("x3 shape:", x3.shape) 
print("x3 size: ", x3.size)


#%% array indexing and slicing

# Multidimensional subarrays


#%%Subarrays as no-copy views
print(x2)
x2_sub = x2[:2, :2] 

print(x2_sub)

x2_sub[0, 0] = 99 
print(x2_sub)

print(x2)

# get a copy from x2
x2_sub_copy = x2[:2, :2].copy()

#%%reshape
#x.reshape

#%% Concatenation of arrays
x = np.array([1, 2, 3]) 
y = np.array([3, 2, 1]) 
np.concatenate([x, y])

z = [99, 99, 99] 
print(np.concatenate([x, y, z]))


#2 dimensional
grid = np.array([[1, 2, 3], [4, 5, 6]])

np.concatenate([grid, grid])
np.concatenate([grid, grid],axis=1)

#mixed dimensions
x = np.array([1, 2, 3]) 
grid = np.array([[9, 8, 7], [6, 5, 4]])
np.vstack([x, grid])

y = np.array([[99], [99]])
np.hstack([grid, y])

#%% splitting of arrays
#np.split, np.hsplit, and np.vsplit.
x = [1, 2, 3, 99, 99, 3, 2, 1] 
x1, x2, x3 = np.split(x, [3, 5]) 
print(x1, x2, x3)






















