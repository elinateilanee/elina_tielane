from datetime import datetime  #programma importē laiku
def saglabat_datus(vards,ekspermenta_nosaukums, vieta, laiks): # izveido funkciju ar parametriem
    try: # pārbauda failu
        with open('ekspermenta_dati.txt','a',encoding='utf8') as fails: #atver failu
            fails.write(f"{vards} - {ekspermenta_nosaukums} - {vieta} - {laiks}\n") #ieraksta faila
    except FileNotFoundError: # programma parāda, ka fails nav atrasts
        print('Nav pieejamā faila.Lūdzu, papildinat failu')

iziesana = ['exit', 'stop','iziet']

def iegut_datus(): 
    while True: 
        print('Ievadiet datus, iziet/stop/exit-lai beigtu programmu')
        vards = input('Ievadiet savu vārdu: ')
        if vards in iziesana:
            break  # beidz programma
        ekspermenta_nosaukums = input('Ievadiet ekspermenta nosaukumu: ')
        if ekspermenta_nosaukums  in iziesana:
            break
        vieta = input('Ievadiet ekspermenta vietu: ')
        if vieta.lower() in iziesana: # ja lietotājs ievada str tad beidz programmu
            break
        now = datetime.now()
        laiks = now.strftime("%m/%d/%Y, %H:%M:%S")
        saglabat_datus(vards,ekspermenta_nosaukums, vieta, laiks)

'''def pareizs_vards(vards):
    pareizais_vards = vards.split() and vards.upper()'''
    

def galvena():
    print('Sveiki! Šī ir ekspermenta programmma.')
    print('---------')
    iegut_datus()
galvena()
