nenodots = input('Vai Jums ir kāds nenodots izdevums? j/n:')
if nenodots == 'j':
    print('Jūs nedrīkstat neko izņemt')
elif nenodots == 'n':
    pieprasits=input('Vai ši publikācija ir pieprasīta? (j/n)')
    if pieprasits == 'j':
        print('Īzniedz uz 2 dienam')
    elif pieprasits == 'n':
        zurnals = input('Vai publikācija ir žurnāls?')
        if zurnals == 'j':
            print('Izniegs uz 7 dineām')
        elif zurnals == 'n':
            studetns= input('Vai jus esat students?(j/n)')
            if studetns == 'j':
                print('Izniedz uz 14 dienam')
            elif studetns == 'n':
                print('Izniedz uz 28 dienam')