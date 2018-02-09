# -*- coding: UTF-8 -*-
from roboti import vrednosti
from roboti.cuvanje.citanje_iz_fajla import ucitavanje_robota, ucitavanje_okvira, ucitavanje_motora, ucitavanje_senzora, prikaz_vrednosti
from roboti.view.glavni import glavni_meni


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
    
    glavni_meni()
    
    print("Prekinuto izvrsavanje")
