from datetime import datetime

iziesana = ['exit', 'stop','iziet']

def iegut_datus():#pārbaudes tiek ieliktas sarakstā #šī ir funkcija kas, iegūst nosaukumu,vārdu, vietu un pārbauda vai iziet no programmas
    ekspermenta_nosaukums = input('Ievadiet ekspermenta nosaukumu: ')
    if ekspermenta_nosaukums  in iziesana:
        exit()#iziet, ja nosaukums ir sarakstā 'iziesana'
    laiks = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    vards = input('Ievadiet savu vārdu: ')
    if vards in iziesana:
        exit()
    vieta = input('Ievadiet ekspermenta vietu: ')
    if vieta in iziesana: # ja lietotājs ievada str tad beidz programmu
        exit()
    return(ekspermenta_nosaukums, laiks, pareizs_vards(vards), vieta)

def pareizs_vards(vards):
    simboli= []#tukšs saraksts, kur glabās vārda burtus
    for i in vards:
        simboli.append(i) #iziet cauri katram simbolam'vards' mainigaja un pievieno sarakstam
    fiksets = ""#šeit glabās pārveidoto vārdu
    while True:
        if " " in simboli:
            simboli.remove(" ") #noņem atrarpi no vārda
        else:
            break
        #pārliecinās, ka pirmais vurts ir lielais
    simboli[0]= simboli[0].upper()
    for i in simboli: #katru elementu no simboliem pievieno'fiksets'
        fiksets = fiksets+i
    return fiksets #atgriež virkni ar lielo burtu un bez atstrapēm

'''vards = vards.replace(" ","")
vards = vards.capitalize( )'''

def saglabat_datus(dati):
    pilns = f"\nVārds: {dati[2]} - eksperiments: {dati[0]}- vieta: {dati[3]}- laiks: {dati[1]}"
    #šādā formātā un secībā dati būs failā
    file = open('ekspermenta_dati2.txt','a',encoding='utf8') #
    file.write(pilns)
    file.close()

def galvena():
    print('Sveicināti ekspermenta programmma.')
    while True: #nodrošina atkārtošanu
        saglabat_datus(iegut_datus())
        while True:
            izvele = input('Turpināt(j/n)')
            if izvele == 'n':
                exit()
            elif izvele not in ['j/n']:
                print('Nepareiza ievade!')
            else:
                break
galvena()