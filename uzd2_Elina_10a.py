decembris = {
    '1decembris',
    '2decembris',
    '3decembris',
    '4decembris',
    '5decembris',
    '6decembris',
    '7decembris'}
temperetura = {
    -2,
    1,
    0,
    -3,
    -5,
    -6,
    3}
datums = input('Ievadiet datumu piem. šadi (1decembris):') 
kopejs= dict.fromkeys(decembris,temperetura) # savieno abas vārdnīcas vienā
if datums in decembris: #pārbauda vai lietotāja inputs ir vārdnīcā
    print(datums,'tempretūra Clesija skalā ir:',kopejs[decembris[temperetura]],' grādi') 
print('*****')
f =  kopejs[decembris[temperetura]]*(9/5)+32 # pārveido c uz f 
print(datums,'tempretūra Fārenheita skalā ir:',f,' grādi')

'''datums = range(5)
for datums in 5
:
  print(datums)
if datums> 5:
  exit()


val = 0 #si vertiba bus visai vardnicai
dd = dict.fromkeys(kk,val)
print(dd)

vardnica[ievade_atsl] = ievadiet_vert
'''


