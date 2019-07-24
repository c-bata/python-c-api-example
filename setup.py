from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='fibonacci',
    ext_modules=cythonize([
        Extension('cyfibonacci', ['cyfibonacci.pyx']),
        Extension('fibonacci', ['fibonacci.c'],
                  extra_compile_args=["-g", "-O0"],
                  extra_link_args=["-g"]),
    ], gdb_debug=True)
)
