# -*- coding: UTF-8 -*-
from roboti.cuvanje.putanje import robotFajl, okvirFajl, motorFajl, senzorFajl
from roboti.model import Robot, Okvir, Motor, Senzor
from roboti.vrednosti import robot_po_oznaci
from roboti import vrednosti


def ucitavanje_robota():
    '''
    Otvara fajl i deli po liniji
    '''
    roboti = []
    with open(robotFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            proizvodjac = fields[2]
            roboti.append(Robot(oznaka, opis, proizvodjac))
    return roboti


def ucitavanje_okvira():
    '''
    Otvara fajl i deli po liniji
    '''
    okviri = []
    with open(okvirFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            duzina = float(fields[2])
            sirina = float(fields[3])
            visina = float(fields[4])
            tezina = float(fields[5])
            tip_materijala = fields[6] 
            robot_oznaka = fields[7]
            robot = robot_po_oznaci(robot_oznaka)
            okviri.append(Okvir(oznaka, opis, duzina, sirina, visina, tezina, tip_materijala, robot))
    return okviri


def ucitavanje_motora():
    '''
    Otvara fajl i deli po liniji
    '''
    motori = []
    with open(motorFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            duzina = float(fields[2])
            sirina = float(fields[3])
            visina = float(fields[4])
            tezina = float(fields[5])
            vreme_rada = int(fields[6])
            obrtaja_u_minuti = float(fields[7])
            potrosnja_po_obrtaju = float(fields[8])
            robot_oznaka = fields[9]
            robot = robot_po_oznaci(robot_oznaka)
            motori.append(Motor(oznaka, opis, duzina, sirina, visina, tezina, vreme_rada, obrtaja_u_minuti, potrosnja_po_obrtaju, robot))
    return motori


def ucitavanje_senzora():
    '''
    Otvara fajl i deli po liniji
    '''
    senzori = []
    with open(senzorFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            duzina = float(fields[2])
            sirina = float(fields[3])
            visina = float(fields[4])
            tip = fields[5]
            merna_jedinica = fields[6]
            izmerena_vrednost = float(fields[7])
            potrosnja_po_merenju = float(fields[8])
            broj_merenja = float(fields[9])
            robot_oznaka = fields[10]
            robot = robot_po_oznaci(robot_oznaka)
            senzori.append(Senzor(oznaka, opis, duzina, sirina, visina, tip, merna_jedinica, izmerena_vrednost, potrosnja_po_merenju, broj_merenja, robot))
    return senzori


def prikaz_vrednosti(lista):
    '''
    Enumeracija lista
    :param lista:
    '''
    for i,el in enumerate(lista):
        print("{} {}".format(i,el))

if __name__ == '__main__':
    vrednosti.roboti = ucitavanje_robota()
    vrednosti.okviri = ucitavanje_okvira()
    vrednosti.motori = ucitavanje_motora()
    vrednosti.senzori = ucitavanje_senzora()
    
    print("Roboti:")
    prikaz_vrednosti(vrednosti.roboti)
    print("Okviri:")
    prikaz_vrednosti(vrednosti.okviri)
    print("Motori:")
    prikaz_vrednosti(vrednosti.motori)
    print("Senzori:")
    prikaz_vrednosti(vrednosti.senzori)