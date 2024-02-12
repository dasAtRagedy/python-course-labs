from setuptools import setup, Extension

module = Extension("fibonaccimodule", sources=["fibonaccimodule.c"])

setup(name="FibonacciModule", 
      version="1.0", 
      description="Python interface for the Fibonacci function written in C.",
      ext_modules=[module]
)

# python ./setup.py build_ext --inplace