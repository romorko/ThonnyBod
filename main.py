from math import sqrt
from random import randint
import turtle


class Bod:

    def __init__(self, x_daj: int = 0, y_daj: int = 0):
        self.x: int = x_daj
        self.y: int = y_daj

    def __str__(self) -> str:
        obsah = f"[{self.x:2};{self.y:2}]"
        return f"{obsah:10}"

    def vrat_vzdialenost(self, other: "Bod |None" = None) -> float:
        if other is None:
            other = Bod(0, 0)

        if not type(other) is Bod:
            raise TypeError("Nespravny typ dat!")
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

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


def generuj_bod(od: int = 0, do: int = 20) -> "Bod":
    x_temp = randint(od, do)
    y_temp = randint(od, do)
    return Bod(x_temp, y_temp)


def porovnaj(a: "Bod") -> int:
    return a.vrat_vzdialenost()


def main():
    tabula = turtle.Screen()
    rozl_x = 1024
    rozl_y = 768
    polos_x = rozl_x // 2
    polos_y = rozl_y // 2
    gen_od = -15
    gen_do = 15
    tabula.screensize(rozl_x, rozl_y)
    tabula.title("Vygenerovane body")
    pero = turtle.Turtle()
    pero.pensize(2)
    pero.pencolor("blue")

    pero.teleport(-rozl_x // 2, 0)
    pero.forward(rozl_x)
    pero.teleport(0, -rozl_y // 2)
    pero.lt(90)
    pero.forward(rozl_y)

    body = list()
    for _ in range(10):
        body.append(generuj_bod(gen_od, gen_do))

    # body1 = [generuj_bod(1,20) for _ in range(10)]
    body.sort(key=porovnaj)

    p_x = polos_x // (gen_do)
    cislo = 0
    for i in range(-p_x, -polos_x, -p_x):
        pero.teleport(i, -3)
        pero.fd(6)
        pero.write(cislo := cislo - 1)

    cislo = 0
    for i in range(p_x, polos_x, p_x):
        pero.teleport(i, -3)
        pero.fd(6)
        pero.write(cislo := cislo + 1)

    pero.lt(90)
    p_y = polos_y // (gen_do)
    cislo = 0
    for j in range(-p_y, -polos_y, -p_y):
        pero.teleport(3, j)
        pero.fd(6)
        pero.up()
        pero.fd(15)
        pero.down()
        pero.write(cislo := cislo - 1)

    cislo = 0
    for j in range(p_y, polos_y, p_y):
        pero.teleport(3, j)
        pero.fd(6)
        pero.up()
        pero.fd(15)
        pero.down()
        pero.write(cislo := cislo + 1)

    pero.lt(-90)
    for index,i in enumerate(body):
        pero.teleport(i.x * p_x, i.y * p_y)
        pero.dot(10, "red")
        pero.up()
        pero.fd(5)
        pero.down()
        pero.write(f"   {index+1}->{i}",align="left", font=("Courier", 12, "bold"))
        pero.up()
        pero.fd(10)
        pero.down()
        pero.color("red")
        pero.teleport(i.x * p_x/2, i.y * p_y/2)
        pero.write(f"{i.vrat_vzdialenost():.2f}",align="left", font=("Courier", 12, "bold"))
        pero.color("black")

        k = 0
        if i.y > 0:
            while k < i.y * p_y:
                pero.teleport(i.x * p_x, k)
                k += 10
                pero.setposition(i.x * p_x, k)
                k += 10
        elif i.y < 0:
            while k > i.y * p_y:
                pero.teleport(i.x * p_x, k)
                k -= 10
                pero.setposition(i.x * p_x, k)
                k -= 10

        k = 0
        if i.x > 0:
            while k < i.x * p_x:
                pero.teleport(k, i.y * p_y)
                k += 10
                pero.setposition(k, i.y * p_y)
                k += 10
        elif i.x < 0:
            while k > i.x * p_x:
                pero.teleport(k, i.y * p_y)
                k -= 10
                pero.setposition(k, i.y * p_y)
                k -= 10
                
        pero.teleport(i.x * p_x, i.y * p_y)
        pero.color("red")
        pero.setposition(0,0)
        pero.color("black")

        k = 0
        if i.y > 0:
            while k < i.y * p_y:
                pero.teleport(i.x * p_x, k)
                k += 10
                pero.setposition(i.x * p_x, k)
                k += 10
        elif i.y < 0:
            while k > i.y * p_y:
                pero.teleport(i.x * p_x, k)
                k -= 10
                pero.setposition(i.x * p_x, k)
                k -= 10

        k = 0
        if i.x > 0:
            while k < i.x * p_x:
                pero.teleport(k, i.y * p_y)
                k += 10
                pero.setposition(k, i.y * p_y)
                k += 10
        elif i.x < 0:
            while k > i.x * p_x:
                pero.teleport(k, i.y * p_y)
                k -= 10
                pero.setposition(k, i.y * p_y)
                k -= 10

    for i in body:
        print(f"{i} {i.vrat_vzdialenost():6.2f}")
    tabula.mainloop()


if __name__ == "__main__":
    main()