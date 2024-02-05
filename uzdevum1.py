#izveidot funkciju ar nosaukumu myFunction kuari nav parametru
#ši f-ja pie izsauksanas izdrukā Hello World
#izsaukt funkciju tad, ja lietotāja ievadītie vesalie skaitļi (a un b) ir vienādi
#pretējā gadijumā parādīt uz ekrāna tekstu 'nesan'\ak'
def myFunction():
    print('Sveika, pasaule!')


a= int(input('1:'))
b= int(input('2:'))
if a == b:
    myFunction()
else:
    print('Nesanāca')

def info(vards, vecums, darbs, ):
    print('Vārds:', vards)
    print('Vecums:', vecums)
    print('Amats:', darbs)
    return

info(vards='Janis', vecums='35',darbs='pavārs')

#uzrakstīt programma f-ju kas saiskta visus skaitlus sarakstā

def saraksts():
    print ('Jūsu saiskaitītie skaitļi', a+b)

a= int(input('1:'))
b= int(input('2:'))

saraksts()

list = [1,2,3,4,5,6]

def summa():
    print(sum(list))
summa()

