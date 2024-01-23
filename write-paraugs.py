fails = open('dati.txt','w', encoding='utf8') #w izveidos failu
fails.write('Mācos rakstīt failā\n')
fails.write('Kaut kads teikums')

fails = open('dati.txt','r', encoding='utf8')
print(fails.read())