# Defining class

class Rectangle:
    # First param is the instance of the object itself. You can call it anything, but the convention is to call self
    def __init__(self, width, height):
        self.width = width
        self._height = height

    @property
    def width(self):
        print('Setting width property')
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width cannot be less than or equal to zero')
        else:
            self._width = width

    @property
    def height(self):
        print('Setting height property')
        return self._height


    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError ('Height should be greater than zero')
        else:
            self_height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r = Rectangle(5,6)
r1 = Rectangle(5,6)
print('Width:{0}'.format(r.width))
print('Height:{0}'.format(r.height))
print ('Area:{0}'.format(r.area()))
print ('To String:{0}'.format(str(r)))
print ('Equal method:{0}'.format(r == r1))
print ('Obect itself is different:{0}'.format(r is not r1))

r2 = 200

print ('Equal method:{0}'.format(r == r2))

r3 = Rectangle(3,2)

print('Check less than method:{0}'.format(r3<r1))


r4 = Rectangle(-100, 10)
r4.width = 10
r4.height = -20
print (str(r4))



