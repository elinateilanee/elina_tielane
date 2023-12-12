skolenuaugumi = {
    'Emils' : 172,
    'Zane' : 185,
    'Katrina' : 164,
    'Gunars' : 184,
    'Enija' : 162,
    'Ilze' : 164,
    'Janis' : 165,
    'Ramona' : 167,
    'Agija' : 177,
    'Daniels' : 184,
    'Markus' : 165,
    'Inara' : 180
} 


for key in skolenuaugumi:
    print(key, ':', skolenuaugumi[key]) # izprinte vardincu stabiņā

print("😍😎😋😋😊😉")
jautajums = input('Vai Jūs vēlaties pievienot jaunu skolēnu? (j/n)')
while jautajums == 'j':
    jaunsskolenavards = input('Kads bus skolēna vārds?')
    jaunsskolenagarums = input('Kads bus skolēna garums?') 

    skolenuaugumi[jaunsskolenavards] = jaunsskolenagarums # pievieno jaunu skolēnu
    print('Jauns paris tika pievienots vardnicai')
    for key in skolenuaugumi:
        print(key, ':', skolenuaugumi[key])
    jautajums = input('Vai Jūs vēlaties pievienot jaunu skolēnu? (j/n)')
while jautajums == 'n':
    for key in skolenuaugumi:
        print(key, ':', skolenuaugumi[key])
    print("😍😎😋😋😊😉")
    izdzestdatus = input('Vai Jūs vēlaties izdzēst datus?(j/n)')
    if izdzestdatus == 'j':
        kurudzest = input('Kuru skolēnu Jūs gribat izdzēst? (vārdu)')
        pop = skolenuaugumi.pop(kurudzest)  #idzēš kaut kādu norādīto key(vārdu)
    for key in skolenuaugumi:
            print(key, ':', skolenuaugumi[key])
    if izdzestdatus == 'n':
        beigtprogrammu = input('Vai Jūs vēlaties beigt programmu?(ievadiet exit)')
        beigtprogrammu == 'exit'
        exit() # beidz programmu