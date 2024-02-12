import fibonaccimodule

print()

try:
    print(fibonaccimodule.fibonacci(-1))
except IndexError as e:
    print(e)

try:
    print(fibonaccimodule.fibonacci("0"))
except TypeError as e:
    print(e)

triangle = fibonaccimodule.Triangle(3,4,5)
print(triangle.perimeter())
print(triangle.area())