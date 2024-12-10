def noteikt_vertejumu_un_atzimi(procenti):
    if procenti >= 95:
        vertejums = "Izcili"
        atzime = 10
    elif procenti >= 87:
        vertejums = "Ļoti labi"
        atzime = 9
    elif procenti >= 77:
        vertejums = "Labi"
        atzime = 8
    elif procenti >= 67:
        vertejums = "Vidēji"
        atzime = 7
    elif procenti >= 54:
        vertejums = "Apmierinoši"
        atzime = 6
    elif procenti >= 41:
        vertejums = "Viduvēji"
        atzime = 5
    elif procenti >= 31:
        vertejums = "Gandrīz apmierinoši"
        atzime = 4
    elif procenti >= 21:
        vertejums = "Vāji"
        atzime = 3
    elif procenti >= 11:
        vertejums = "Ļoti vāji"
        atzime = 2
    else:
        vertejums = "Slikti"
        atzime = 1

    return vertejums, atzime

def ievadit_rezultatu():
    while True:
        try:
            rezultats = float(input("Ievadiet testa rezultātu (0-100): "))
            if 0 <= rezultats <= 100:
                return rezultats
            else:
                print("Lūdzu ievadiet skaitli no 0 līdz 100.")
        except ValueError:
            print("Nederīga ievade. Lūdzu ievadiet skaitli.")

def galvena_programma():
    while True:
        rezultats = ievadit_rezultatu()
        vertejums, atzime = noteikt_vertejumu_un_atzimi(rezultats)
        print(f"Rezultāts: {rezultats}% - {vertejums} (atzīme: {atzime})\n")

        turpinat = input("Vai vēlaties ievadīt citu rezultātu? (jā/nē): ").strip().lower()
        if turpinat != 'jā':
            print("Programma beigusies.")
            break

# Sākt programmu
galvena_programma()