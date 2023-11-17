#piemērs sarkastam ar dazadiem datu tipiem

mixed = ['Suns', 7.25 , 8, True]
print (mixed[2])

#apgriezt skaitļu sarakstu
skaitli = [1,2,3,4,5,6,7,8,9,2,3,451]
apgriezt = list(reversed(skaitli))
print(apgriezt)

#filtre tikai para skaitlus
para_skaitli = [num for num in skaitli if num%2 == 0] # ja ir != 0  tad nepara skaitli
print(para_skaitli) 

#iegust saraksta garumu

videjais = sum(skaitli)/len(skaitli)
print(f'Videjais skaitlis: {videjais}')

#atrast lielako un mazako skaitli
lielakais = max(skaitli)
print(f'Lielakais skaitlis: {lielakais}')

mazakais = min(skaitli)
print(f'Mazakais skaitlis: {mazakais}')

augli = ['Abols','Mandarini','Ananass','Apelsins','Kivi']
#atrast vardus, kas sakas ar konkretu burtu
varda_sakums = [vards for vards in augli if vards.startswith('A')]
print(f'Vardi, kas sakas ar A:{varda_sakums}')