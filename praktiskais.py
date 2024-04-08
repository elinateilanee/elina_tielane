#atvērt failu skaitli.txt(šajā gadījumā fails tiek izveidots, jo ir w režīms)
with open("skaitli.txt", "w") as fails:
    print("Ievadiet skaitļus failā(katru skaitli ievadiet jaunā rindiņā.")
    print("Ievadiet tukšu rindiņu, lai pabeigtu ievadi.")
    
    while True:
        skaitlu_ievade = input("Ievadiet skaitli: ")
        if skaitlu_ievade == "": #ja ievada tukšu rindu, tad tiek pabeigta ievade (ja vēlas, var aizstāt ar stop vai iziet utt)
            break
        fails.write(skaitlu_ievade + "\n") #tiek nolasīti lietotāja ievadītie skaitļi un ierakstīti failā

with open("skaitli.txt", "r") as fails: #ar r režīmu nolasa faila saturu, encoding pie skaitļiem teorētiski nebūtu vajadzīgs
    rindas = fails.readlines() #nolasa faila saturu un sadala pa rindām

#mainīgie, kas glabās rezultātu(pozitīvo, negatīvo sk summa, cik ir pozitīvo un cik ir negatīvo skaitļu)
poz_summa = 0
neg_summa = 0
poz_skaits = 0
neg_skaits = 0

for rinda in rindas:#iziet cauri rindām
    skaitlits = int(rinda.strip()) #rinda tiek pārbeidota par veselu skaitli

    if skaitlits > 0:
        poz_summa += skaitlits
        poz_skaits += 1
    elif skaitlits < 0:
        neg_summa += skaitlits
        neg_skaits += 1 #ifā ielitka skaitļu pārbaude

print("➕ skaitļu summa:", poz_summa)
print("➖ skaitļu summa:", neg_summa)
print("➕ skaitļu skaits:", poz_skaits)
print("➖ skaitļu skaits:", neg_skaits)

#šeit tiek izdrukāta vidējā vērtība poz skaitļiem un neg skaitļiem
if poz_skaits > 0:
    print("Vidējais pozitīvais skaitlis:", poz_summa / poz_skaits)
else:
    print("Nav pozitīvu skaitļu")
if neg_skaits > 0:
    print("Vidējais negatīvais skaitlis:", neg_summa / neg_skaits)
else:
    print("Nav negatīvu skaitļu")

    #darbu būtu vērts papildināt līdzīgi kā recepšu failu-ar izņēmumiem, ja fails ir tukšs vai tāda faila nav utt
    #tāpat arī būtu jāpārbauda vai lietotājs tiešām ievada skaitļus
    
    #except ValueError:
    #print("Jāievada skaitlis.")
    #exit() 