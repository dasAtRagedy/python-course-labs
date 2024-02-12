import numpy as np
import numpy.matlib
import sympy as sp
import matplotlib.pyplot as plt

def uzd1(a: float = -1.3, b: float = 2.5, n: int = 64):
    ans = [a+(b-a)/n*e for e in range(n+1)]
    ans = list(zip(ans[:-1], ans[1:]))
    return ans
print(uzd1(), end='\n\n')

def uzd2(arr: list[int] = [1, 2, 3, 4], n: int = 4):
    return arr * n
print(uzd2(), end='\n\n')

def uzd3(num: int = 3, n: int = 4):
    return [num] * n
print(uzd3(), end='\n\n')

def uzd4(x: int = 10, y: int = 10):
    if x <= 2 or y <= 2:
        return [[1]*x]*y
    return (
        [[1]*x] + 
        [[1]+[0]*(x-2)+[1]]*(y-2) + 
        [[1]*x]
    )
[print(line) for line in uzd4()]
print()

def uzd5(n: int = 8):
    return [[(i+j)%2 for i in range(n)]
                     for j in range(n)]
[print(line) for line in uzd5()]
print()

def uzd6(n: int = 8):
    return [[i+j for i in range(n)]
                  for j in range(n)]
[print(line) for line in uzd6()]
print()

def uzd7(n: int = 5, col: int = 2):
    return sorted(np.random.rand(n, n).tolist(), key=lambda x: x[col-1])
[print(line) for line in uzd7()]
print()

def uzd8(matrix: np.matrix):
    return list(np.linalg.eig(matrix))
print(uzd8(np.matlib.mat([[4,2],[1,3]])), end='\n\n')

def uzd9():
    x = sp.symbols('x')
    return sp.diff((0.5*x**2 + 5*x + 4), x)
print(uzd9(), end='\n\n')

def uzd10():
    x = sp.symbols('x')
    return (
        sp.integrate(sp.exp(-x), x),
        sp.integrate(sp.exp(-x), (x, 0, 1))
    )
print(uzd10(), end='\n\n')

input()
def uzd11():
    # (np.cos(theta) + 1)
    theta = np.linspace(0, 2 * np.pi, 1000)
    plt.figure(figsize=(6, 6))
    my_plot = plt.subplot(111, polar=True)
    my_plot.plot(theta, np.cos(theta)+1)
    plt.show()
    # i don't know what the f am I looking at.
    pass
uzd11()

def uzd12():
    nums = np.random.normal(0, np.sqrt(1), 1000)
    plt.hist(nums, bins=70)
    plt.show()
uzd12()