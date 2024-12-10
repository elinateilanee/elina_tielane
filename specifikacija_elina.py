def meiginajumu_sk(teksts, tips):
    meiginajumi = 4
    while meiginajumi > 0:
        try:
            ievade = tips(input(teksts))
            if ievade <= 0:
                print("Ievadītajam skaitlim jābūt pozitīvam")
                raise ValueError
            return ievade
        except ValueError:
            meiginajumi -= 1
            print(f"Jūs ievadijāt nepareizus datus, vēl ir atlikuši {meiginajumi} meiginājumi")
    print("Programma beidzās")
    exit()
        

def ievaddati():
    pieturu_sk= meiginajumu_sk("Cik daudz Jums ekskursijā būs pieturu, piem. (2)?: ", int) 
    marsuti = []
    laiki = []
    t_veidi = []
    cenas = []
    for i in range(1, pieturu_sk+1): # iziet cauri lietotāja ievadītajam pieturu sk
        marsutu_attalumi = meiginajumu_sk(f"Ievadiet maršutu attālumu {i} pieturai,piem. (55.5km) ", float)
        marsuti.append(marsutu_attalumi)
        marsutu_laiks = meiginajumu_sk(f"Ievadiet laiku līdz {i} pieturai,piem. (1.2h) ", float)
        laiki.append(marsutu_laiks)
        transpota_veids = meiginajumu_sk(f"Kāda veida transportu izmantosiet līdz {i} pieturai (1-vilciens,2-kājas, 3- autobuss)?: ", int)
        t_veidi.append(transpota_veids)
        bilesu_cena = meiginajumu_sk(f"Ievadiet biļešu cenu, lai tiktu uz {i} .pieturu, piem. 1.77 (EUR) ", float)
        cenas.append(bilesu_cena)
    skolenu_skaits = meiginajumu_sk("Cik skolēni piedalīsies ekskursijā?", int)
    return pieturu_sk, marsuti, laiki, t_veidi, cenas, skolenu_skaits #programma returno mainīgos

def redigesana(pieturu_sk, marsuti, laiki, t_veidi, cenas):
    while True: # iziet cauri ciklam
        jautajums = input("Vai Jūs vēletos kaut ko vēl rediģēt? (j/n)").lower  
        if jautajums == "n":
            break
        elif jautajums == "j":
            redigesnas_opcijas = meiginajumu_sk("Ievadiet ko tieši Jūs vēlaties rediģēt(1-maršuta attālumu, 2- maršuta laiku 3- transpota veidu, 4 - biļešu cenu):", int)
            pietura = meiginajumu_sk(f"Ievadiet kādu pieturu Jūs vēlaties rediģēt {1-pieturu_sk} ", int)
            if redigesnas_opcijas ==1:
                marsuti[pietura] = meiginajumu_sk("Ievadiet maršutu attālumu" ,pietura, ".pieturai,piem. (55.5km) ", float)
            elif redigesnas_opcijas ==2:
                laiki[pietura] = meiginajumu_sk("Ievadiet laiku līdz" ,pietura, ".pieturai,piem. (1.2h) ", float)
            elif redigesnas_opcijas ==3:
                t_veidi[pietura] = meiginajumu_sk("Kāda veida transportu izmantosiet līdz" ,pietura, ".pieturai (1-vilciens,2-kājas, 3- autobuss)?: ", int)
            elif redigesnas_opcijas ==4:
                cenas[pietura] = meiginajumu_sk("Ievadiet biļešu cenu, lai tiktu uz" ,pietura, ".pieturu, piem. 1.77 (EUR) ", float)
        else:
            print("Nepareiza datu ievade jāievade j/n")
    return pieturu_sk, marsuti, laiki, t_veidi, cenas




def laika_apreikins(laiki):
    return sum(laiki) # apreiķina maršutu laiku 

def galvenais():
    print("Labdien! Šī ir ekskursijas plānošanas programma")
    ievaddati()
    """pieturu_sk, marsuti, laiki, t_veidi, cenas =""" 
    """redigesana(pieturu_sk, marsuti, laiki, t_veidi, cenas)"""
    def izmaksu_apreikins(cenas):
        bilesu_cena_kopeja = sum(cenas) # apreiķina biļešu sumuu
        return  bilesu_cena_kopeja
    print(f"Viena skolēna kopējās izmaksas ir {izmaksu_apreikins()} EUR")
    print(f"Kopējās ekskursijas laiiks ir {laika_apreikins()} h")
    print("Lai Jums jauka šī diena")

galvenais()

