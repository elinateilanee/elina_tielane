
#sākumā var izveidot sakārtotus sarakstus vēlaikai izmantošainai
valstis = {
        'Somija': 133,
        'Zviedrija': 5000,
        'Italija': 20000,
        'Latvija': 17777,
        'Lietuva': 245555,
        'Vacija': 16666,
        'ASV': 12222,
        'Brazilija': 14000,
        'Krievija': 35600,
        'Kina': 98000
    }
valstis_augosi = sorted(valstis, key=len)
valstis_dilstosi = sorted(valstis, key=len, reverse=True)  
iedzivoatjiAugosi = sorted(valstis, key=valstis.get)
iedzivoatjiDilstosi = sorted(valstis, key=valstis.get, reverse=True)
while True:
    print('\nTavas iespējas: \n1-Augošā secībā\n2-Dilstošā secībā\n3-Iedzīvotāju skaits\n4-Dilstošais pēc iedz. skaita\n5-Pievienot datus\n6-izdrukāt visu\nStop')
    ievadietskaitli = (input('ievadiet ciparu:' ))
    if ievadietskaitli == '1':
        print('\n\t Augošā secībā ')
        for vertiba in valstis_augosi:
            print(vertiba,valstis[vertiba])
    elif ievadietskaitli == '2':
        print('\n\t Dilstošā secībā ')
        for vertiba in valstis_dilstosi:
            print(vertiba,valstis[vertiba])    
    elif ievadietskaitli == '3':
        print('\n\t  Augošā secībā pēc iedz. skaita')
        for vertiba in iedzivoatjiAugosi:
            print(vertiba, valstis[vertiba])
    elif ievadietskaitli == '4':
        print('\n\t  Dilstoša secībā pēc iedz. skaita')
        for vertiba in iedzivoatjiDilstosi:
            print(vertiba, valstis[vertiba])
    
    elif ievadietskaitli == '5': 
        jaunavalsts = input('Ievadiet valsts nosaukumu:')
        if jaunavalsts == 'stop':
            print('Jūs izvēlējāties beigt programmu')
            break
        jauniIedzivotaji= input('Ievadiet iedz. skaitu:')
        if jauniIedzivotaji == 'stop':
            print('Jūs izvēlējāties beigt programmu')
            break
        #ar update() fun. atjaunot vārdnīcu
        valstis.update({jaunavalsts: jauniIedzivotaji})
        print('\n\nVārnīca + jaunais ieraksts:')
        for vertiba in valstis:
            print(vertiba, valstis[vertiba])
    elif ievadietskaitli == '6':
        for vertiba in valstis:
            print(vertiba,valstis[vertiba])
    elif ievadietskaitli == 'stop':
        print('Jūs izvēlējāties beigt programmu')
        break
    else:
        print('Ievadīti nekorekti dati!')