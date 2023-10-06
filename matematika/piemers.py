import math
import random
skaitlis = 43.7
print('Noapoļots uz leju:',math.floor(skaitlis))
print('Noapoļots uz augšu:', math.ceil(skaitlis))

print('Mainiga pakape', math.pow(skaitlis,2))
print(math.pow(4,6)) #pirmais sk ir tas, ko kapina , otrais ir pakape
pakape = 3
print(math.pow(skaitlis, pakape))

print('Kvadratsakne:', math.sqrt(skaitlis))

x = 2312431242/231243
print('x:', x)
print('Formatēts x: ' "%.3f"%x)
print('Formatēts x: ' "{:.2f}".format(x))

cipars = random.random() #0.1-1.0
print (cipars)

cipars2 = random.randint(1,50)
print(cipars2)
