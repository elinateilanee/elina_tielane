# r režīmam failam jabūt mapē
#f=open('demo.txt','r', encoding='utf8')
#print(f.read()) # izdrukā faila saturu

'''f=open('demo.txt','r', encoding='utf8')
print(f.readline())''' #nolasis 1 rindinu

f=open('demo.txt','r', encoding='utf8')
print(f.read(10)) # atgriez 10 simbolus, ieskaitot atstapers


f.close() #darba beigas aizver failu