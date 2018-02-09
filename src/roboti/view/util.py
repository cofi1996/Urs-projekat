# -*- coding: UTF-8 -*-
def prikaz_menija(*meni_opcije):
    '''
    Provera opcije unosa za meni
    '''
    for i in range(3):
        print()
    for i in meni_opcije:
        print(i)


def unos_stringa(poruka, poruka_greska):
    '''
    Provera da li je oznaka dobro uneta
    :param poruka:
    :param poruka_greska:
    '''
    while True:
        vrednost = input(poruka)
        if vrednost is None or vrednost == "":
            print(poruka_greska)
        else:
            return vrednost
     

def unos_boolean(poruka, poruka_greska):
    '''
    Provera da li je oznaka dobro uneta
    :param poruka:
    :param poruka_greska:
    '''
    while True:
        vrednost = input(poruka+"[d/n]:")
        if vrednost is None or vrednost == "":
            print(poruka_greska)
        else:
            b = True if vrednost == "d" else False
            return b
    
def provera_unosa(poruka, poruka_greska, convert):
    '''
    Provera tipa 
    :param poruka:
    :param poruka_greska:
    :param convert:
    '''
    while True:
        try:
            return convert(input(poruka))
        except:
            print(poruka_greska)
            
        
def vrednost_za_pretragu(poruka,convert):
    '''
    Provera vrednosti pretrage
    :param poruka:
    :param convert:
    '''
    try:
        return convert(input(poruka))
    except:
        return None