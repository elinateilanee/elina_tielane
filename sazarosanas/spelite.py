import random
# akmens, skeres, papirs
gajieni = ['akmens','papirs','skeres'] # saraksts
while True:
    cilveka_gajiens = input('Ievadi savu gajienu:')
    datora_gajiens = random.choice(gajieni)
    print('Cilvēks:',cilveka_gajiens,'vs Dators:',datora_gajiens)
    if cilveka_gajiens == datora_gajiens: #== nozime salidzinasana
        print('Neizskirts')
    elif cilveka_gajiens == 'akmens'and datora_gajiens == 'skeres':
        print('Čilveks uzvar!')
    elif cilveka_gajiens == 'skeres'and datora_gajiens == 'papirs':
        print('Čilveks uzvar!')
    elif cilveka_gajiens == 'papirs'and datora_gajiens == 'akmens':
        print('Čilveks uzvar!')
    else:
        print('Dators uzvar!')
