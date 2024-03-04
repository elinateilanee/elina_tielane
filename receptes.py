'''darbu sak ar funkciju saglabat_recepti(),
kas lauj ievadit nosaukumu un kaloriju saturu.
Saglaba sos datus faila 'receptes.txt'.
funkcija paradit_recepti(), atver failu un izvada visu 
recepsu nosaukumus;
funkcija paradit_visas_receptes() '
parādīs receptes un kalorijas'''

def saglabat_recepti():
    receptes = {}
    while True:
        nosaukums= input('Ievadiet receptes nosaukumu(iziet-lai partrauktu) ')
        if nosaukums.lower()=='iziet':
            break
        kalorijas= float(input('Ievadiet kaloriju daudzumu: '))
        receptes[nosaukums]=kalorijas

    with open('receptes.txt','w',encoding='utf8') as fails:
        for nosaukums,kalorijas in receptes.items():
            fails.write(f"{nosaukums}: {kalorijas}\n")

def paradit_visas_receptes():
    try:
        with open('receptes.txt','r',encoding='utf8') as fails:
            print('Pieejamās receptes: ')
            for rinda in fails:
                nosaukums,kalorijas=rinda.strip().split(': ')
                print(f"{nosaukums}-{kalorijas} kcal.")
    except FileNotFoundError:
        print('Nav pieejamu recepšu.Lūdzu, papildinat failu')

#parādīs vienu konkrētu recepti
def  paradit_recepti():
    try:
        with open('receptes.txt','r',encoding='utf8') as fails:
            receptes={}
            for rinda in fails:
                nosaukums,kalorijas=rinda.strip().split(': ')
                receptes[nosaukums]=float(kalorijas)
        print("Pieejamas receptes")
        #izdrukā pieejamo recepšu nosaukumus
        for nosaukums in receptes:
            print(nosaukums)
        izvele=input('Izvelieties recepti(vares redzet kalorijas): ')
        if izvele in receptes:
            print(f"{izvele} kaloriju saturs: {receptes[izvele]} kcal")
        else:
            print('Recepte nav atrasta.')
    except FileNotFoundError:
        print('Nav pieejamu recepšu.Lūdzu, papildinat failu')
def galvenais():
    print('Šī ir DIY recepšu programma.')
    while True:
        darbiba=input("1- Saglabat receptes, 2- Redzēt visas receptes, 3- Sīkāks info. par recepti, q-iziet: ")
        if darbiba == '1':
            saglabat_recepti()
        elif darbiba== '2':
            paradit_visas_receptes()
        elif darbiba== '3':
            paradit_recepti()
        elif darbiba.lower() == 'q':
            break
        else:
            print('Nepareiza ievade. Jaizvēlas darbība no saraksta.')
galvenais()