import math
import random
radiuss = int(input('Ievadiet rinķa līnijas rādiusu:'))
print(radiuss)
PI = 3.1415
print('Rinķa līnijas garums:', 2*PI*radiuss)
print('Rinķa līnijas Laukums:', radiuss*radiuss*PI)
katete1 = int(input('Ievadiet taisnlenķa trijstūra pirmās katetes garumu:'))
print(katete1)
katete2 = int(input('Ievadiet taisnlenķa trijstūra otrās katetes garumu:'))
print(katete2)
h = math.sqrt(katete1*katete1+katete2*katete2)
print('Taisnlenķa trijstūra hipotenūzas garums:', h)
print('Gadījuma skaitlis no 0 - 1:', random.random())