## Shapes Cython-C++ Examples
Simple examples for Cython C++ API

### Compilation
To compile code, type the following at command prompt:
```
python setup.py build_ext --inplace
```

### Example
```
import rect
myRect = rect.PyRectangle(1,2,3,4)
myRect.getArea()
```