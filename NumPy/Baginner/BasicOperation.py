import numpy as np

# Basic Operations

# Addition
a=np.array([20,30,40,50,60])
b=np.arange(5) # auto set b=0,1,2,3,4
b=np.array([2,4,5,6,7])

print(b)
c=a-b**2
print(c)


# Multiplication 
mul=a*b
print(mul)

# Division 
div=a/b
print(div)

# Matrix Multiplication
A=np.array([[1,1],
            [0,1]])
B=np.array([[2,0],
            [3,4]])

matMul=A@B
print(matMul)

# Another matrix Product operation
dotMul=A.dot(B)
print(dotMul)

