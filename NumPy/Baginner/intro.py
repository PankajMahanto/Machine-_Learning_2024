import numpy as np

a=np.array([[1,2,3],
            [4,5,6]])
# Dimention of the Array
print(a.ndim)

# Size of the Array = Total number of element of the array
print(a.size)

# Find type of the number
print("type: ",a.dtype)

print("Itemsize: ",a.itemsize)

# Dimension of the Array is n x m
print(a.shape)

# Find the row of the Array 
print(a.shape[0])

# Find the Column of the Array 
print(a.shape[1])

# Zeros Function 
b=np.zeros((3,4))
print(b)

# Ones Function 
b=np.ones((3,4))
print(b)


# Empty Array 
em=np.empty((2,3))
print(em)

# arange function 
# rg=np.arange(10,30,5)
rg=np.arange(0,2,0.3)
print(rg)


from numpy import pi
line=np.linspace(0,2,9)
print(line)

x=np.linspace(0,2*pi,100)
print(x)
f=np.sin(x)
print(f)






