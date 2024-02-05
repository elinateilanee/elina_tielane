'''def fun(x,y): #padodi divi parametri x un y
    #talak raksa ko funkcija dara
    z = 2*(x+y) # apreikina izteiksmi
    return z #atgriez rezultatu

print('Programma sakas')
a = 7
rez=fun(a,2+a)
print('Funkcijas rezultats', rez)

a = 6 #aiziet ka x
b = 2 #aiziet ka y
rez2 = fun(a,b)
print('fUNKCIJAS Rezultats', rez2)'''

print('Kods ar funkcijam')
def tuksasrindas(): #funkkcija bez parametireem, izdruka tuksu rindu
    print('\n')

def zvaigznes():
    print('***')

def sveiks(vards):
    print('Sveiks,' , vards)
print('Programma sākas')

def virskarsts ():
    print('Skaisti')

while True:
    sveiks('Pēteri!') # padod f-ja argumentu
    zvaigznes()
    tuksasrindas()
    sveiks('Jāni!')
    virskarsts()
    
    skaitli = int(input('Ievadi skaitli'))

    
    vai_turpinat = input('Vai turpināt')
    
    if vai_turpinat == 'j':
        continue
    else:
        zvaigznes()
        exit()