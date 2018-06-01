# -*- coding: UTF-8 -*-
from roboti.view.util import prikaz_menija, provera_unosa, vrednost_za_pretragu
from roboti import vrednosti
from roboti.cuvanje.upis_u_fajl import cuvanje_okvira
from roboti.vrednosti import okvir_po_oznaci, robot_po_oznaci
from roboti.model import Okvir
from roboti.view.roboti import unos_oznake_robota, prikaz_robota


def meni_okviri(): 
    '''
    Ovo je metoda za prikaz metoda okvira
    Kupi vrednost,porverava da li je dobra vrednost i na osnovu toga poziva
    '''
    while True:
        prikaz_menija("Koju opciju zelite: ","1 - Prikaz okvira","2 - Unos okvira","3 - Izmena okvira","4 - Pretraga okvira","5 - Sortiranje okvira","6 - Prikaz robota za koje je iskoriscen odgovarajuci okvir","7 - Izlaz")
                    
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
            
        if opcija == 7:
            break
        elif opcija == 1:
            prikaz_okvira(vrednosti.okviri)
        elif opcija == 2:
            o = unos_okvira()
            vrednosti.okviri.append(o)
            cuvanje_okvira(vrednosti.okviri)
            print("Okvir uspesno kreiran {}".format(o))
        elif opcija == 3:
            okvir_oznaka = unos_oznake_okvira("Unesite oznaku okvira: ", True)
            okvir = okvir_po_oznaci(okvir_oznaka)
            izmena_okvira(okvir)
            cuvanje_okvira(vrednosti.okviri)
            print("Okvir uspesno izmenjen {}".format(okvir))
        elif opcija == 4:
            pretraga_okvira()
        elif opcija == 5:
            sortiranje_okvira()
        elif opcija == 6:
            okvir_oznaka = unos_oznake_okvira("Unesite oznaku okvira: ", True)
            okvir = okvir_po_oznaci(okvir_oznaka)
            pronadjen = pronadji_robote_za_okvir(okvir)
            prikaz_robota(pronadjen)

           
def prikaz_okvira(okviri):
    '''
    Formatiranje okvira
    :param okviri:
    '''
    print("{:10}|{:30}|{:10}|{:10}|{:10}|{:10}|{:20}|{:10}|".format("Oznaka", "Opis", "Duzina", "Sirina", "Visina", "Tezina", "Tip Materijala", "Robot"))
    for o in okviri:
        print("{:10}|{:30}|{:10}|{:10}|{:10}|{:10}|{:20}|{:10}|".format(o.oznaka, o.opis, o.duzina, o.sirina, o.visina, o.tezina, o.tip_materijala, "" if o.robot is None else o.robot.oznaka))
        

def unos_okvira():
    '''
    Metoda za unos atributa okvira
    '''
    print("Unos vrednosti za okvir: ")
    oznaka = unos_oznake_okvira("Oznaka: ", False)
    opis = input("Opis: ")
    duzina = provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina = provera_unosa("Sirina: ", "Sirina mora biti decimalna vrednost", float)
    visina = provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tezina = provera_unosa("Tezina: ", "Tezina mora biti decimalna vrednost", float)
    tip_materijala = input("Tip materijala: ")
    robot_oznaka = unos_oznake_robota("Oznaka robota: ", True)
    robot = robot_po_oznaci(robot_oznaka)
    o = Okvir(oznaka, opis, duzina, sirina, visina, tezina, tip_materijala, robot)
    return o


def unos_oznake_okvira(poruka, postojeca):
    '''
    Provera unosa oznake okvira
    :param poruka:
    :param postojeca:
    '''
    if postojeca:
        poruka_greska = "Okvir sa oznakom ne postoji"
    else:
        poruka_greska = "Okvir sa oznakom vec postoji"
        
    while True:
        vrednost = input(poruka)
        
        if vrednost is None or vrednost == "":
            break
        else:
            okvir = okvir_po_oznaci(vrednost)
            if okvir is None and postojeca:
                print(poruka_greska)
            elif okvir is not None and not postojeca:
                print(poruka_greska)
            else:
                return vrednost


def izmena_okvira(okvir):
    '''
    Izmena vrednosti okvira
    :param okvir:
    '''
    print("Unos vrednosti za okvir: ")
    oznaka = input("Oznaka: ")
    opis = input("Opis: ")
    duzina = provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina = provera_unosa("Sirina: ", "Sirina mora biti decimalna vrednost", float)
    visina = provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tezina = provera_unosa("Tezina: ", "Tezina mora biti decimalna vrednost", float)
    tip_materijala = input("Tip materijala: ")
    robot_oznaka = unos_oznake_robota("Oznaka robota: ", True)
    robot = robot_po_oznaci(robot_oznaka)
    okvir.oznaka = oznaka
    okvir.opis = opis
    okvir.duzina = duzina
    okvir.sirina = sirina
    okvir.visina = visina
    okvir.tezina = tezina
    okvir.tip_materijala = tip_materijala
    okvir.robot = robot


