from math import sqrt


class Bod:

    def __init__(self, x_daj: int = 0, y_daj: int = 0):
        self.x: int = x_daj
        self.y: int = y_daj

    def __str__(self)->str:
        return f"[{self.x};{self.y}]"

    def vrat_vzdialenost(self, other: "Bod" |None = None) -> float:
        if other is None:
            other = Bod(0, 0)

        if not type(other) is Bod:
            raise TypeError("Nespravny typ dat!")
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def spocitaj(self, other: "Bod") -> "Bod":
        if not type(other) is Bod:
            raise TypeError("Nevhodny typ argumentu! Vyzadovany je Bod.")
        return Bod(self.x + other.x, self.y + other.y)

    def odcitaj(self, other: "Bod") -> "Bod":
        if not type(other) is Bod:
            raise TypeError("Nevhodny typ argumentu! Vyzadovany je Bod.")
        return Bod(self.x - other.x, self.y - other.y)

    def vynasob(self, other: int) -> "Bod":
        if not type(other) is int:
            raise TypeError("Nevhodny typ argumentu! Vyzadovany je int.")
        return Bod(self.x * other, self.y * other)

    def __add__(self, other):
        if type(other) is Bod:
            return Bod(self.x + other.x, self.y + other.y)
        if type(other) is int:
            return Bod(self.x + other, self.y + other)
        raise NotImplemented
    
    def __sub__(self, other):
        if type(other) is Bod:
            return Bod(self.x - other.x, self.y - other.y)
        if type(other) is int:
            return Bod(self.x - other, self.y - other)
        raise NotImplemented
    
    def __mul__(self,other:int)->"Bod":
        if isinstance(other,int):
            return Bod(self.x * other, self.y * other)
        
    def __truediv__(self,other:int)->"Bod":
        pass
            

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


def nacitaj_bod(nazov:str):
    x_temp = int(input(f"Zadaj suradnicu x bodu {nazov}:"))
    y_temp = int(input(f"Zadaj suradnicu y bodu {nazov}:"))
    return Bod(x_temp, y_temp)

def main():
    try:
        A = nacitaj_bod("A")
        B = nacitaj_bod("B")
    except ValueError:
        print("Suradnica musi byt cele cislo!")
    else:
        print(A,B)


if __name__ == "__main__":
    main()
