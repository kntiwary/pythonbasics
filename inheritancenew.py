class Polygon:
    "Polygon"
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    "Triangle"
    def __init__(self):
        # super(Triangle, self).__init__(self,3)
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c=self.sides
        s = (a+b+c)/2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


class Square(Polygon):
    "Square"
    def __init__(self):
        super(Square, self).__init__(4)
        # Polygon.__init__(self,4)

    def findArea(self):
        a,b,c,d=self.sides
        # s = (a+b+c)/2
        area = a*b*c*d
        print('The area of the triangle is %0.2f' % area)


# t = Triangle()
# t = Square()
# t.inputSides()
# t.dispSides()
# t.findArea()

print("{} is subclassof {}----".format(Square.__doc__,Triangle.__doc__),issubclass(Square,Triangle))
