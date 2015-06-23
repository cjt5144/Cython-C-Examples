## Shapes Cython-C++ Examples
Simple examples for Cython C++ API

### Compilation
To compile code, change directory to folder containing setup.py and type the following at command prompt:
```
python setup.py build_ext --inplace
```

### Example
```
import rect
myRect = rect.PyRectangle(1,2,3,4)
myRect.getArea()
```

### Known Caveats (Subject to Change)

C++ functions external to any class **must** be included in separate .pyx file and wrapped in a pure Python function.
