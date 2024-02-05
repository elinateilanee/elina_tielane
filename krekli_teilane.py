def krekli (skaits,apdruka,piegade):
    if apdruka == 'TEKSTS':
        sum = skaits+5*skaits
        print('Par teksta apdruku jāmaksā 5 eiro,', 'summa:', sum)
    elif apdruka == 'ZIME':
        sum = skaits+7*skaits
        print('Par teksta apdruku jāmaksā 7 eiro,', 'summa:', sum)
    elif apdruka == 'FOTO':
        sum = skaits+10*skaits
        print('Par teksta apdruku jāmaksā 10 eiro,', 'summa:', sum)
    elif sum<50:
        piegade == True and sum+15
        print('Par piekadi jāmaksā 15 eiro,', 'summa:', sum)
    elif piegade == False and sum >=50:
        sum+0
        print('Par piekadi jāmaksā 0 eiro,', 'summa:', sum)
    elif sum >= 100:
        sum*0.95
        print('Jums ir 5% atlaide,', 'summa:', sum)
krekluskaits = int(input('Ievadiet kreklu skaitu:'))
krekluapdruka = input('Ievadiet krekla apdruku:') 
piegadde = 0
krekli(krekluskaits,krekluapdruka, piegadde)
