#izveidot 3 sarakstus: lietotajs pats noradis, 
# cik elementus likt saraksta.

# 1 un 2 sarkasta vertibas ievada lietotajs

# 3 saraksts vertibas iegust apvienotjot pirmos 2 sarakstus

#Katra saraksta saturu gliti smuki paradit uz ekramna
saraksts1 =[]
saraksts2 = []
print('Ievadiet cik elementus Jūs vēlaties 1 sarakstā:')
garums = int(input())
for i in range(garums):
    lieta1 = input('Ievadiet 1 saraksta vertibu:')
    saraksts1.append(lieta1)
print('Pirmā saraksta elementi:', saraksts1)

print('Ievadiet cik elementus Jūs vēlaties 2 sarakstā:')
garums2 = int(input())
for i in range(garums2):
    lieta2 = input('Ievadiet 2 saraksta vertibu:')
    saraksts2.append(lieta2)
print('Otrā saraksta elementi:', saraksts2)

jauns_saraksts = [saraksts1 +saraksts2]
print(jauns_saraksts)
