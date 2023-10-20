atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('Vai briesmonis ir draudzīgs?(j/n)')
print('Bēdz prom!')

#pārbaudīt vai lietotājs prot reizināt ar 7 
#programma atrkārtp darbību līdz brīdim, kad usdpto vsisi 12 jautājumi
'''reiz = 7
for i in range (1,13): #cikla mainīgais no 1-12
    print("Cik ir",i,'x',reiz,'?')
    minejums = input()
    if minejums == 'stop':
        break
    if minejums == 'izlaist':
        print('Tiek izlaists')
        continue #izlaiž 1 jautājumu un turpina tālāk
    atb = i * reiz
    if int(minejums) == atb:
        print('Pareizi!')
    else:
        print('Nē, tas ir',atb)
        #ja ir nepareizi, tad atgriežas pie jautājuma
        # reizinātāju ievada lietotājs'''
    