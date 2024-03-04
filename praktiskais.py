#uzrakstit program. kas lasa katru rindinu un sadal to vārdos
#programma parbauda vai ir pietiekams datu skaits, lai izvaditu informaciju un pec tam izvada datus uz ekrana

faila_nosaukums= 'dati3,txt'

try:
    with open(faila_nosaukums,'r', encoding='utf8') as fails:
#3- katru rindu sadala pa vardiem izmantojot atstarpes ka atdalitajus
        for rinda in fails:
            dati = rinda.split()
#4 - parbaudit vai ir pietiekams datu skaits(vards,uzverds,vecums)
            if len(dati) >= 3:
                vards = dati[0]
                uzvards = dati[1]
                vecums = dati[2]
#5 - parādīt datus uz ekreāna
                print(f'Vārds:{vards}','Uzvards:{uzvards}','Vecums:{vecums}')
            else: 
                print('Kluda faila nepietiek datu.')
except FileNotFoundError:
    print(f'Kluda: Fails'{faila_nosaukums}'nav atrasts.')
except Exception as e:
    print(f'Kluda:Neparedzeta kluda = {e}' )