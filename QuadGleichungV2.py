#QuadGleichungV2

from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Unendlich viele Lösungen.")
        else:
            print("Nicht lösbar.")
    else:
        x = -c / b
        print("Eine Lösung:", x)
else:
    p = b / a
    q = c / a
    d = p ** 2 / 4 - q

    if d < 0:
        print("Nicht lösbar.")
    elif d == 0:
        x = -p / 2
        print("Doppelte Lösung:", x)
    else:
        x1 = (-p + sqrt(d)) / 2
        x2 = (-p - sqrt(d)) / 2
        print("Zwei Lösungen:", x1, "und", x2)

#TESTS:
#a: 0
#b: 0
#c: 0
#Unendlich viele Lösungen.

#a: 0
#b: 0
#c: 1
#Nicht lösbar.      

#a: 0
#b: 10
#c: 5
#Eine Lösung: -0.5 

#a: 2
#b: 3
#c: 4
#Nicht lösbar.

#a: 2
#b: 4
#c: 2
#Doppelte Lösung: -1.0

#a: 2
#b: 4
#c: 0
#Zwei Lösungen: -0.5 und -1.5

#a: a
#ValueError: could not convert string to float: 'a'

#b: b
#ValueError: could not convert string to float: 'b'

#c: c
#ValueError: could not convert string to float: 'c'