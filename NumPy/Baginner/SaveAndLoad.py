import numpy as np

# Sava the file here 
a=np.array([1,2,3,4,5,6])
np.save('array_save',a)

# Load the file here
b=np.load('array_save.npy')
print(a)

# Save as a .csv file extension 
cs=np.array([1,2,3,4,5,6])
np.savetxt('arr.csv',cs)

csp=np.loadtxt('arr.csv')
print(csp)


# Best way read and write file using Pandas

import pandas as pd
# If all of your columns are same type 
# x=pd.read_csv('filename.csv',header=0).values

# You can also simply select the columns you need 
# x=pd.read_csv('filename.csv',usecols=['A','B']).values






# Taking input using the numpy and then create a pandas DataFrame and print the data using pandas

a=np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

print(a)

# Create a dataframe and use it 
df=pd.DataFrame(a)
print(df)

# Easily save dataframe
df.to_csv('pd.csv')

# Read this dataframe
data=pd.read_csv('pd.csv')






