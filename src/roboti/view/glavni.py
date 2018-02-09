# -*- coding: UTF-8 -*-
from roboti.view.util import prikaz_menija, provera_unosa
from roboti.view.roboti import meni_roboti
from roboti.view.okviri import meni_okviri
from roboti.view.motori import meni_motori
from roboti.view.senzori import meni_senzori


def glavni_meni():
    '''
    Prikazuje pocetni meni
    '''
    while True:
        prikaz_menija("Koju opciju zelite: ","1 - Roboti","2 - Okviri","3 - Motori","4 - Senzori","5 - Prekid")
        
        opcija = provera_unosa("Opcija: ","Opcija mora biti celobrojna vrednost", int)
        
        if opcija == 5:
            break
        elif opcija == 1:
            meni_roboti()
        elif opcija == 2:
            meni_okviri()
        elif opcija == 3:
            meni_motori()
        elif opcija == 4:
            meni_senzori()
        
