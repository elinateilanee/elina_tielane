#f-ja kas nosaka vecuma statusu atkariba no ievaditajiem datiem
def parbaudit_vecumu(vecums):
    if vecums<18:
        print('Tu esi nepilngadīgs')
    elif vecums >=18 and vecums <65:
        print('Tu esi pilngadīgs')
    else:
        print('Tu esi seniors')
lietotajavecums= float(input('Īevadiet vecumu: '))
parbaudit_vecumu(lietotajavecums)