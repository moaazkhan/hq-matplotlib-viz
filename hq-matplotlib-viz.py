#importing
import matplotlib.pyplot as plt
import numpy as np

################################################
#line chart rose-pine-default style

plt.style.use("rose-pine.mplstyle")

x_data = np.arange(0,20,0.02)
y_data = np.sin(x_data)
plt.plot(x_data, y_data)

plt.rcParams['figure.figsize'] = [6,7]
plt.rcParams['savefig.dpi'] = 600
plt.grid(False)
plt.show()

#to save in file remove # below
#plt.savefig('filename_1.png')

################################################
fig = plt.figure()
# Creating array from list 
x= np.random.randint(1,100,20)
y= np.random.randint(1,100,20)

# Numpy array as scatter plot
plt.scatter(x,y)

plt.rcParams['figure.figsize'] = [6,7]
plt.rcParams['savefig.dpi'] = 600
# Adding details to the plot
plt.title('Scatter')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(False)



################################################

plt.style.use("rose-pine-dawn.mplstyle")
plt.plot(x_data, y_data)

plt.rcParams['figure.figsize'] = [6,7]
plt.rcParams['savefig.dpi'] = 600
plt.grid(False)
plt.show()

################################################
fig = plt.figure()
# Creating array from list 
x= np.random.randint(1,100,20)
y= np.random.randint(1,100,20)

# Numpy array as scatter plot
plt.scatter(x,y)

plt.rcParams['figure.figsize'] = [6,7]
plt.rcParams['savefig.dpi'] = 600
# Adding details to the plot
plt.title('Scatter')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(False)
# Displaying the plot