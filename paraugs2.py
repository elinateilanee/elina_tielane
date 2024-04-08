''''laut ievadit tekstu, ierakstit to faila
'teksta_fails.txt' Ievadit skaitli, papildinat
failu ar so skaitli, katru rindu sakot ar 
'Papildus rindas nr'''

def ierakstit_faila():
    teksts = input('Ievadiet teikumu: ')

    with open("teksta_fails.txt",'w', encoding='utf8') as file:
        file.write(teksts)

def papildus_skaitlis():
    skaitlis=int(input('Ievadiet vesalus skaitlus: '))
    
    #a rezims update datus
    with open("teksta_fails.txt",'a', encoding='utf8') as file:
        for i in range(skaitlis):
            file.write(f"\nPapildus rinda nr. {i+1}")

ierakstit_faila()  
papildus_skaitlis()
