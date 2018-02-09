# -*- coding: UTF-8 -*-
from roboti.view.util import prikaz_menija, provera_unosa, vrednost_za_pretragu
from roboti import vrednosti
from roboti.cuvanje.upis_u_fajl import cuvanje_robota
from roboti.vrednosti import robot_po_oznaci
from roboti.model import Robot, MehanickiDeo, ElektricniDeo


def meni_roboti():
    '''
    Ovo je metoda za prikaz menija robota
    Kupi vrednost,porverava da li je dobra vrednost i na osnovu toga poziva
    '''
    while True:
        prikaz_menija("Koju opciju zelite: ","1 - Prikaz robota","2 - Unos robota","3 - Izmena robota","4 - Pretraga robota","5 - Prikaz delova robota","6 - Prikaz tezine mehanickih delova robota","7 - Prikaz potrosnje elektricnih delova robota","8 - Izlaz")
                
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 8:
            break
        elif opcija == 1:
            prikaz_robota(vrednosti.roboti)
        elif opcija == 2:
            r = unos_robota()
            vrednosti.roboti.append(r)
            cuvanje_robota(vrednosti.roboti)
            print("Robot uspesno kreiran {}".format(r))
        elif opcija == 3:
            robot_oznaka = unos_oznake_robota("Unesite oznaku robota ", True)
            robot = robot_po_oznaci(robot_oznaka)
            izmena_robota(robot)
            cuvanje_robota(vrednosti.roboti)
            print("Robot uspesno izmenjen {}".format(robot))
        elif opcija == 4:
            pretraga_robota()
        elif opcija == 5:
            robot_oznaka = unos_oznake_robota("Unesite oznaku robota ", True)
            robot = robot_po_oznaci(robot_oznaka)
            pronadjen = pronadji_delove_za_robota(robot)
            prikaz_delova(pronadjen)
        elif opcija == 6:
            robot_oznaka = unos_oznake_robota("Unesite oznaku robota ", True)
            robot = robot_po_oznaci(robot_oznaka)
            pronadjen = pronadji_delove_za_robota(robot)
            tezina = tezina_mehanickih_delova(pronadjen)
            print("Ukupna tezina mehanickih delova robota je: {}".format(tezina))
        elif opcija == 7:
            robot_oznaka = unos_oznake_robota("Unesite oznaku robota ", True)
            robot = robot_po_oznaci(robot_oznaka)
            pronadjen = pronadji_delove_za_robota(robot)
            potrosnja = potrosnja_elektricnih_delova(pronadjen)
            print("Ukupna potrosnja elektricnih delova robota je: {}".format(potrosnja))


def prikaz_robota(roboti):
    '''
    Metoda za prikaz robota i pravljenje tabele
    :param roboti:
    '''
    
    print("{:10}|{:30}|{:10}|".format("Oznaka", "Opis", "Proizvodjac"))
    for r in roboti:
        print("{:10}|{:30}|{:10}|".format(r.oznaka, r.opis, r.proizvodjac))
            
        
def unos_robota():
    '''
    Metoda za unos robota
    '''
    print("Unos vrednosti za robota: ")
    oznaka = unos_oznake_robota("Oznaka: ", False)
    opis = input("Opis: ")
    proizvodjac = input("Proizvodjac: ")
    r = Robot(oznaka, opis, proizvodjac)
    return r

        
def unos_oznake_robota(poruka, postojeca):
    '''
    Provera unosa oznake robota
    :param poruka:
    :param postojeca:
    '''
    if postojeca:
        poruka_greska = "Robot sa oznakom ne postoji"
    else:
        poruka_greska = "Robot sa oznakom vec postoji"
        
    while True:
        vrednost = input(poruka)
        
        if vrednost is None or vrednost == "":
            break
        else:
            robot = robot_po_oznaci(vrednost)
            if robot is None and postojeca:
                print(poruka_greska)
            elif robot is not None and not postojeca:
                print(poruka_greska)
            else:
                return vrednost   


