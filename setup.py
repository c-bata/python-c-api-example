from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='fibonacci',
    ext_modules=cythonize([
        Extension('cyfibonacci', ['cyfibonacci.pyx'],
                  extra_compile_args=["-g"],
                  extra_link_args=["-g"]),
        Extension('fibonacci', ['fibonacci.c']),
    ], gdb_debug=True)
)
