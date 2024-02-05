'''def atnemsana(): #funkcija netiek nodoti parametri
    print(34-4)

print('Sveika, ziema!')
atnemsana() # funkcijas atnemsana() pie izsuakšanas izvada rezultātu 30'''

#funkcijai 'plus' tiek padoti 2 parametri
#konsolē jāparāda summa
#funkciju izsauc, norādot šis 2 vertibas(argumenti)

def plus(num1, num2):
    print(num1+num2)
plus(4,5)

#nodefinēt f-ja reizināt(), iedodot parametru num1
def reizinat(num1):
    return num1*8
rez = reizinat(8)
print(rez)
#izsauc f-ju nodot skailti 8 ka argumentu num 1 un 
#funkcijas izsaukumu piesķir mainīgajam rez