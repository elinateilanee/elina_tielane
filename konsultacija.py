import datetime # lai varetu iegut datumu

def iegut_gadu():
    now = datetime.datetime.now()
    return now.year

def saglabat_faila(fails, dati):
    try:
        with open(fails,'w', encoding='utf') as file:
            for masina in dati:
                file.write('Masinas marka: ', masina['nosaukums'])
                file.write('\nGads: ', masina['gads'])
                file.write('\nModelis: ', masina['modelis'])
                file.write('\nCena: ', masina['cena'])
        print('Dati ir veiksimigi ierakstiti faila', fails)
    except Exception as e:
        print('Kluda ierakstot datus faila:', e )
#def saglavat_faila(faila_nos,dati):

masinas_sk = int(input('Par cik masinam velas saglabat info: '))  # par cik auto info
tag_gads = iegut_gadu()
#sarkasts lai glabatu auto info.
masinas = [] # sakuma tukss saraksts



for i in range(masinas_sk):
    print('\n Ievadiet info par ', i+1,'.masinu')
    nosaukums = input('Ievadiet masinas nosaukumu: ')
    gads = input('Gads: ')
    #parbauda vai ir skaitlis un vai ir lielaks par tagad-gadu
    while not gads.isdigit() or int(gads)> tag_gads: 
        print('Ievaidet pareizus datus!')
        gads = input('Gads: ')
    modelis= input('Masinas modelis: ')
    cena = input('Cena: ')
    masinas.append({"Marka": nosaukums,"gads ": gads, "modelis": modelis, "cena" : cena})

for masina in masinas:
    fails = masina["nosaukums"]+".txt"
    saglabat_faila(fails,[masina])