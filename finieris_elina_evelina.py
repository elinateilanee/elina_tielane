
def matrialuuzskaite():
    garums = float(input('Ievadiet podesta garumu(cm):')) # lietotāja ievade kā float skaitlis
    platums = float(input('Ievadiet podesta platumu(cm):')) 
    augstums = float(input('Ievadiet podesta augstumu(cm):')) 
    skaits = int(input('Ievadiet podesta skaitu:'))
    ievade_faila = input('Vai velaties ievadīt failā (j/n):')
    if ievade_faila == 'j':  # pārbaude vai lietotājs vēlas saglabāt failā 
        faila_nosaukums = input('Ievadiet faila nosaukumu:') # lietotājs ievada faila nosaukumu
        with open(faila_nosaukums,'a',encoding='utf8') as fails: # izvedo un saglabā informāciju failā
            fails.write(f"Podesta garums: {garums} platums: {platums} augstums: {augstums} skaits: {skaits}" ) # ieraksta failā informāciju
            fails.close 
    elif ievade_faila == 'n':
        print("\tInformācija""\nPodesta garums: ",garums,"cm""\nPodesta platums:", platums,"cm""\nPodesta augstums:",augstums,"cm""\nPodestu skaits:",skaits)
    listes = 12*skaits #apreiķini
    sturi = 8*skaits
    plaksne = 1250*5000/10
    podesta_lielums = garums*platums
    plaksnu_daudzums = podesta_lielums/plaksne
    ievade_faila2 = input('Vai velaties ievadīt failā (j/n):')
    if ievade_faila2 == 'j': # ir iespēja saglabāt failā
        with open(faila_nosaukums,'a',encoding='utf8') as fails:
            fails.write(f"\n\tApreikini matrialu daudzumiem\nListes daudzums: {listes} \nSturu daudzums:{sturi} \n Plaksnu daudzums: {plaksnu_daudzums}" )
            fails.close
    elif ievade_faila2 == 'n':
        print("\tPlaknes lielums un daudzums""\nLīstes daudzums: ",listes,"\nStūru daudzums:", sturi, "\nPlaksnu daudzums:", plaksnu_daudzums) 
matrialuuzskaite()



'''def iegut_pareizus_datus():
    with open(faila_nosaukums,'r',encoding='utf8') as fails:
        nolasiti_dati = fails.readlines()
        try:
            for garums, platums, augstums, skaits in nolasiti_dati:
                if not float or int:
                    raise ValueError
        except ValueError:
            print('Ievadiet skaitli')'''