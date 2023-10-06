taksatarifsnakti = 0.77
taksatarifsdiena = 0.37
pasazieri = int(input('Pasažieru skaits taksī:'))
if pasazieri >4 or pasazieri==0:
    print('Piedodied tāc cilvēku skaits nevar braukt')
elif pasazieri <4:
    print('Jūs drīkstat braukt')
laiks = int(input('Iveadi laiku kad vēlies izbraukt:'))
if laiks > 21 or laiks < 6:
    print(taksatarifsnakti)
elif laiks:
    print(taksatarifsdiena)
noligsana = (input('Vai jūs redzat taksi stacijas stāvvietā? j/n:'))
if noligsana == 'j':
    print('Nolīgšanas maksa ir 2 eiro')
elif noligsana == 'n':
        print('Nolīgšanas maksa ir 4,50 eiro')
gaidisanas_laiks =  (input('Vai jūs vajadzēs gaidīt? j/n:'))
if gaidisanas_laiks == 'j':
     print('Būs jāmaksā 0,15 par 1 min')
elif gaidisanas_laiks == 'n':
     print('Ok')
attālums = (input('Cik tālu vēlaties braukt?:'))
