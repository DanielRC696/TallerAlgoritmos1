# 1 Verifica si 'x' está entre 'y' y 'z', y si 'w' es par:
x, y, z, w = 15, 10, 20, 8

resultado = (y <= x <= z) and (w % 2 == 0)
print(resultado)

# 2 Comprueba si 'a' es mayor que 'b' o si 'c' es igual a 'd', pero no ambas condiciones:
a, b, c, d = 7, 5, 3, 3

resultado2 = (a > b) != (c == d)
print(resultado2)

# 3 Verifica si 'x' es negativo, 'y' es positivo, y 'z' es cero:
x, y, z = -3, 5, 0

resultado3 = (x < 0) and (y > 0) and (z == 0)
print(resultado3)

