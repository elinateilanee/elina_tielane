def noteiktizklitibu(gadi_skola,gadi_darbā,diploms):
    if diploms=='bakalors' and gadi_skola>=4 and gadi_darbā>=2:
        print('Tev ir augsta izgl. un darba pieredze')
    elif diploms=='magistrs' and gadi_skola>=6 and gadi_darbā>=4:
        print('Tava un darba pagaza patiks darba devejam')
    else:
        print('Ieteicams uzkrāt pieredzi')

#lietotaja datu ievade
darbaagadi = float(input('Īevadiet cik gadus darba stardajat: '))
skolasgadi = float(input('Īevadiet cik gadus macijaties: '))
iglitibalimenis = input('Kads ir tavs izfl. limenis?: ')
noteiktizklitibu(darbaagadi,skolasgadi,iglitibalimenis)