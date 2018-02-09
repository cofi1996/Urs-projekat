# -*- coding: UTF-8 -*-
from roboti.view.util import prikaz_menija, provera_unosa, vrednost_za_pretragu
from roboti import vrednosti
from roboti.cuvanje.upis_u_fajl import cuvanje_motora
from roboti.vrednosti import motor_po_oznaci, robot_po_oznaci
from roboti.model import Motor
from roboti.view.roboti import unos_oznake_robota, prikaz_robota


def meni_motori(): 
    '''
    Ovo je metoda za prikaz metoda motora
    Kupi vrednost,porverava da li je dobra vrednost i na osnovu toga poziva
    '''
    while True:
        prikaz_menija("Koju opciju zelite: ","1 - Prikaz motora","2 - Unos motora","3 - Izmena motora","4 - Pretraga motora","5 - Sortiranje motora","6 - Prikaz robota koji imaju ugradjen odgovarajuci motor","7 - Izlaz")
                    
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
            
        if opcija == 7:
            break
        elif opcija == 1:
            prikaz_motora(vrednosti.motori)
        elif opcija == 2:
            m = unos_motora()
            vrednosti.motori.append(m)
            cuvanje_motora(vrednosti.motori)
            print("Motor uspesno kreiran {}".format(m))
        elif opcija == 3:
            motor_oznaka = unos_oznake_motora("Unesite oznaku motora: ", True)
            motor = motor_po_oznaci(motor_oznaka)
            izmena_motora(motor)
            cuvanje_motora(vrednosti.motori)
            print("Motor uspesno izmenjen {}".format(motor))
        elif opcija == 4:
            pretraga_motora()
        elif opcija == 5:
            sortiranje_motora()
        elif opcija == 6:
            motor_oznaka = unos_oznake_motora("Unesite oznaku motora: ", True)
            motor = motor_po_oznaci(motor_oznaka)
            pronadjen = pronadji_robote_za_motor(motor)
            prikaz_robota(pronadjen)


def prikaz_motora(motori):
    '''
    Formatiranje motora
    :param motori:
    '''
    print("{:10}|{:25}|{:10}|{:10}|{:10}|{:10}|{:16}|{:20}|{:20}|{:10}|{:10}|".format("Oznaka", "Opis", "Duzina", "Sirina", "Visina", "Tezina", "Vreme rada", "Obrtaji u minuti", "Potrosnja po obrtaju", "Robot", "Elektricna potrosnja"))
    for m in motori:
        print("{:10}|{:25}|{:10}|{:10}|{:10}|{:10}|{:16}|{:20}|{:20}|{:10}|{:10}|".format(m.oznaka, m.opis, m.duzina, m.sirina, m.visina, m.tezina, m.vreme_rada, m.obrtaja_u_minuti, m.potrosnja_po_obrtaju, "" if m.robot is None else m.robot.oznaka, m.elektricna_potrosnja()))
        

def unos_motora():
    '''
    Metoda za unos atributa motora
    '''
    print("Unos vrednosti za motor: ")
    oznaka = unos_oznake_motora("Oznaka: ", False)
    opis = input("Opis: ")
    duzina = provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina = provera_unosa("Sirina: ", "Sirina mora biti decimalna vrednost", float)
    visina = provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tezina = provera_unosa("Tezina: ", "Tezina mora biti decimalna vrednost", float)
    vreme_rada = provera_unosa("Vreme rada: ", "Vreme rada mora biti celobrojna vrednost", int)
    obrtaja_u_minuti = provera_unosa("Obrtaji u minuti: ", "Obrtaji u minuti moraju biti decimalna vrednost", float)
    potrosnja_po_obrtaju = provera_unosa("Potrosnja po obrtaju: ", "Potrosnja po obrtaju mora biti decimalna vrednost", float)
    robot_oznaka = unos_oznake_robota("Oznaka robota: ", True)
    robot = robot_po_oznaci(robot_oznaka)
    m = Motor(oznaka, opis, duzina, sirina, visina, tezina, vreme_rada, obrtaja_u_minuti, potrosnja_po_obrtaju, robot)
    return m


