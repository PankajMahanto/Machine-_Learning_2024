

import numpy as np

a=np.array([2,1,5,1,7,4,5,8,14,10,9,18,20,22])

import matplotlib.pyplot as plt
# If you're using Jupyter Notebook, you may also want to run the following
# line of code to display your code in the notebook:
# %matplotlib inline


# plt.plot(a)
# plt.show()


# x=np.linspace(0,2,20)
# y=np.linspace(0,10,20)
# plt.plot(x,y,'purple') #!line
# plt.plot(x,y,'o') # dots
# plt.show()

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
X=np.arange(-5,5,0.15)
Y=np.arange(-5,5,0.15)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2 + Y**2)
Z=np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cmap='viridis')
plt.show()