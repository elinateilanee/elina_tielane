#peiveinot skaitļus sarakstam
def pievienot_skaitlus():
    skaitli = []
    while True:
        try:
            skaitlis= int(input("Ievadiet skaitli(0, lai pārtrauktu darbu)"))
            if skaitlis == 0:
                break
            skaitli.append(skaitlis)
        except ValueError:
            print('Ievadiet skaitli')
    print("Saraksts", skaitli)

pievienot_skaitlus()