def unos_oznake_motora(poruka, postojeca):
    '''
    Provera unosa oznake motora
    :param poruka:
    :param postojeca:
    '''
    if postojeca:
        poruka_greska = "Motor sa oznakom ne postoji"
    else:
        poruka_greska = "Motor sa oznakom vec postoji"
        
    while True:
        vrednost = input(poruka)
        
        if vrednost is None or vrednost == "":
            break
        else:
            motor = motor_po_oznaci(vrednost)
            if motor is None and postojeca:
                print(poruka_greska)
            elif motor is not None and not postojeca:
                print(poruka_greska)
            else:
                return vrednost


def izmena_motora(motor):
    '''
    Izmena vrednosti motora
    :param motor:
    '''
    print("Unos vrednosti za motor: ")
    oznaka = input("Oznaka: ")
    opis = input("Opis: ")
    duzina = provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina = provera_unosa("Sirina: ", "Sirina mora biti decimalna vrednost", float)
    visina = provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tezina = provera_unosa("Tezina: ", "Tezina mora biti decimalna vrednost", float)
    vreme_rada = provera_unosa("Vreme rada: ", "Vreme rada mora biti celobrojna vrednost", int)
    obrtaja_u_minuti = provera_unosa("Obrtaji u minuti: ", "Obrtaji u minuti moraju biti decimalna vrednost", float)
    potrosnja_po_obrtaju = provera_unosa("Potrosnja po obrtaju: ", "Potrosnja po obrtaju mora biti decimalna vrednost", float)
    robot_oznaka = unos_oznake_robota("Oznaka robota: ", True)
    robot = robot_po_oznaci(robot_oznaka)
    motor.oznaka = oznaka
    motor.opis = opis
    motor.duzina = duzina
    motor.sirina = sirina
    motor.visina = visina
    motor.tezina = tezina
    motor.vreme_rada = vreme_rada
    motor.obrtaja_u_minuti = obrtaja_u_minuti
    motor.potrosnja_po_obrtaju = potrosnja_po_obrtaju
    motor.robot = robot


