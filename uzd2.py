#tukšs saraksts, kur būs mašīnas
masinas = []
def pievienot_masinu(nosaukums,marka,gads):
    masinas.append({
        "nosaukums":nosaukums,
        "marka":marka,
        'gads':gads,
    })
    print(f"Mašīna '{nosaukums}'pievienot sarakstam. ")

def paradit_masinas():
    if masinas:
        print("\nMašīnas sarakstā:")
        for masina in masinas:
            print(f"Nosaukums:{masina["nosaukums"]}, Marka:{masina["marka"]}, Gads:{masina["gads"] }")
    else:
        print("\nSaraksts ir tukšs")
def atjaunot_masinu(nosaukums,jauna_marka,jauns_gads):
        for masina in masinas:
            if masina["nosakumus"] == nosaukums:
                masina["marka"] == jauna_marka
                masina["gads"] == jauns_gads
                print(f"Mašīna '{nosaukums}' atjaunināta")
                return
        print(f"Mašīna '{nosaukums}' nav atrasta sarakstā")

def dzest_masinu(nosaukums):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masinas.remove(masina)
            print(f"Mašīna '{nosaukums}' dzesta no saraksta")
            return 
    print(f"Mašīna '{nosaukums}' nav atrasta saraksta")

while True:
    print("\nIzvēlēties darbību")
    print("1Pievienot mašinu:")
    print("2 Paradīt visas  mašinas:")
    print("3 Atjauninat mašinu:")
    print("4 Dzēst  mašinu:")
    print("5 Iziet")

    izvele =input("Izvelies darbibu (1-5): ")
    if izvele == "1":
        nosaukums = input('Ievadiet masinas nosaukums')
        marka = input('Ievadiet masinasmarku')
        gads = int(input('Ievadiet masinas gadu'))
        pievienot_masinu(nosaukums,marka,gads)
    elif izvele == "2":
        paradit_masinas()

    elif izvele == "3":
        nosaukums = input('Ievadiet masinas nosaukums')
        jauna_marka = input("Ievadiet jauno marku:")
        jauns_gads = int(input('Ievadiet jauno masinas gadu'))
        atjaunot_masinu(nosaukums,jauna_marka,jauns_gads)

    elif izvele == "4":
        nosaukums = input('Ievadiet masinas nosaukums')
        dzest_masinu(nosaukums)
    elif izvele == "5":
        break
    else:
        print("Nepareiza ievade")