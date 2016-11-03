# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
    def area(self):
        return 0.5*self.base * self.height
    def __str__(self):
        return "Triangle with base " + str(self.base) + " and height " + str(self.height)
    def __eq__(self, other):
        return type(other) == Triangle and self.base == other.base and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.shapeSet = []
        self.index = -1
        
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh not in self.shapeSet:
            self.shapeSet.append(sh)
            return True
        else:
            return False
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        return self
    def next(self):
        self.index += 1
        #print self.index
        #print len(self.shapeSet)
        if self.index > (len(self.shapeSet)-1):
            raise StopIteration
        return self.shapeSet[self.index]
    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        mystring = ''
        for shape in self.shapeSet:
            mystring += (str(shape) + '\n')
        return mystring

##circle = Circle(2.0)
##print circle.area()
##print circle
##square1 = Square(4.0)
##square2 = Square(1.0)
##triangle = Triangle(1.0, 1.0)
##print triangle.area()
##print triangle
##shapeset = ShapeSet()
##shapeset.addShape(circle)
##shapeset.addShape(square1)
##shapeset.addShape(square2)
##shapeset.addShape(triangle)
##print shapeset
##for shape in shapeset:
##    print shape
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    largestArea = 0
    largestShapeList = []
    for shape in shapes:
        if largestArea < shape.area():
            largestArea = shape.area()
            largestShapeList = [shape,]
        elif largestArea == shape.area():
            largestShapeList.append(shape)
    largestShapeTuple = tuple(largestShapeList)
    return largestShapeTuple

##ss = ShapeSet()
##ss.addShape(Triangle(3,8))
##ss.addShape(Circle(1))
##ss.addShape(Triangle(4,6))
##largest = findLargest(ss)
##for shape in largest:
##    print shape

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    inFile = open("shapes.txt", 'r')
    shapeList = []
    for line in inFile:
        shapeList.append(line.strip().lower())
    #print shapeList
    shapeList2 = []
    for shape in shapeList:
        shapeList2.append(shape.split(','))
    #print shapeList2
    ss = ShapeSet()
    for shape in shapeList2:
        if shape[0] == 'circle':
            ss.addShape(Circle(float(shape[1])))
        elif shape[0] == 'square':
            ss.addShape(Square(float(shape[1])))
        elif shape[0] == 'triangle':
            ss.addShape(Triangle(float(shape[1]), float(shape[2])))
        else:
            print "Unknown shapes!"
    return ss

ss = readShapesFromFile("shapes.txt")
print ss
