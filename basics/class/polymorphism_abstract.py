from abc import ABC, abstractmethod


class CoordinateAbstract(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def get_distance(self):
        pass


class CartesianCoordinate2D(CoordinateAbstract):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # get_distance must be overridden
    def get_distance(self):
        return self.x**2 + self.y**2

    # define the different method with the same name
    def show_coordinate(self):
        print(f"(x, y) = ({self.x}, {self.y})")


class CartesianCoordinate3D(CoordinateAbstract):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # get_distance must be overridden
    def get_distance(self):
        return self.x**2 + self.y**2 + self.z**2

    # define the different method with the same name
    def show_coordinate(self):
        print(f"(x, y, z) = ({self.x}, {self.y}, {self.z})")


if __name__ == "__main__":
    # abstract base class cannot be instantiated
    # coord = CoordinateAbstract(0.0)

    coord_2d = CartesianCoordinate2D(-2.1, 3.9)
    coord_2d.show_coordinate()
    print(f"distance from origin: {coord_2d.get_distance()}")
    print()

    coord_3d = CartesianCoordinate3D(-2.1, 3.9, 10.0)
    coord_3d.show_coordinate()
    print(f"distance from origin: {coord_3d.get_distance()}")
    print()

    # return true if the class is the same or derived class
    print(
        f"isinstance(coord_2d, CoordinateAbstract): {isinstance(coord_2d, CoordinateAbstract)}"
    )
    print(
        f"isinstance(coord_3d, CoordinateAbstract): {isinstance(coord_3d, CoordinateAbstract)}"
    )
