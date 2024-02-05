#vienkārsa fun ar lietotaja datu ievadi un nosacfijumiem
def parbaudit_skaitli(skaitlis):
    if  skaitlis>0:
        print('Skaitlis ir pozitivs')
    elif skaitlis<0:
        print('Skaitlis ir negativs')
    else:
        print('Skaitlis ir 0')
lietotajuskaits = float(input('Īevadiet skaitli: '))
parbaudit_skaitli(lietotajuskaits)