import datetime
#lietotajs ievadis datumu

def iegut_datumu():
    while True:
        try:
            date_str= input('Datums: YYYY-MM-DD:')
            #parbaudit vai datums ir nakotne 
            #parvers par datetime objetu
            ievad_datums = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if ievad_datums > datetime.date.today():
                print('Lielaks par sodienu!')
            else:
                return ievad_datums
        except ValueError:
            print('nepareizs formats. Meiginiet velreiz')

iegut_datumu()

def masinas_dati():
    try:
        gads = int(input('Ievadiet gadu'))
        if(gads<2012 or gads>2022):
            print('Vajag pareizus datus!')
        else:
            print('Paldies!')
    except ValueError:
        print('Pareizus datus!')

masinas_dati()

#failam ievaito dau nosaukumu var ierakst'it:
#filename = f"{masina}_{gads}.txt"
''' def saglabat_faila(datums,temats,klase,skolenu_atz):
        filename= f"{temats}_{klase}.txt"
        #izveidos failu, parbaudis vai eksiste. Ja eksiste pielks info klat
        try:
            with open(filename,'r', encoding='UTF8') as file:
                existing_data = file.read().strip()
        expect FileNotFountError:
            existing_data""'''
        #seit jaturpina ar faila izveidi
        #if existing-data:
            #file.write
            