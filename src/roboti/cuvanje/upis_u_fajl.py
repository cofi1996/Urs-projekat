# -*- coding: UTF-8 -*-
from roboti.cuvanje.putanje import robotFajl, okvirFajl, motorFajl, senzorFajl
from roboti.model import Robot, Okvir, Motor, Senzor


def cuvanje_robota(roboti):
    '''
    Cuvanje atributa robota
    :param roboti:
    '''
    with open(robotFajl,"w") as f:
        for r in roboti:
            f.write("{}|".format(r.oznaka))
            f.write("{}|".format(r.opis))
            f.write("{}|\n".format(r.proizvodjac))
          
          
def cuvanje_okvira(okviri):
    '''
    Cuvanje atributa okvira
    :param okviri:
    '''
    with open(okvirFajl,"w") as f:
        for o in okviri:
            f.write("{}|".format(o.oznaka))
            f.write("{}|".format(o.opis))
            f.write("{}|".format(o.duzina))
            f.write("{}|".format(o.sirina))
            f.write("{}|".format(o.visina))
            f.write("{}|".format(o.tezina))
            f.write("{}|".format(o.tip_materijala))
            f.write("{}|\n".format("None" if o.robot is None else o.robot.oznaka))


def cuvanje_motora(motori):
    '''
    Cuvanje atributa motora
    :param motori:
    '''
    with open(motorFajl,"w") as f:
        for m in motori:
            f.write("{}|".format(m.oznaka))
            f.write("{}|".format(m.opis))
            f.write("{}|".format(m.duzina))
            f.write("{}|".format(m.sirina))
            f.write("{}|".format(m.visina))
            f.write("{}|".format(m.tezina))
            f.write("{}|".format(m.vreme_rada))
            f.write("{}|".format(m.obrtaja_u_minuti))
            f.write("{}|".format(m.potrosnja_po_obrtaju))
            f.write("{}|\n".format("None" if m.robot is None else m.robot.oznaka))
  
            
def cuvanje_senzora(senzori):
    '''
    Cuvanje atributa senzora
    :param senzori:
    '''
    with open(senzorFajl,"w") as f:
        for s in senzori:
            f.write("{}|".format(s.oznaka))
            f.write("{}|".format(s.opis))
            f.write("{}|".format(s.duzina))
            f.write("{}|".format(s.sirina))
            f.write("{}|".format(s.visina))
            f.write("{}|".format(s.tip))
            f.write("{}|".format(s.merna_jedinica))
            f.write("{}|".format(s.izmerena_vrednost))
            f.write("{}|".format(s.potrosnja_po_merenju))
            f.write("{}|".format(s.broj_merenja))
            f.write("{}|\n".format("None" if s.robot is None else s.robot.oznaka))
            
            
if __name__ == '__main__':
    roboti = []
    r1 = Robot("RB1", "Robot 1", "Proizvodjac 1")
    r2 = Robot("RB2", "Robot 2", "Proizvodjac 2")
    roboti.append(r1)
    roboti.append(r2)
    cuvanje_robota(roboti)
    
    okviri = []
    o1 = Okvir("O1", "Okvir 1", 50, 100, 100, 50, "Materijal 1", r1)
    o2 = Okvir("O2", "Okvir 2", 100, 100, 120, 70, "Materijal 2", r2)
    okviri.append(o1)
    okviri.append(o2)
    cuvanje_okvira(okviri)
    
    motori = []
    m1 = Motor("M1", "Motor 1", 30, 50, 40, 15, 10, 30.5, 100.0, r1)
    m2 = Motor("M2", "Motor 2", 40, 40, 40, 20, 15, 20.5, 100.5, r2)
    motori.append(m1)
    motori.append(m2)
    cuvanje_motora(motori)
    
    senzori = []
    s1 = Senzor("S1", "Senzor 1", 5, 10, 15, "Toplotni", "Merna jedinica 1", 140, 20, 2, r1)
    s2 = Senzor("S2", "Senzor 2", 3, 6, 5, "Svetlosni", "Merna jedinica 2", 50, 40, 5, r2)
    senzori.append(s1)
    senzori.append(s2)
    cuvanje_senzora(senzori)
    
    print("Vrednosti upisane u fajlove")