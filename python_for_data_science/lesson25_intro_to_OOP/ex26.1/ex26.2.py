class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'X: {}, Y: {}'.format(self.get_x(), self.get_y())

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if str(x).isnumeric():
            self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if str(y).isnumeric():
            self.__y = y


point_1 = Point()
point_2 = Point(4, 5)
print(point_1, point_2)

point_1.set_y(5)
point_2.set_x(12)

print(point_1, point_2)
