# -*- coding: UTF-8 -*-
from roboti.view.util import prikaz_menija, provera_unosa, vrednost_za_pretragu
from roboti import vrednosti
from roboti.cuvanje.upis_u_fajl import cuvanje_senzora
from roboti.vrednosti import senzor_po_oznaci, robot_po_oznaci
from roboti.model import Senzor
from roboti.view.roboti import unos_oznake_robota, prikaz_robota


def meni_senzori(): 
    '''
    Metoda koja prikazuje meni senzora
    Kupi vrednost,porverava da li je dobra vrednost i na osnovu toga poziva
    '''
    while True:
        prikaz_menija("Koju opciju zelite: ","1 - Prikaz senzora","2 - Unos senzora","3 - Izmena senzora","4 - Pretraga senzora","5 - Sortiranje senzora","6 - Prikaz robota koji imaju ugradjen odgovarajuci senzor","7 - Izlaz")
                    
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
            
        if opcija == 7:
            break
        elif opcija == 1:
            prikaz_senzora(vrednosti.senzori)
        elif opcija == 2:
            s = unos_senzora()
            vrednosti.senzori.append(s)
            cuvanje_senzora(vrednosti.senzori)
            print("Senzor uspesno kreiran {}".format(s))
        elif opcija == 3:
            senzor_oznaka = unos_oznake_senzora("Unesite oznaku senzora: ", True)
            senzor = senzor_po_oznaci(senzor_oznaka)
            izmena_senzora(senzor)
            cuvanje_senzora(vrednosti.senzori)
            print("Senzor uspesno izmenjen {}".format(senzor))
        elif opcija == 4:
            pretraga_senzora()
        elif opcija == 5:
            sortiranje_senzora()
        elif opcija == 6:
            senzor_oznaka = unos_oznake_senzora("Unesite oznaku senzora: ", True)
            senzor = senzor_po_oznaci(senzor_oznaka)
            pronadjen = pronadji_robote_za_senzor(senzor)
            prikaz_robota(pronadjen)


def prikaz_senzora(senzori):
    '''
    Formatiranje senzora
    :param senzori:
    '''
    print("{:10}|{:25}|{:10}|{:10}|{:10}|{:10}|{:16}|{:20}|{:20}|{:15}|{:10}|{:10}|".format("Oznaka", "Opis", "Duzina", "Sirina", "Visina", "Tip", "Merna jedinica", "Izmerena vrednost", "Potrosnja po merenju", "Broj merenja", "Robot", "Elektricna potrosnja"))
    for s in senzori:
        print("{:10}|{:25}|{:10}|{:10}|{:10}|{:10}|{:16}|{:20}|{:20}|{:15}|{:10}|{:10}|".format(s.oznaka, s.opis, s.duzina, s.sirina, s.visina, s.tip, s.merna_jedinica, s.izmerena_vrednost, s.potrosnja_po_merenju, s.broj_merenja, "" if s.robot is None else s.robot.oznaka, s.elektricna_potrosnja()))
        

def unos_senzora():
    '''
     Metoda za unos senzora
    '''
    print("Unos vrednosti za senzor: ")
    oznaka = unos_oznake_senzora("Oznaka: ", False)
    opis = input("Opis: ")
    duzina = provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina = provera_unosa("Sirina: ", "Sirina mora biti decimalna vrednost", float)
    visina = provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tip = input("Tip: ")
    merna_jedinica = input("Merna jedinica: ")
    izmerena_vrednost = provera_unosa("Obrtaji u minuti: ", "Izmerena vrednost mora biti decimalna vrednost", float)
    potrosnja_po_merenju = provera_unosa("Potrosnja po merenju: ", "Potrosnja po merenju mora biti decimalna vrednost", float)
    broj_merenja = provera_unosa("Broj merenja: ", "Broj merenja mora biti decimalna vrednost", float)
    robot_oznaka = unos_oznake_robota("Oznaka robota: ", True)
    robot = robot_po_oznaci(robot_oznaka)
    s = Senzor(oznaka, opis, duzina, sirina, visina, tip, merna_jedinica, izmerena_vrednost, potrosnja_po_merenju, broj_merenja, robot)
    return s


