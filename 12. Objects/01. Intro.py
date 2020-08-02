"""
06.01.2019 16:51
Introduction to objects
Bogdan Prădatu
"""


class Point:
    """ Point class represents and manipulates x,y coordiantes. """
    # __init__ is invoked everytime an object will be created
    def __init__(self, x=0, y=0):  # self could be any other word
        """ Creates a new point at x,y coordinates """
        self.x = x
        self.y = y

    def __str__(self):      # initially named coord, but it seems that
                            # if the method is called __str__,
                            # Python knows what's up. It will override the
                            # default behaviour of the built-in str function.
        """ output point coordinates as string in tuple format: (x,y) """
        return f"{(self.x, self.y)}"

    def __add__(self, other):  # this will override the behaviour of "+" operator
        """ Return new point with my and some other points coordinates summed"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # this will override the behaviour of "+" operator
        """ Return new point with my and some other points coordinates subtracted"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def same_coordinates(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def distance(self, target=None):
        """ Computes distance betwen me and target
            if no target is given, compute from origin"""
        if target is None:
            return ((self.x**2)+(self.y**2))**0.5
        else:
            return (((self.x-target.x)**2)+((self.y-target.y)**2))**0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def mirror(self, y=False):
        """ Return a point mirrored about the X axis
            or Y, if y = True """
        if y is False:
            return Point(self.x, -self.y)
        else:
            return Point(-self.x, self.y)

    def slope(self, target=None):
        """ Returns the slope between me and a target point """
        if target is None:
            dx = self.x
            dy = self.y
        else:
            dx = target.x - self.x
            dy = target.y - self.y
        if dx == 0:
            # print("Vertical line. Cannot calculate slope.")
            return None
        else:
            slope = dy/dx
        return slope

    def line(self, other):
        """ Return the equation of a line that connects me and other point
            y = mx + c. Output tuple of (m,c).
        """
        m = self.slope(other)
        if m is None:
            return None, None
        else:
            c = -m*self.x+self.y
        return m, c

    def intersection(self, other1, other2, other3):
        """ Return intersection point of lines myself-other1
            and other2-other3
        """
        m1, c1 = self.line(other1)
        m2, c2 = other2.line(other3)
        x = (-c1+c2)/(m1-m2)
        y = m1*x + c1
        return Point(x, y)

    def perpendicular(self, other1, other2, other3):
        """ Determine if the two lines created by myself-other1
            and other2-other3 are perpendicular
        """
        m1, c1 = self.line(other1)
        m2, c2 = other2.line(other3)
        if m1 is None and m2 == 0 or m1 == 0 and m2 is None:
            return True
        elif m1 == (-1/m2):
            return True
        return False

    def collinear(self, point1, point2, *args):
        """ Check if three or more points are colinear with this point """
        items = [self, point1, point2]
        slope = []
        for arg in args:
            items.append(arg)
        for i in range(len(items)-1):
            slope.append(items[0].slope(items[i+1]))
        for s in range(len(slope)):
            if slope[0] != slope[s]:
                return False
        return True

    def concyclic(self, p1, p2, *args):
        """ Check if three or more points are concyclic
            and return Circle if True, or False
        """
        bisector1 = Line()
        bisector2 = Line()
        bisector3 = Line()
        bisector1.line(self, p1)
        bisector2.line(self, p2)
        bisector3.line(p1, p2)
        midpoint1 = self.halfway(p1)
        midpoint2 = self.halfway(p2)
        midpoint3 = p1.halfway(p2)
        perp1 = bisector1.getPerpendicular(midpoint1)
        perp2 = bisector2.getPerpendicular(midpoint2)
        perp3 = bisector3.getPerpendicular(midpoint3)
        i1 = perp1.intersection(perp2)
        i2 = perp1.intersection(perp3)
        i3 = perp2.intersection(perp3)
        radius_square = (((self.x - i1.x)**2)+((self.y - i1.y)**2))
        radius = (((self.x - i1.x)**2)+((self.y - i1.y)**2))**0.5
        count = 0
        for arg in args:
            if abs((arg.x - i1.x)**2+(arg.y - i2.y)**2) - radius_square < 1e-10:
                count += 1
        if (i1.same_coordinates(i2) and
            i1.same_coordinates(i3) and
            i2.same_coordinates(i3) and
           count == len(args)):
            return Circle(i1.x, i1.y, radius)
        return False


