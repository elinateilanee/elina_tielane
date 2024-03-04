#ar w+ izveidot failu 'dati2,txt'
fails = open('dati2.txt','w+', encoding='utf8')
#ierakstit faila sarakstu ar 3 pilsetqam
pilsetas= 'Riga\n','Marupe\n','Sigulda\n' #\n sakarto rindu 
fails.writelines(pilsetas) 
#ierakstit vienu virkni ar Hello, World
fails.write('Hello, World\n')

fails = open('dati2.txt','a+', encoding='utf8')
#pievienot vārdnīcu ar 3 valstīm un galvaspilsētām

valstis= {
        '\nSomija': 'Helsinki',
        '\nIgaunija': 'Tallina',
        '\nLatvija': 'Riga'
           }
fails.writelines(str(valstis))
