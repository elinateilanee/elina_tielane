dzivnieki = input('Vai jums būs kamielis taksī? j/n: ')
if dzivnieki == 'j':
    print('Atvainojiet, bet šim taksistam ir alerģija no kamieļiem')
    exit()
elif dzivnieki == 'n':
    pasazieri = int(input('Pasažieru skaits taksī: '))
    if pasazieri >= 4 or pasazieri <= 1:
        print('Piedodied tāds cilvēku skaits nevar braukt')
        exit()
    elif 1 <= pasazieri <= 4:
        laiks = float(input('Ievadies laiku kad Jūs braucat: '))
        if 6 <= laiks <= 21:
            diena = 0.37
        else:
            nakts = 0.77

    noligsana = input('Vai Jūs redzat taksi stacijas stāvvietā? j/n: ')
    if noligsana == 'j':
        noligsanas_maksa_parasta = 2.00
    elif noligsana == 'n':
        noligsanas_maksa_papildus = 2.00 + 2.50

    gaidisanas_laiks = input('Vai Jūs vajadzēs gaidīt j/n: ')
    if gaidisanas_laiks == 'n':
        nav_gaidisanas_laika = 0
    elif gaidisanas_laiks == 'j':
        gaidisanas_maksa = 0.15
        gaidisanas_laiks_minutes = int(input('Cik minūtes?: '))
    attalums = float(input('Cik tālu vēlaties braukt? (km): '))

    print('\n\t čeks ')
    print(f'izsaukuma laiks: {laiks:.2f}')
    print(f'gaidīšanas laiks: { nav_gaidisanas_laika or gaidisanas_laiks_minutes:.2f} min')
    print(f'attālums: {attalums:.2f} km')
    print('\n\ttarifu aprēķins')
    print('attāluma summa:', attalums*diena or attalums*nakts)
    print('izsaukums:', noligsanas_maksa_parasta or noligsanas_maksa_papildus)
    print('gaidīšana:', gaidisanas_maksa*gaidisanas_laiks_minutes or nav_gaidisanas_laika)
    kopsumma = attalums*diena or attalums*nakts + noligsanas_maksa_parasta or noligsanas_maksa_papildus + gaidisanas_maksa*gaidisanas_laiks_minutes or nav_gaidisanas_laika
    print(f'\n\t kopsumma: {kopsumma:.2f}')
    print()
    print('Paldies, ka izbraucāt ar MēsMīlamKamieļus<3')
else:
    print('Ups ir notikusi kļūda :c')