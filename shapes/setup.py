# This code was taken from http://docs.cython.org/src/userguide/wrapping_CPlusPlus.html and belongs to:
# Stefan Behnel, Robert Bradshaw, Dag Sverre Seljebotn, Greg Ewing, William Stein, Gabriel Gellner, et al.
# This code was edited and compiled by Christopher Thompson for clarity and succinctness.

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           "rect.pyx",                 # our Cython source
           sources=["Rectangle.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
))