def izmena_robota(robot):
    '''
    Izmena oznake,opisa i proizvodjaca
    :param robot:
    '''
    print("Unos vrednosti za robota: ")
    oznaka = input("Oznaka: ")
    opis = input("Opis: ")
    proizvodjac = input("Proizvodjac: ")
    robot.oznaka = oznaka
    robot.opis = opis
    robot.proizvodjac = proizvodjac


def pretraga_robota():
    '''
    Meni za pretragu robota
    Kupi vrednost i na osnovu toga pretrazuje
    '''
    while True:
        prikaz_menija("Pretraga robota: ","1 - po oznaci","2 - po opisu","3 - po proizvodjacu","4 - Izlaz")
        
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 4:
            break
        elif opcija == 1:
            oznaka = input("Unesite oznaku za pretragu: ")
            print();
            pronadjeni = pretraga_po_oznaci(oznaka)
            prikaz_robota(pronadjeni)
        elif opcija == 2:
            opis = input("Unesite opis za pretragu: ")
            print();
            pronadjeni = pretraga_po_opisu(opis)
            prikaz_robota(pronadjeni)
        elif opcija == 3:
            proizvodjac = input("Unesite proizvodjaca za pretragu: ")
            print();
            pronadjeni = pretraga_po_proizvodjacu(proizvodjac)
            prikaz_robota(pronadjeni)    
            

def pretraga_po_oznaci(oznaka):
    '''
    Metoda za pretragu po oznaci
    :param oznaka:
    '''
    pronadjeni = []
    for r in vrednosti.roboti:
        if oznaka in r.oznaka:
            pronadjeni.append(r)
    return pronadjeni


def pretraga_po_opisu(opis):
    '''
    Metoda za pretragu po opisu
    :param opis:
    '''
    pronadjeni = []
    for r in vrednosti.roboti:
        if opis in r.opis:
            pronadjeni.append(r)
    return pronadjeni


def pretraga_po_proizvodjacu(proizvodjac):
    '''
    Metoda za pretragu po proizvodjacu
    :param proizvodjac:
    '''
    pronadjeni=[]
    for r in vrednosti.roboti:
        if proizvodjac in r.proizvodjac:
            pronadjeni.append(r)
    return pronadjeni


def pronadji_delove_za_robota(robot):
    '''
    Metoda koja pretrazuje delove i dodaje ih u listu
    :param robot:
    '''
    pronadjeni = []
    for o in vrednosti.okviri:
        if o.robot ==  robot:
            pronadjeni.append(o)
    for m in vrednosti.motori:
        if m.robot == robot:
            pronadjeni.append(m)
    for s in vrednosti.senzori:
        if s.robot == robot:
            pronadjeni.append(s)
    return pronadjeni
    
    
def prikaz_delova(delovi):
    '''
    Metoda za prikaz i formatiranje delova
    :param delovi:
    '''
    print("{:10}|{:30}|{:10}|{:10}|{:10}|{:10}|".format("Oznaka", "Opis", "Duzina", "Sirina", "Visina", "Robot"))
    for d in delovi:
        print("{:10}|{:30}|{:10}|{:10}|{:10}|{:10}|".format(d.oznaka, d.opis, d.duzina, d.sirina, d.visina, "" if d.robot is None else d.robot.oznaka))
    
    
def tezina_mehanickih_delova(delovi):
    '''
    Zadaje mu inicijalnu nulu i za odgovarajuci pronadjeni deo dodaje tezinu cija je forma definisana u modulu model
    :param delovi:
    '''
    tezina = 0
    for d in delovi:
        if isinstance(d, MehanickiDeo):
            tezina += d.tezina
    return tezina


def potrosnja_elektricnih_delova(delovi):
    '''
    Zadaje mu inicijalnu nulu i za odgovarajuci pronadjeni deo dodaje elektricnu potrosnju cija je forma definisana u modulu model
    :param delovi:
    '''
    potrosnja = 0
    for d in delovi:
        if isinstance(d, ElektricniDeo):
            potrosnja += d.elektricna_potrosnja()
    return potrosnja 
           
           
if __name__ == '__main__':
    pass