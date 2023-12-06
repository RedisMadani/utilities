# Linear Equation Solver and 3D Plotter

![screenshot2](https://github.com/RedisMadani/Solver-linear-equations/assets/136177376/52a8a792-23fb-413c-bc94-86b70ee284a3)

This script solves a system of three linear equations and plots the solution in a 3D graph.

## Usage

1. Run the script using Python.
2. Enter the coefficients for each equation when prompted. Each value should be separated by a space.
   - For example, to enter the equation `6x + 5y - 3z = 4`, you would input: `6 5 -3 4`.
3. The script will solve the system of equations and display the solution.
4. A 3D graph will be generated showing the intersection of the three planes represented by the equations. The solution point will be marked with a black marker.

## Prerequisites

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone or download this repository.
2. Install the required dependencies using pip:

```shell
pip install numpy matplotlib
```

## Example

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Prompt user to enter coefficients for each equation
print('The 3 equations are entered individually, each value of the equation is entered separated by a space, for example:')
print('input = 6 5 -3 4')
print('This will be equal to 6x + 5y - 3z = 4')

print('Enter values for equation 1: ')
a, b, c, d = map(float, input().split()) 

print('Enter values for equation 2: ')
e, f, g, h = map(float, input().split())

print('Enter values for equation 3: ')
i, j, k, l = map(float, input().split())

# Solve the linear equation
A = np.array([[a,b,c],[e,f,g],[i,j,k]])
b_a = np.array([d,h,l])
sol = np.linalg.solve(A,b_a)
print(sol)

# Generate data for 3D plot
x,y = np.linspace(0,10,10), np.linspace(0,10,10)
X,Y = np.meshgrid(x,y)

Z1 = (d-a*X-b*Y)/c
Z2 =(h-e*X-f*Y)/g
Z3 =(l+X-Y)/k

# Create 3D graphics
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z1,alpha=0.5,cmap=cm.Accent,rstride=100,cstride=100)
ax.plot_surface(X,Y,Z2,alpha=0.5,cmap=cm.Paired,rstride=100,cstride=100)
ax.plot_surface(X,Y,Z3,alpha=0.5,cmap=cm.Pastel1,rstride=100,cstride=100)
ax.plot((sol[0],),(sol[1],),(sol[2],),lw=2,c='k', marker='o', markersize=7, markeredgecolor='g', markerfacecolor='white')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
```

## License

This project is licensed under the [MIT License](LICENSE).
