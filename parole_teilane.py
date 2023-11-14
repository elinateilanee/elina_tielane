parole = 'kamielis' # definē mainīgo parole
lietotājvārds = '12345'# definē mainīgo lietotājvārds
original_range = range(1, 5) # uztaisīt range no kā sākt un ar ko beigt
reversed_range = list(original_range)[::-1] # apmainīt range lai sākots no 4 - 1
num = 0 
print('Pareizais lietotājvārds ir kamielis un parole 12345') 
lietotājvārds = input('Lūdzu ievadiet savu lietotājvārdu: ') # lietotājs ievada savu lietotājvārdu
parole = input('Lūdzu ievadiet savu paroli: ') # lietotājs ievada savu paroli
while lietotājvārds != 'kamielis' or parole != '12345' : # iznamon while funkciju
    lietotājvārds = input('Lūdzu ievadiet savu lietotājvārdu: ') # lietotājs ievada savu lietotājvārdu
    parole = input('Lūdzu ievadiet savu paroli: ') # lietotājs ievada savu paroli
    if lietotājvārds != 'kamielis':  # ja lietotājs nav kamielis tad
        for num in reversed_range:  # apamaina range
            print('Ir atlikuši vēl',num, 'meiģinājumi!')
    if num< 1: # ja mainīgais mazāks par 1
        exit # beidzasn darbība
    elif lietotājvārds != 'kamielis' and parole != '12345': # ja lietotājvārds un parole ir nepareizas tad
        print('Parole ir jābūt 5 rakstzīmes garai!')
        for num in reversed_range: # apamaina range
            print('Ir atlikuši vēl',num, 'meiģinājumi!')
    if num< 1:  # ja mainīgais mazāks par 1
        exit # beidzasn darbība
print('Pieslēgšanās veiksmīga')
vesalais_skaitlis_pirmais  = input('Ievadiet 1 vesalo skaitli:')
if vesalais_skaitlis_pirmais == 'stop':
    print('Programmas beigas!')