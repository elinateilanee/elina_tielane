#izstrādāt programmu ar funkciju palaīdzību pārvērš Clesija grādus uz Fārenheita
#grādus ievada lietotājs

def gradi():
    print('F. būs', a * (9/5) + 3)
a = int(input('Ievadiet grādus:'))

gradi()

def kermenis():
    print('Jūsu ĶMI ir', ĶMI)
svars = float(input('Ievadiet savu svaru: '))
augums = float(input('Ievadiet augumu: '))
ĶMI = svars/ augums*augums

if ĶMI < 18.5:
    print('Jums ir nepietiekama ķermeņa masa')
elif ĶMI >= 18.5 and ĶMI <= 24.99:
    print('Jums ir normāla ķermeņa masa')
elif ĶMI >= 25 and ĶMI <= 29.99:
    print('Jums ir liela ķermeņa masa')
elif ĶMI > 30:
    print('Jums ir aptaukošanās')

kermenis()