class Line:
    """ y = mx + c """
    def __init__(self, m=0, c=0, x=None):
        """ Create line object
            x - in case of vertical line, the equation is x = constant
        """
        if x is None:
            self.m = m
            self.c = c
            self.x = x
        else:
            self.m = None
            self.c = None
            self.x = x

    def __str__(self):
        if self.x is None:
            return f"y = {self.m}*x + {self.c}"
        else:
            return f"Vertical Line. x = {self.x}"

    def __eq__(self, other):
        if self.m == other.m and self.c == other.c:
            return True
        return False

    def line(self, point1, point2):
        """ Use two Point objects to create a line
            Return (m,c) from line equation y = mx + c"""
        dx = (point2.x - point1.x)
        dy = (point2.y - point1.y)
        if dx == 0:
            self.m = None
            self.c = None
            self.x = point1.x
            return self.m, self.c, self.x
        else:
            self.m = dy/dx
        if self.m is None:
            return None, None
        else:
            self.c = -self.m * point1.x + point1.y
            # self.c = -m*point2.x+point2.y
        return self.m, self.c

    def segment(self, point1, point2):
        """ Use two given points to create a line
            and return the length of the segment between the points
        """
        self.line(point1, point2)
        length = point1.distance(point2)
        return length        

    def point(self, x=None, y=None):
        """ Given either x or y coordinates, return a point object
            that sits on this line.
        """
        if self.m is None and x is not None:
            if x == self.x:
                from random import randrange
                x = x
                y = randrange(0, 99999999)
                return Point(x, y)
            else:
                return "Given x coordinate not on line"
        elif self.m is None and x is None:
            from random import randrange
            x = self.x
            y = randrange(0, 99999999)
        elif x is not None and y is None:
            y = self.m * x + self.c
        elif x is None and y is not None:
            x = (y-self.c)/self.m
        return Point(x, y)

    def intersection(self, other):
        """ Return intersection point of this and other line """
        if self.m is None:
            x = self.x
            y = other.m*x + other.c
        elif other.m is None:
            x = other.x
            y = self.m*x + self.c
        else:
            x = (-self.c+other.c)/(self.m-other.m)
            y = self.m*x + self.c
            # y = other.m*x + other.c
        return Point(x, y)

    def isPerpendicular(self, other):
        """ Return True if other line is perpendicular on this line"""
        if self.m is None and other.m == 0 or self.m == 0 and other.m is None:
            return True
        elif self.m * other.m == -1:
            return True
        return False

    def getPerpendicular(self, point):
        """ Return (m,c) coefficients of the line equation (y = mx +c)
            for a perpendicular line that passes through a given point
        """
        perp_line = Line()
        if self.m is None:
            perp_line.m = 0
        elif self.m != 0:
            perp_line.m = -1/self.m
        else:
            perp_line.m = None
            perp_line.c = None
            self.x = point.x
            return Line(perp_line.m, perp_line.c, self.x)
        perp_line.c = point.y - point.x*perp_line.m
        return Line(perp_line.m, perp_line.c)

    def parallel(self, other):
        """ Return True if other line is parallel to this line """
        if self.m == other.m:
            return True
        else:
            return False

    def angle(self, other):
        """ Return angle between this and other line """
        from math import atan, degrees
        if self.m is None and other.m == 0 or self.m == 0 and other.m is None:
            angle = 90
        else:
            angle = abs(degrees(atan((self.m - other.m)/(1+self.m*other.m))))
        return angle


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, width, height):
        """ Initialize rectangle at posn (upper left corner),
            with width and height
        """
        self.corner = posn
        self.width = width
        self.height = height

    def __str__(self):
        return "({0}, {1}, {2})".format(
            self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        perimeter = self.width*2+self.height*2
        return perimeter

    def area(self):
        """ Return the area of the rectangle """
        area = self.width*self.height
        return area

    def flip(self):
        " Swap rectangle width with its height """
        self.width, self.height = self.height, self.width

    def within(self, *args):
        """ Test if one or more points fall within the rectangle borders """
        count = 0
        for arg in args:
            if (self.corner.x <= arg.x <= self.corner.x+self.width
                    and self.corner.y-self.height <= arg.y <= self.corner.y):
                count += 1
        if count == len(args):
            return True
        if 0 < count < len(args):
            print(f"Only {count} points of {len(args)} fall within the rectangle")
        return False

    def collision(self, other):
        """ Return True if this rectangle overlaps with other rectangle """
        left = False
        right = False
        up = False
        down = False
        if other.corner.x < self.corner.x:
            left = True
        if other.corner.x > self.corner.x:
            right = True
        if other.corner.y > self.corner.y:
            up = True
        if other.corner.y < self.corner.y:
            down = True
        if (left and up and
            other.corner.y - other.height <= self.corner.y and
            other.corner.x + other.width >= self.corner.x):
            return True
        if (right and up and
            other.corner.y - other.height <= self.corner.y and
            other.corner.x <= self.corner.x + self.width):
            return True
        if (left and down and
            other.corner.y >= self.corner.y - self.height and
            other.corner.x + other.width >= self.corner.x):
            return True
        if (right and down and
            other.corner.x <= self.corner.x + self.width and
            other.corner.y >= self.corner.y - self.height):
            return True
        return False


class Circle:
    """ (x-a)^2 + (y-b)^2 = r^2
                or
        x^2 + y^2 + Ax + By + C = 0
    """
    
    def __init__(self, a=0, b=0, r=0):
        """ Create circle with center at (a,b) and radius r """
        self.a = a
        self.b = b
        self.r = r
        self.A = -2*self.a
        self.B = -2*self.b
        self.C = (self.a**2)+(self.b**2)-(self.r**2)

    def __str__(self):
        return f"(x-{self.a})^2 + (y-{self.b})^2 = {self.r**2:2f}"


o = Point()                              # instantiate an object of type Point
q = Point(5, 7)                          # Make a second point

print("o = Point()\nPoint() is called a constructor function")
print("o = Point(5,7).")
print("type(o):", type(o))
# print("o coords.: ({0},{1})".format(o.x,o.y))
print("o coords.:", str(o))              # use of coord method
print("q coords.: ({0},{1})".format(q.x, q.y))

q.x = 10
q.y = 15
print("\nq.x = 10\nq.y = 15")
print("q coords.: ({0},{1})".format(q.x, q.y))

print("\n***** Distance Between Points Method *****")
print("q.dist_from_origin():", q.distance())

print("\n***** Midpoint Method *****")
h = o.halfway(q)
print("h = o.halfway(q)\nh:", h)         # defining a __str__ method also changes
                                         # the behaviour of the print function
print("\n***** Mirror Method *****")
m = q.mirror()
print("m = q.mirror\nm =", str(m))

print("\n***** Slope Method *****")
s = q.slope()
print("s = q.slope()\ns =", s)

print("\n***** __add__ Magic Method *****")
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1+p2
print("p1 = Point(1,2)\np2 = Point(3,4)\np3 = p1+p2")
print("p3 =", p3)

print("\n***** Line Method *****")
print("p1.line(p2)\ny = mx+c: (m,c) =", p1.line(p2))

print("\n***** Intersect Method *****")
print("p1.intersection(p2,p3,q)\nIntersection point:", p1.intersection(p2, p3, q))
l1 = Line()
l2 = Line()
l1.line(p1, p2)
l2.line(p3, q)
pi = l1.intersection(l2)
print(pi)
print("\n***** Perpendicular Method *****")
print("p1.perpendicular(p2,p3,q)\nAre the lines perpendicular?:", p1.perpendicular(p2, p3, q))

print("\n***** Concyclic Points *****")
p1 = Point(3, 2)
p2 = Point(2, 3)
p3 = Point(-3, 2)
p4 = Point(-2, 3)
p5 = Point(3.4, 1.2)
p6 = Point(-3.4, 1.2)
p7 = Point(3.4, -1.2)
p8 = Point(3, -2)
p9 = Point(2, -3)
print(p1.concyclic(p2, p3, p4, p5, p6, p7, p8, p9))

print("\n***** Rectangle Class *****")
box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box:", box)
print("bomb:", bomb)

print("\n***** Collision Test *****")
r0 = Rectangle(Point(20, 50), 30, 30)
r1 = Rectangle(Point(30, 70), 30, 30)
r2 = Rectangle(Point(30, 40), 30, 30)
r3 = Rectangle(Point(10, 40), 30, 30)
r4 = Rectangle(Point(10, 70), 30, 30)
r5 = Rectangle(Point(30, 20), 20, 20)
r6 = Rectangle(Point(40, 40), 30, 20)
r7 = Rectangle(Point(30, 70), 20, 30)
r8 = Rectangle(Point(0, 40), 30, 20)
r9 = Rectangle(Point(30, 40), 10, 10)
r10 = Rectangle(Point(10, 70), 50, 30)
r11 = Rectangle(Point(10, 70), 30, 50)
r12 = Rectangle(Point(10, 20), 50, 30)
r13 = Rectangle(Point(30, 40), 10, 10)
r14 = Rectangle(Point(50, 20), 20, 20)
r15 = Rectangle(Point(0, 80), 10, 10)
r16 = Rectangle(Point(51, 19), 10, 10)
r17 = Rectangle(Point(100, 30), 10, 10)
r18 = Rectangle(Point(-100, 30), 10, 10)
r19 = Rectangle(Point(40, 100), 30, 30)
r20 = Rectangle(Point(40, -10), 30, 30)

print(r0.collision(r1))
print(r0.collision(r2))
print(r0.collision(r3))
print(r0.collision(r4))
print(r0.collision(r5))
print(r0.collision(r6))
print(r0.collision(r7))
print(r0.collision(r8))
print(r0.collision(r9))
print(r0.collision(r10))
print(r0.collision(r11))
print(r0.collision(r12))
print(r0.collision(r13))
print(r0.collision(r14))
print(r0.collision(r15))
print(r0.collision(r16))
print(r0.collision(r17))
print(r0.collision(r18))
print(r0.collision(r19))
print(r0.collision(r20))
