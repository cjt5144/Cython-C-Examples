// This code was taken from http://docs.cython.org/src/userguide/wrapping_CPlusPlus.html and belongs to:
// Stefan Behnel, Robert Bradshaw, Dag Sverre Seljebotn, Greg Ewing, William Stein, Gabriel Gellner, et al.
// This code was edited and compiled by Christopher Thompson for clarity and succinctness.

namespace shapes {
    class Rectangle {
    public:
        int x0, y0, x1, y1;
        Rectangle(int x0, int y0, int x1, int y1);
        ~Rectangle();
        int getLength();
        int getHeight();
        int getArea();
        void move(int dx, int dy);
    };
}