def pretraga_okvira():
    '''
    Meni za pretragu okvira
    '''
    while True:
        prikaz_menija("Pretraga okvira: ","1 - po oznaci","2 - po opisu","3 - po duzini","4 - po sirini","5 - po visini","6 - po tezini","7 - po tipu materijala","8 - Izlaz")

        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 8:
            break
        elif opcija == 1:
            oznaka = input("Unesite oznaku za pretragu: ")
            print();
            pronadjeni = pretraga_po_oznaci(oznaka)
            prikaz_okvira(pronadjeni)
        elif opcija == 2:
            opis = input("Unesite opis za pretragu: ")
            print();
            pronadjeni = pretraga_po_opisu(opis)
            prikaz_okvira(pronadjeni)
        elif opcija == 3:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost duzine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost duzine za pretragu:", float)
            print();
            pronadjeni = pretraga_po_duzini(minimalna, maksimalna)
            prikaz_okvira(pronadjeni) 
        elif opcija == 4:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost sirine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost sirine za pretragu:", float)            
            print();
            pronadjeni = pretraga_po_sirini(minimalna, maksimalna)
            prikaz_okvira(pronadjeni) 
        elif opcija == 5:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost visine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost visine za pretragu:", float) 
            print();
            pronadjeni = pretraga_po_visini(minimalna, maksimalna)
            prikaz_okvira(pronadjeni) 
        elif opcija == 6:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost tezine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost tezine za pretragu:", float)
            print();
            pronadjeni = pretraga_po_tezini(minimalna, maksimalna)
            prikaz_okvira(pronadjeni) 
        elif opcija == 7:
            tip_materijala = input("Unesite tip materijala za pretragu: ")
            print();
            pronadjeni = pretraga_po_tipu_materijala(tip_materijala)
            prikaz_okvira(pronadjeni) 


def pretraga_po_oznaci(oznaka):
    '''
    Metoda za pretragu po oznaci
    :param oznaka:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if oznaka in o.oznaka:
            pronadjeni.append(o)
    return pronadjeni


def pretraga_po_opisu(opis):
    '''
    Metoda za pretragu po opisu
    :param opis:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if opis in o.opis:
            pronadjeni.append(o)
    return pronadjeni


def pretraga_po_duzini(minimalna, maksimalna):
    '''
    Pretraga po dozini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if minimalna is not None:
            if o.duzina < minimalna:
                continue
        if maksimalna is not None:
            if o.duzina > maksimalna:
                continue
        pronadjeni.append(o)
    return pronadjeni


def pretraga_po_sirini(minimalna, maksimalna):
    '''
    Pretraga po sirini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if minimalna is not None:
            if o.sirina < minimalna:
                continue
        if maksimalna is not None:
            if o.sirina > maksimalna:
                continue
        pronadjeni.append(o)
    return pronadjeni


def pretraga_po_visini(minimalna, maksimalna):
    '''
    Pretraga po visini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if minimalna is not None:
            if o.visina < minimalna:
                continue
        if maksimalna is not None:
            if o.visina > maksimalna:
                continue
        pronadjeni.append(o)
    return pronadjeni


def pretraga_po_tezini(minimalna, maksimalna):
    '''
    Pretraga po tezini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if minimalna is not None:
            if o.tezina < minimalna:
                continue
        if maksimalna is not None:
            if o.tezina > maksimalna:
                continue
        pronadjeni.append(o)
    return pronadjeni


def pretraga_po_tipu_materijala(tip_materijala):
    '''
    Pretraga  po tipu materijala
    :param tip_materijala:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if tip_materijala in o.tip_materijala:
            pronadjeni.append(o)
    return pronadjeni


def sortiranje_okvira():
    '''
    Sortiranje okvira po tezini
    '''
    while True:
        prikaz_menija("Sortiranje okvira: ","1 - po tezini","2 - Izlaz")
        
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 2:
            break
        elif opcija == 1:
            sortirani = sortiranje_po_tezini(vrednosti.okviri)
            prikaz_okvira(sortirani)


def sortiranje_po_tezini(okviri):
    '''
    Sortiranje okvira po tezini
    :param okviri:
    '''
    sortirani = []
    sortirani.extend(okviri)
    sortirani.sort(key=lambda x:x.tezina, reverse=False)
    return sortirani


def pronadji_robote_za_okvir(okvir):
    '''
    Metoda koja vraca pretrazene robote po okviru
    :param okvir:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if o.oznaka ==  okvir.oznaka:
            pronadjeni.append(o.robot)
    return pronadjeni


if __name__ == '__main__':
    pass