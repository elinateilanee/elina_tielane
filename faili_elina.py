def rakstit_faila_datus(vards,uzvards,macibupreiksmets, atzime1 ): #uztaiisa funkciju ar parametriem
    try: # ja atzime ir 0 tad n/v
        with open('rezultati_elina.txt','a',encoding='utf8') as fails: #atver failu
            fails.write(f"{vards} {uzvards}: {macibupreiksmets} -{atzime1}\n") #ieraksta faila
    except FileNotFoundError:
        print('Nav pieejamā faila.Lūdzu, papildinat failu')

def iegut_datus():  #uztaiisa funkciju bez parametriem
        while True: # veic darbibu lidz ievada iziet tad breako
            print('Ievadiet datus, iziet-lai izietu')
            vards= input('Ievadiet savu vardu:') #lietotajs ievada info.
            if vards.lower()=='iziet': #ja inputa ir ar mazo burtu iziet tad beidz programmu
                break   
            uzvards = input('Ievadiet savu uzvardu:') #lietotajs ievada info.
            if uzvards.lower()=='iziet':
                break #ja inputa ir ar mazo burtu iziet tad beidz programmu
            macibupreiksmets= input('Ievadiet mācību priekšmetu:') #lietotajs ievada info.
            if macibupreiksmets.lower()=='iziet':
                break #ja inputa ir ar mazo burtu iziet tad beidz programmu
            atzime= input('Ievadiet atzimi:') #lietotajs ievada info.
            if atzime =='iziet':
                break #ja inputa ir ar mazo burtu iziet tad beidz programmu
            try: 
                atzime1 = int(atzime)
                if not 0 <= atzime1 <=10:
                    raise ValueError
            except ValueError: # ja nepareizi ievaditi dati tad
                print('Nekorekta datu ievade, ievadiet vesalu skaitli no 0-10 ') 
                continue
            atzime1 == 'n/v' if atzime1 == 0 else str(atzime1)
        rakstit_faila_datus(vards,uzvards,macibupreiksmets, atzime1 ) #izsauc funkciju

def sakartot_atzimes():
    lists = []  #izveidojas lsists
    try:
        with open('rezultati_elina.txt','r',encoding='utf8') as fails:
            nolasitidati2 = fails.readlines() #nolasa failu
        for lines in nolasitidati2: 
            vards_uzvards,prieksmets_atzime = lines.strip().split(':') # sadala rindinas
            prieksmets, atzime = prieksmets_atzime.split('-')
            if atzime =='n/v':
                atzime ==0
            else:
                atzime = int(atzime)
            lists.append(vards_uzvards +':'+ prieksmets, atzime)
            sakartots_lists = sorted(lists, key=lambda x: x[1]) # sakarto listu ar lambu
        for vards_uzvards_prieksmets, atzime in sakartots_lists:
            print(f'{vards_uzvards_prieksmets}- {atzime} ')
    except FileNotFoundError:
        print('Nav pieejama faila.Lūdzu, papildinat failu')    

def ievadit_konsole():
    try:
        with open('rezultati_elina.txt','r',encoding='utf8') as fails:
            nolasitidati = fails.readlines()  #nolasa faila rindinas
        if not nolasitidati: # ja nav ridinu tad izpilda print
            print('Nav datu, ievadiet datus')
        else:
            print(nolasitidati)
    except FileNotFoundError:
        print("Fails nav atrasts")

def galvenais(): #izveido funkciju 
    print('Šī ir failu apstrādes programma.')
    while True: 
        darbiba=input("1- Ievadīt informāciju, 2- Sakārtot atzīmes augošā secībā, 3- Izvadīt informāciju par atzīmēm konsolē, lai izietu teksts-iziet: ")
        if darbiba == '1': # ja dariba vienāeda ar 1 tad
            iegut_datus()
        elif darbiba== '2':
            sakartot_atzimes()
        elif darbiba== '3':
            ievadit_konsole()
        elif darbiba.lower() == 'iziet':
            break
        else:
            print('Nepareiza ievade. Jaizvēlas darbība no saraksta.')
galvenais()