from math import sqrt
from random import randint


class Bod:

    def __init__(self, x_daj: int = 0, y_daj: int = 0):
        self.x: int = x_daj
        self.y: int = y_daj

    def __str__(self) -> str:
        return f"[{self.x};{self.y}]"

    def vrat_vzdialenost(self, other: "Bod |None" = None) -> float:
        if other is None:
            other = Bod(0, 0)

        if not type(other) is Bod:
            raise TypeError("Nespravny typ dat!")
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    #     def spocitaj(self, other: "Bod") -> "Bod":
    #         if not type(other) is Bod:
    #             raise TypeError("Nevhodny typ argumentu! Vyzadovany je Bod.")
    #         return Bod(self.x + other.x, self.y + other.y)
    #
    #     def odcitaj(self, other: "Bod") -> "Bod":
    #         if not type(other) is Bod:
    #             raise TypeError("Nevhodny typ argumentu! Vyzadovany je Bod.")
    #         return Bod(self.x - other.x, self.y - other.y)
    #
    #     def vynasob(self, other: int) -> "Bod":
    #         if not type(other) is int:
    #             raise TypeError("Nevhodny typ argumentu! Vyzadovany je int.")
    #         return Bod(self.x * other, self.y * other)

    def __add__(self, other):
        if type(other) is Bod:
            return Bod(self.x + other.x, self.y + other.y)
        if type(other) is int:
            return Bod(self.x + other, self.y + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) is Bod:
            return Bod(self.x - other.x, self.y - other.y)
        if type(other) is int:
            return Bod(self.x - other, self.y - other)
        return NotImplemented

    def __mul__(self, other: int) -> "Bod":
        if isinstance(other, int):
            return Bod(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other: int) -> "Bod":
        if isinstance(other, int):
            return Bod(self.x * other, self.y * other)
        else:
            return NotImplemented

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, other):
        if not type(other) is int:
            raise TypeError("Nespravny typ dat pre suradnicu x! Vyzadovany je int.")
        else:
            self._x = other

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, other):
        if not type(other) is int:
            raise TypeError("Nespravny typ dat pre suradnicu y! Vyzadovany je int")
        else:
            self._y = other


def nacitaj_bod(nazov: str):
    x_temp = int(input(f"Zadaj suradnicu x bodu {nazov}:"))
    y_temp = int(input(f"Zadaj suradnicu y bodu {nazov}:"))
    return Bod(x_temp, y_temp)


def generuj_bod(od: int, do: int) -> "Bod":
    x_temp = randint(od, do)
    y_temp = randint(od, do)
    return Bod(x_temp, y_temp)



def main():
    try:
        # A = nacitaj_bod("A")
        # B = nacitaj_bod("B")
        # C = Bod(1,6)
        A = Bod(2, 3)
        B = Bod(4, 5)
        D = A + B
        E = A + 2
        F = 2 * A
    except ValueError:
        print("Suradnica musi byt cele cislo!")
    except TypeError as e:
        print(e)
    else:
        for i in range(20):
            print(generuj_bod(1,20))
        #print(A, B, D, E, F,G)


if __name__ == "__main__":
    main()