def unos_oznake_senzora(poruka, postojeca):
    '''
    Metoda za  proveru oznake senzora
    :param poruka:
    :param postojeca:
    '''
    if postojeca:
        poruka_greska = "Senzor sa oznakom ne postoji"
    else:
        poruka_greska = "Senzor sa oznakom vec postoji"
        
    while True:
        vrednost = input(poruka)
        
        if vrednost is None or vrednost == "":
            break
        else:
            senzor = senzor_po_oznaci(vrednost)
            if senzor is None and postojeca:
                print(poruka_greska)
            elif senzor is not None and not postojeca:
                print(poruka_greska)
            else:
                return vrednost


def izmena_senzora(senzor):
    '''
    Metoda za izmenu atributa senzora
    :param senzor:
    '''
    print("Unos vrednosti za senzor: ")
    oznaka = input("Oznaka: ")
    opis = input("Opis: ")
    duzina = provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina = provera_unosa("Sirina: ", "Sirina mora biti decimalna vrednost", float)
    visina = provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tip = input("Tip: ")
    merna_jedinica = input("Merna jedinica: ")
    izmerena_vrednost = provera_unosa("Izmerena vrednost: ", "Izmerena vrednost mora biti decimalna vrednost", float)
    potrosnja_po_merenju = provera_unosa("Potrosnja po merenju: ", "Potrosnja po merenju mora biti decimalna vrednost", float)
    broj_merenja = provera_unosa("Broj merenja: ", "Broj merenja mora biti decimalna vrednost", float)
    robot_oznaka = unos_oznake_robota("Oznaka robota: ", True)
    robot = robot_po_oznaci(robot_oznaka)
    senzor.oznaka = oznaka
    senzor.opis = opis
    senzor.duzina = duzina
    senzor.sirina = sirina
    senzor.visina = visina
    senzor.tip = tip
    senzor.merna_jedinica = merna_jedinica
    senzor.izmerena_vrednost = izmerena_vrednost
    senzor.potrosnja_po_merenju = potrosnja_po_merenju
    senzor.broj_merenja = broj_merenja
    senzor.robot = robot


def pretraga_senzora():
    '''
    Meni za pretragu senzora
    '''
    while True:
        prikaz_menija("Pretraga senzora: ","1 - po oznaci","2 - po opisu","3 - po duzini","4 - po sirini","5 - po visini","6 - po tipu","7 - po mernoj jedinici","8 - po izmerenoj vrednosti","9 - po potrosnji po merenju","10 - po broju merenja","11 - Izlaz")

        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 11:
            break
        elif opcija == 1:
            oznaka = input("Unesite oznaku za pretragu: ")
            print();
            pronadjeni = pretraga_po_oznaci(oznaka)
            prikaz_senzora(pronadjeni)
        elif opcija == 2:
            opis = input("Unesite opis za pretragu: ")
            print();
            pronadjeni = pretraga_po_opisu(opis)
            prikaz_senzora(pronadjeni)
        elif opcija == 3:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost duzine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost duzine za pretragu:", float)
            print();
            pronadjeni = pretraga_po_duzini(minimalna, maksimalna)
            prikaz_senzora(pronadjeni) 
        elif opcija == 4:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost sirine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost sirine za pretragu:", float)            
            print();
            pronadjeni = pretraga_po_sirini(minimalna, maksimalna)
            prikaz_senzora(pronadjeni) 
        elif opcija == 5:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost visine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost visine za pretragu:", float) 
            print();
            pronadjeni = pretraga_po_visini(minimalna, maksimalna)
            prikaz_senzora(pronadjeni) 
        elif opcija == 6:
            tip = input("Unesite tip za pretragu: ")
            print();
            pronadjeni = pretraga_po_tipu(tip)
            prikaz_senzora(pronadjeni)
        elif opcija == 7:
            merna_jedinica = input("Unesite mernu jedinicu za pretragu: ")
            print();
            pronadjeni = pretraga_po_mernoj_jedinici(merna_jedinica)
            prikaz_senzora(pronadjeni) 
        elif opcija == 8:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost izmerene vrednosti za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost izmerene vrednosti za pretragu:", float)
            print();
            pronadjeni = pretraga_po_izmerenoj_vrednosti(minimalna, maksimalna)
            prikaz_senzora(pronadjeni) 
        elif opcija == 9:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost potrosnje po merenju za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost potrosnje po merenju za pretragu:", float)
            print();
            pronadjeni = pretraga_po_potrosnji_po_merenju(minimalna, maksimalna)
            prikaz_senzora(pronadjeni) 
        elif opcija == 10:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost broja merenja za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost broja merenja za pretragu:", float)
            print();
            pronadjeni = pretraga_po_broju_merenja(minimalna, maksimalna)
            prikaz_senzora(pronadjeni) 


