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
    