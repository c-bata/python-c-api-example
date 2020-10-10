from setuptools import setup, Extension
from Cython.Build import cythonize
from mypyc.build import mypycify

# Cython
ext_modules = cythonize([
    Extension('cyfibonacci', ['cyfibonacci.pyx']),
], gdb_debug=True)

# mypyc
ext_modules += mypycify(['myfibonacci.py'])

# C extension
ext_modules.append(
    Extension('fibonacci', ['fibonacci.c'],
              extra_compile_args=["-g", "-O0"],
              extra_link_args=["-g"])
)

setup(
    name='fibonacci',
    ext_modules=ext_modules,
)
