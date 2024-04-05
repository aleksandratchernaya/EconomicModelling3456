import random
class Point:
    def _init_(self, x, y):
        """
        This will be called when instantiating an object
        :param x: the value of x
        :param y: the value of y
        """
        self.x = x
        self.y = y
    def _str_(self):
        """
        This will return the string value used in printing the point
        :return:
        """
        return f"({self.x}, {self.y})"

    def _repr_(self):
        """
        This i swhen the point is in a list or other container
        :return:
        """
        return self._str_()

    def distance_origin(self):
        """
        Calculate the distance to origin of this point
        :return:
        """
        return (self.x*2 + self.y2)*0.5

    def _gt_(self, other):
        """
        define how a point is greater than another
        :param other: the other point to compare against
        :return:
        """
        return self.distance_origin() > other.distance_origin()

    def _eq_(self, other):
        """
        define when 2 points are equal
        :param other:
        :return:
        """
        return self.distance_origin() == other.distance_origin()


a = Point(2, 3)
b= Point(7, 9)
print(f"a=({a.x}, {a.y})")
print(f"b=({b.x}, {b.y})")

# creating a list of random 5 points
points = [] # initialize an empty list
for _ in range(5):
    # x = random.randint(-100, 100)
    # y = random.randint(-100, 100)
    # random_points = Point(x, y)
    # points.append(random_points)

    # or in a single line like this
    points.append(Point(random.randint(-100, 100),
                        random.randint(-100, 100)))

for point in points:
    print(f"n({point.x}, {point.y})")

# try to print the first point
print("printing a point value:", points[0])
print(points)

a = Point(3, 4)
print(f"distance origin a={a.distance_origin()}")
b = Point(5, 12)
print(f"distance origin b={b.distance_origin()}")
print(f"a > b = {a > b}, a < b = {a < b}")

points.sort()
print(f"largest point in the list is {points[-1]}") # the largest is the last in ordered list