def pretraga_motora():
    '''
    Meni za pretragu motora
    '''
    while True:
        prikaz_menija("Pretraga motora: ","1 - po oznaci","2 - po opisu","3 - po duzini","4 - po sirini","5 - po visini","6 - po tezini","7 - po vremenu rada","8 - po obrtajima u minuti","9 - po potrosnji po obrtaju","10 - Izlaz")

        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 10:
            break
        elif opcija == 1:
            oznaka = input("Unesite oznaku za pretragu: ")
            print();
            pronadjeni = pretraga_po_oznaci(oznaka)
            prikaz_motora(pronadjeni)
        elif opcija == 2:
            opis = input("Unesite opis za pretragu: ")
            print();
            pronadjeni = pretraga_po_opisu(opis)
            prikaz_motora(pronadjeni)
        elif opcija == 3:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost duzine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost duzine za pretragu:", float)
            print();
            pronadjeni = pretraga_po_duzini(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 
        elif opcija == 4:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost sirine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost sirine za pretragu:", float)            
            print();
            pronadjeni = pretraga_po_sirini(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 
        elif opcija == 5:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost visine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost visine za pretragu:", float) 
            print();
            pronadjeni = pretraga_po_visini(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 
        elif opcija == 6:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost tezine za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost tezine za pretragu:", float)
            print();
            pronadjeni = pretraga_po_tezini(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 
        elif opcija == 7:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost vremena rada za pretragu:", int)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost vremena rada za pretragu:", int)
            print();
            pronadjeni = pretraga_po_vremenu_rada(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 
        elif opcija == 8:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost obrtaja u minuti za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost obrtaja u minuti za pretragu:", float)
            print();
            pronadjeni = pretraga_po_obrtajima_u_minuti(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 
        elif opcija == 9:
            minimalna = vrednost_za_pretragu("Unesite minimalnu vrednost potrosnje po obrtaju za pretragu:", float)
            maksimalna = vrednost_za_pretragu("Unesite maksimalnu vrednost potrosnje po obrtaju za pretragu:", float)
            print();
            pronadjeni = pretraga_po_potrosnji_po_obrtaju(minimalna, maksimalna)
            prikaz_motora(pronadjeni) 


def pretraga_po_oznaci(oznaka):
    '''
    Metoda za pretragu po oznaci
    :param oznaka:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if oznaka in m.oznaka:
            pronadjeni.append(m)
    return pronadjeni


def pretraga_po_opisu(opis):
    '''
    Metoda za pretragu po opisu
    :param opis:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if opis in m.opis:
            pronadjeni.append(m)
    return pronadjeni


def pretraga_po_duzini(minimalna, maksimalna):
    '''
    Metoda za pretragu po duzini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.duzina < minimalna:
                continue
        if maksimalna is not None:
            if m.duzina > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def pretraga_po_sirini(minimalna, maksimalna):
    '''
    Metoda za pretragu po sirini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.sirina < minimalna:
                continue
        if maksimalna is not None:
            if m.sirina > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def pretraga_po_visini(minimalna, maksimalna):
    '''
    Metoda za pretragu po visini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.visina < minimalna:
                continue
        if maksimalna is not None:
            if m.visina > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def pretraga_po_tezini(minimalna, maksimalna):
    '''
    Pretra po tezini u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.tezina < minimalna:
                continue
        if maksimalna is not None:
            if m.tezina > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def pretraga_po_vremenu_rada(minimalna, maksimalna):
    '''
    Pretraga po vremenu u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.vreme_rada < minimalna:
                continue
        if maksimalna is not None:
            if m.vreme_rada > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def pretraga_po_obrtajima_u_minuti(minimalna, maksimalna):
    '''
    Pretraga po obrtajima u minuti u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.obrtaja_u_minuti < minimalna:
                continue
        if maksimalna is not None:
            if m.obrtaja_u_minuti > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def pretraga_po_potrosnji_po_obrtaju(minimalna, maksimalna):
    '''
    Pretraga po potrosnji u opsegu
    :param minimalna:
    :param maksimalna:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if minimalna is not None:
            if m.potrosnja_po_obrtaju < minimalna:
                continue
        if maksimalna is not None:
            if m.potrosnja_po_obrtaju > maksimalna:
                continue
        pronadjeni.append(m)
    return pronadjeni


def sortiranje_motora():
    '''
    Sortiranje motora po opciji
    '''
    while True:
        prikaz_menija("Sortiranje motora: ","1 - po tezini","2 - po elektricnoj potrosnji","3 - Izlaz")
        
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 3:
            break
        elif opcija == 1:
            sortirani = sortiranje_po_tezini(vrednosti.motori)
            prikaz_motora(sortirani)
        elif opcija == 2:
            sortirani = sortiranje_po_potrosnji(vrednosti.motori)
            prikaz_motora(sortirani)


def sortiranje_po_tezini(motori):
    '''
    Sortiranje motora po tezini
    :param motori:
    '''
    sortirani = []
    sortirani.extend(motori)
    sortirani.sort(key=lambda x:x.tezina, reverse=False)
    return sortirani


def sortiranje_po_potrosnji(okviri):
    '''
    Sortiranje okvira po potrosnji
    :param okviri:
    '''
    sortirani = []
    sortirani.extend(okviri)
    sortirani.sort(key=lambda x:x.elektricna_potrosnja(), reverse=False)
    return sortirani


def pronadji_robote_za_motor(motor):
    '''
    Pretrazuje robote po motoru
    :param motor:
    '''
    pronadjeni = []
    for m in vrednosti.motori:
        if m.oznaka ==  motor.oznaka:
            pronadjeni.append(m.robot)
    return pronadjeni
 
           
if __name__ == '__main__':
    pass