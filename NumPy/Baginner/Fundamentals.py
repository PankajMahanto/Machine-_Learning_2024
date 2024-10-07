import numpy as np
# Array Fundamentals 
a=np.array([1,2,3,4,5,6])
print(a[0])


# 2 D array 
b=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]])
print("element: ",b[1,3])


# Adding,Removing and Sorting Elements

arr=np.array([2,1,5,7,3,4,8,6])
print(arr)
print("sort:",np.sort(arr))
print("\n\n")
print("argsort:",np.argsort(arr))
print("lexsort:",np.lexsort(arr))
# print("searchsorted:",np.searchsorted(arr))
# print("partitionsort:",np.partition(arr))

print("Max:",arr.max())
print("Min:",arr.min())
print("sum:",arr.sum())


# How to get unique items and counts

arr=np.array([11,11,12,13,14,11,15,16,17,12,13,11,14,18,19,20])

unique_values,occurences_counts=np.unique(arr,return_counts=True)
print(unique_values)
print(occurences_counts)
print("Total element:",occurences_counts.sum())