def pretraga_po_oznaci(oznaka):
    '''
    Metoda za pretragu senzora po oznaci
    :param oznaka:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if oznaka in s.oznaka:
            pronadjeni.append(s)
    return pronadjeni


def pretraga_po_opisu(opis):
    '''
    Metoda za pretragu senzora po opisu
    :param opis:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if opis in s.opis:
            pronadjeni.append(s)
    return pronadjeni


def pretraga_po_duzini(minimalna, maksimalna):
    '''
    Metoda za pretragu senzora po duzini
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.duzina < minimalna:
                continue
        if maksimalna is not None:
            if s.duzina > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def pretraga_po_sirini(minimalna, maksimalna):
    '''
    Metoda za pretragu senzora po sirini
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.sirina < minimalna:
                continue
        if maksimalna is not None:
            if s.sirina > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def pretraga_po_visini(minimalna, maksimalna):
    '''
    Motoda za pretragu senzora po visini
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.visina < minimalna:
                continue
        if maksimalna is not None:
            if s.visina > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def pretraga_po_tipu(tip):
    '''
    Pretraga po tipu senzora
    :param tip:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if tip in s.tip:
            pronadjeni.append(s)
    return pronadjeni


def pretraga_po_mernoj_jedinici(merna_jedinica):
    '''
    Pretraga po mernoj jedinici senzora
    :param merna_jedinica:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if merna_jedinica in s.merna_jedinica:
            pronadjeni.append(s)
    return pronadjeni


def pretraga_po_izmerenoj_vrednosti(minimalna, maksimalna):
    '''
    Trazi unos minimalne i maksimalni i izmedju tih vrednosti prikazuje pronadjene
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.izmerena_vrednost < minimalna:
                continue
        if maksimalna is not None:
            if s.izmerena_vrednost > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def pretraga_po_broju_merenja(minimalna, maksimalna):
    '''
    Trazi unos minimalne i maksimalni vrednosti merenja i izmedju tih vrednosti prikazuje pronadjene
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.broj_merenja < minimalna:
                continue
        if maksimalna is not None:
            if s.broj_merenja > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def pretraga_po_potrosnji_po_merenju(minimalna, maksimalna):
    '''
    Trazi unos minimalne i maksimalne i izmedju tih vrednosti prikazuje pronadjene
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.potrosnja_po_merenju < minimalna:
                continue
        if maksimalna is not None:
            if s.potrosnja_po_merenju > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def pretraga_po_vremenu_rada(minimalna, maksimalna):
    '''
    Trazi unos minimalne i maksimalne vrednosti rada i izmedju tih vrednosti prikazuje pronadjene
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if minimalna is not None:
            if s.vreme_rada < minimalna:
                continue
        if maksimalna is not None:
            if s.vreme_rada > maksimalna:
                continue
        pronadjeni.append(s)
    return pronadjeni


def sortiranje_senzora():
    '''
    Sortiranje senzora po opciji
    '''
    while True:
        prikaz_menija("Sortiranje senzora: ","1 - po mernoj jedinici","2 - po broju merenja","3 - Izlaz")
        
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 3:
            break
        elif opcija == 1:
            sortirani = sortiranje_po_mernoj_jedinici(vrednosti.senzori)
            prikaz_senzora(sortirani)
        elif opcija == 2:
            sortirani = sortiranje_po_broju_merenja(vrednosti.senzori)
            prikaz_senzora(sortirani)


def sortiranje_po_mernoj_jedinici(senzori):
    '''
    Soritranj po mernoj jedini senzora
    :param senzori:
    '''
    sortirani = []
    sortirani.extend(senzori)
    sortirani.sort(key=lambda x:x.merna_jedinica, reverse=False)
    return sortirani


def sortiranje_po_broju_merenja(okviri):
    '''
    Soriranje po broju merenja
    :param okviri:
    '''
    sortirani = []
    sortirani.extend(okviri)
    sortirani.sort(key=lambda x:x.broj_merenja, reverse=False)
    return sortirani


def pronadji_robote_za_senzor(senzor):
    '''
    Trazi robote po oznaci senzora
    :param senzor:
    '''
    pronadjeni = []
    for s in vrednosti.senzori:
        if s.oznaka ==  senzor.oznaka:
            pronadjeni.append(s.robot)
    return pronadjeni
 
           
if __name__ == '__main__':
    pass