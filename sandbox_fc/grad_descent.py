import numpy as np
import types

class Function:
    """
    Define the result of a function, giving a value for a specific state vector
    :param formula: A callable lambda function that takes one or multiple variables
    """

    def __init__(self, formula:types.FunctionType):
        self.formula = formula
        self.order = formula.__code__.co_argcount
        print(f"Function of order {self.order} initialized.")
        assert(isinstance(self.formula(*np.ones(self.order)), (int,float,complex))) #Check if function accepts numeric inputs and produces numeric output
        assert(isinstance(self.formula(*np.zeros(self.order)), (int,float,complex))) 

    def evaluate(self, *vector) -> np.number:
        """
        Applies the formula to the given vector (for x, y, z, etc.).

        :param vector: A sequence of inputs the value of a variable or different variables
        :return: A value with the formula applied to the array
        """
        #assert(type(vector) == np.array)
        if len(vector) < self.order:
            print("Warning: Number of arguments provided lower than order of function.")
            return np.nan
        if len(vector) > self.order:
            print("Warning: Number of arguments provided greater than order of function.")
            return np.nan

        return self.formula(*vector)

    def gradient(self, *vector, delta:float) -> np.array:
        if len(vector) < self.order:
            print("Warning: Number of arguments provided lower than order of function.")
            return np.nan
        if len(vector) > self.order:
            print("Warning: Number of arguments provided greater than order of function.")
            return np.nan
        
        v = np.array(vector, float)
        dy = np.array(v)

        y0 = self.evaluate(*v)
        for i in range(v.size):
            delta_i = delta*np.array([i==j for j in range(v.size)])
            dy[i] = (self.evaluate(*(v+delta_i)) - y0)/delta
        return dy, y0

class OptAlgorithm:
    """
    Generic class for an optimization algorithm to apply to a given function
    """
    def __init__(self):
        pass

    def step(self, function:Function, *x0):
        print("Define step function for the corresponding algorithm")
        return np.array(0)

class GradientDescent:
    """
    Optimization algorithm of the form x1 = x0 - a*dy/dX, where a is the step size
    and dy/dX is the approximation of the gradient at x0
    """
    def step(self, function:Function, *x_i, stepsize, deltagradient) -> np.array:
        grad, y_a = function.gradient(*x_i, delta=deltagradient)
        x_a = np.array(x_i, float)
        x_b = x_a - grad*stepsize
        return x_b, y_a ##Return y_a to prevent evaluating several times at same point

class Optimizer:
    """
    Generic class for any optimization algorithm for a given Function object and optimization method.
    """
    def __init__(self, function:Function, algorithm:OptAlgorithm):
        self.function = function
        self.method = algorithm

    def solve(self, *x0, tol=1e-8, stepsize=1e-4, deltagradient=1e-8) -> np.ndarray:
        x_i_1 = np.array(x0,float)
        x_i, y_i_1 = self.method.step(self.function, *x_i_1, stepsize=stepsize, deltagradient=deltagradient)
        y_i = self.function.evaluate(*x_i)

        xsol = [[*x_i_1], [*x_i]]
        ysol = [y_i_1, y_i]

        while np.linalg.norm(x_i - x_i_1,2) > tol:
#            print(f"This is the value of x_i {x_i}")
            x_i_1 = x_i #Jump to next step

            x_i, y_i_1 = self.method.step(self.function, *x_i_1, stepsize=stepsize, deltagradient=deltagradient)
            y_i = self.function.evaluate(*x_i)

            xsol.append([*x_i])
            ysol.append(y_i)

        return np.array(ysol), np.array(xsol)


### INLINE TEST OF FUNCTION CLASS
my_function = Function(lambda x, y, z: x**2 + y**2 + 2*x*z + z**2)
my_function.evaluate(2,3,4,5)
my_function.evaluate(2,3)

print(my_function.evaluate(2,3,4))
print(my_function.gradient(2,3,4, delta=1e-8))

### INLINE TEST OF ALGORITHM AND OPTIMIZER
my_algorithm = GradientDescent()
opt = Optimizer(my_function, my_algorithm)

my_ysol, my_xsol = opt.solve(2,3,4)

import matplotlib.pyplot as plt
plt.plot(my_ysol)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1,3)
ax.set_ylim(-1,3)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("function value")

plt.plot(my_xsol[:,0],my_xsol[:,1],my_ysol[:]) #Projection in xy plane of solution points and 

plt.show()
print(my_xsol[-1,:])
print(my_ysol[-1])

# Function is nonconvex with local minima at [0,0,0] and [-1,0,1]