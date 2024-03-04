#ielasit programma faila saturu
import sys
def nolasit_failus(failins):
    try:
        with open(failins, 'r', encoding='utf8') as file:
            saturs = file.read()  #glabā faila saturu
            return saturs 
    except FileNotFoundError as e:
        print(f"Fails {failins} nav atrasts,", file=sys.stderr)

#funkcija, kas saskaita sibolus faila
def saskaitit(saturs):
    return len(saturs)

#funkcija kas izvada 1 un pedejo simbolu
def pirmais_un_pedejais(saturs):
    return saturs[0], saturs [-1]

def lasit_simbolus(failins, garums):
    try:
        with open(failins, 'r', encoding='utf8') as file:
            saturs = file.read(int(garums))
            return saturs
    except FileNotFoundError as e:
        print(f"Fails {failins} nav atrasts,", file=sys.stderr)
    except ValueError:
        return 'Garums jabūt skaitlim'
#funkcija kas nolasa 1 rindinu
def lasit_pirmio_rindinu(failins):
    try:
        with open(failins, 'r', encoding='utf8') as file:
            pirmarinda = file.readline()
            print(pirmarinda)
    except FileNotFoundError as e:
        print(f"Fails {failins} nav atrasts,", file=sys.stderr)

failins = input('Ludzu ievadiet faila nosaukumu: ')
saturs = nolasit_failus(failins)

if saturs:
    print('1) Simbolu skaits:', saskaitit(saturs) )
    print('2) 1 in pedejais simbols:', pirmais_un_pedejais(saturs) )

    garums = input('Ludzu ievadiet garumu: ')
    print('3) Simboliu no sakuma lidz garumam:', lasit_simbolus(failins, garums))

    print('\nPirma rindina:')
    lasit_pirmio_rindinu(failins)
