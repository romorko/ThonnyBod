from math import sqrt


class Bod:

    def __init__(self, x_daj: int = 0, y_daj: int = 0):
        self.x: int = x_daj
        self.y: int = y_daj

    def __str__(self):
        return f"[{self.x};{self.y}]"

    def vrat_vzdialenost(self, other: "Bod |None " = None) -> float:
        if other is None:
            other = Bod(0,0)
        
        if not type(other) is Bod:
            raise TypeError("Nespravny typ dat!")
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, other):
        if not type(other) is int:
            raise TypeError("Nespravny typ dat!")
        else:
            self._x = other

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, other):
        if not type(other) is int:
            raise TypeError("Nespravny typ dat!")
        else:
            self._y = other


def main():
    A = Bod(1, 3)
    B = Bod(4, 5)
    print(A.vrat_vzdialenost(B))


if __name__ == "__main__":
    main()
