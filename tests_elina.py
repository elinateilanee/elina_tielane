 """def noteikt_vertejumu_un_atzimi():
    if ievadita_atzime >= 0 and ievadita_atzime <= 10:
       print(f'Rezultāts: {ievadita_atzime} - Ļoti, ļoti slikti (atzīme 1)' )
    elif ievadita_atzime >= 11 and ievadita_atzime <= 20:
        print(f'Rezultāts: {ievadita_atzime} - Ļoti slikti (atzīme 2 )' )
    elif ievadita_atzime >= 21 and ievadita_atzime <= 30 :
        print(f'Rezultāts: {ievadita_atzime} - slikti (atzīme 3`)' )
    elif ievadita_atzime >= 31 and ievadita_atzime <= 40 :
        print(f'Rezultāts: {ievadita_atzime} - vāji (atzīme 4`)' )
    elif ievadita_atzime >= 41 and ievadita_atzime <= 53 :
        print(f'Rezultāts: {ievadita_atzime} - viduvēji (atzīme 5`)' )
    elif ievadita_atzime >= 54 and ievadita_atzime <= 66 :
        print(f'Rezultāts: {ievadita_atzime} - viduvēji (atzīme 6`)' )
    elif ievadita_atzime >= 67 and ievadita_atzime <= 76 :
        print(f'Rezultāts: {ievadita_atzime} - labi (atzīme 7`)' )
    elif ievadita_atzime >= 77 and ievadita_atzime <= 86:
        print(f'Rezultāts: {ievadita_atzime} - ļoti labi (atzīme 8`)' )
    elif ievadita_atzime >= 87 and ievadita_atzime <= 94:
        print(f'Rezultāts: {ievadita_atzime} - izcili (atzīme 9`)' )
    elif  ievadita_atzime >= 95 and ievadita_atzime <= 100:
        print(f'Rezultāts: {ievadita_atzime} - ļoti izcili (atzīme 10`)' )
    """

def ievadit_rezultatu():
    while True:
        try:
            ievadita_atzime = float(input("Testa rezultatu (0-100) "))
            if ievadita_atzime   >=  0 and ievadita_atzime  <= 100:
                return ievadita_atzime 
            else:
                print("Ievadiet no 0 -100")
        except ValueError:
            print('Nederīga ievade')

def darbiba():
    while True:
            ievadita_atzime = ievadit_rezultatu()
            vertejums, atzime = noteikt_vertejumu_un_atzimi(ievadita_atzime )
            print(f"Rezultāts: {ievadita_atzime }% - {vertejums} (atīme)")

            turpinat = input("Vai ievadīsiet citu rezultātu(jā/nē)")
            if turpinat != 'jā':
                    print("Programma beigusies!")
                    break