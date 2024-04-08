''''prasīt ievadīt datus līdz brīdim kamēr ievada tukšu rindu.
datus saglabāt failā'''
dati = []
while True:
    ievadesdati = input('Ievadiet datus(iziet-lai izietu),Enter, lai beigtu rakstīt: ')
    if ievadesdati.lower() == 'iziet':
        print('Programma pārtraukta')
        break
    #pārtrauc ciklu, ja ievada tukssu rindu Enter
    elif not ievadesdati:
        break
    dati.append(ievadesdati)
    #atvērt failu, lai ierakstītu datus
    with open("jaunais_fails.txt", 'w', encoding='utf8') as file:
        #ieraksta katru sava rinda
        for line in dati:
            file.write(line+'\n')
    print('Dati ir ierakstiti jaunaja failā.')