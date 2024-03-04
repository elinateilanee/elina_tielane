import csv
#uzrakstit program. kas strukture datus no 1 faila atjaunina un ieraksta jaunafail.
saktonejiedati = 'sakotnejiedati.csv'
redigetiedati = 'redigetie_dati.csv'

#meigniam atvert sajotnejo failu
try:
    with open(saktonejiedati,'r',encoding='utf8') as sakotnejiedati:
        lasitajs = csv.DictReader(sakotnejiedati)
        sakotnejiedati = list(lasitajs)
    #atjauno datus
        for persona in sakotnejiedati:
            persona['vecums']= int(persona['vecums'])+1 #palielinas vecums par 1 gadu
    #ieraksta datus jauna faila
    with open(saktonejiedati,'w', encoding='utf8') as redigetiedati:
        rakstitajs = csv.DictWriter(redigetiedati, fieldnames=['vards', 'uzvards', 'vecums'])
        rakstitajs.writeheader()
        rakstitajs.writerows(sakotnejiedati)
    print(f'Dati it atjunati un saglabati faila'{redigetie_dati}'nav atrasts.')

except FileNotFoundError:
    print(f'Kluda: Fails'{saktonejiedati}'nav atrasts.')
except Exception as e:
    print(f'Kluda:Neparedzeta kluda = {e}' )