# distutils: language = c++
# distutils: sources = Rectangle.cpp

# Above lines link the Rectangle.o necessary to 'import rect'

"""
This code was taken from http://docs.cython.org/src/userguide/wrapping_CPlusPlus.html and belongs to:
Stefan Behnel, Robert Bradshaw, Dag Sverre Seljebotn, Greg Ewing, William Stein, Gabriel Gellner, et al.
This code was edited and compiled by Christopher Thompson for clarity.
"""

cdef extern from "Rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getLength()
        int getHeight()
        int getArea()
        void move(int, int)