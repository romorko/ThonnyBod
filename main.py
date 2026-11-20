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


def generuj_bod(od: int=0, do: int=20) -> "Bod":
    x_temp = randint(od, do)
    y_temp = randint(od, do)
    return Bod(x_temp, y_temp)

def porovnaj(a:"Bod")->int:
    return int(a.vrat_vzdialenost())
        

def main():
    tabula = turtle.Screen()
    tabula.screensize(800,600)
    tabula.title("Vygenerovane body")
    pero = turtle.Turtle()
    pero.up()
    pero.pensize(2)
    pero.pencolor("blue")
    
    pero.setpos(-400,0)
    pero.down()
    pero.forward(800)
    pero.up()
    pero.setpos(0,-300)
    pero.lt(90)
    pero.down()
    pero.forward(600)
    
    body = list()
    for _ in range(10):
        body.append(generuj_bod(-15,15))
    
    #body1 = [generuj_bod(1,20) for _ in range(10)]
    body.sort(key=porovnaj)
    
    p=-400//20
    for i in range(-400,400,20):
        pero.up()
        pero.setpos(i,-5)
        pero.down()
        pero.fd(10)
        pero.write(p)
        p+=1
        
        
    pero.lt(90)
    p=-300//20
    for j in range(-300,300,20):
        pero.up()
        pero.setpos(5,j)
        pero.down()
        pero.fd(-10)
        pero.write(p)
        p+=1
    
    pero.lt(-90)
    for i in body:
        pero.up()
        pero.setpos(i.x*20,i.y*20)
        pero.down()
        pero.dot(10,"red")
        pero.up()
        pero.fd(5)
        pero.down()
        pero.write(f"{i}")
        pero.up()
    
    for i in body:
        print(f"{i} {i.vrat_vzdialenost():6.2f}")
    tabula.mainloop()           

if __name__ == "__main__":
    main()
