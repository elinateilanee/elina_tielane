saraksts = [2,5,8,1,10,2,6]
saraksts.append('Cepums') # sis elements ar append tiks pielikts saraksta beigas
print(saraksts)

#izmet no beigām
saraksts.pop() # izmet 1 no beigam
print(saraksts)

saraksts.insert(3, 'Hello!') # ievieto 3 no kreisas
print(saraksts)

saraksts.remove(5) # izdzes noradito vertibu
print(saraksts)

#funcijas del pieleitojums
tests = [1,2,3,4,5,6,7,8]
del saraksts[2] #izdzes vienu elementu
print(tests)

del tests[3:6]
print(tests) #izdzes intervalu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2] #no 2 - 7 elementam dzes katru 2
print (cipari)

