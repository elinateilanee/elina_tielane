try:
    krekluskaits = int(input('Ievadiet kreklu skaitu:'))
    krekluapdruka = int(input('Ievadiet krekla apdruku \n 1-Teksts(5 EUR) \n 2-Zime (7 EUR) \n 2-Zime (10 EUR):'))
except ValueError:
    print('Error')
    exit()
piegade = input('Ir piegade (j/n):')
if piegade not in ['j', 'n'] or krekluapdruka not in [1,2,3] or krekluskaits < 0:
    print(' Ievadīt pareizus datus.')
    exit()

if piegade == 'j':
    piegade = True
else:
    piegade = False

def pasuti_teketrus (skaits, apdruka, piegade):
    krekli = skaits*[5,7,20][apdruka-1] # apreikina cenu bez atlaides
    #apreiķina piegādes maksu
    if krekli >=50 and piegade ==True:
        piegade= 0
    if krekli < 50 and piegade ==True:
        piegade= 0    
    else:
        piegade = 'Nav.'
    #apreikina atbildi
    if krekli>100:
        atlaide = round(krekli*0.05,2)
    else:
        atlaide = 0 

    kopsumma = krekli-atlaide
    if type(piegade) != str:
        kopsumma = kopsumma+piegade
    if type(piegade) != int:
        piegade = str(float(piegade))+ 'EUR'
    return [krekli, piegade, atlaide, kopsumma]


rez = pasuti_teketrus(krekluskaits, krekluapdruka, piegade)
print('-----IZMAKSAS------')
print('Kopējā cena - ', rez[3], 'EUR \n', 'Krekli-',float(rez[0]), 'EUR \n ''piegade- ', rez[1],'atlaide - ', rez[2],'EUR')