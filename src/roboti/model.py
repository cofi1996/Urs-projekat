# -*- coding: UTF-8 -*-


class Identifikacija(object):
    '''
    Definisanje roditeljske klase identrifikacija
    '''
    def __init__(self, oznaka, opis, **kwargs):
        super().__init__(**kwargs)
        self.oznaka = oznaka
        self.opis = opis
        
    def __str__(self, *args, **kwargs):
        return "{} {}".format(self.oznaka, self.opis)
    
    
class Dimenzije(object):
    '''
    Definisanje roditeljske klase identifikacija
    '''
    def __init__(self, duzina, sirina, visina, **kwargs):
        super().__init__(**kwargs)
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina

    @property
    def duzina(self):
        return self.__duzina

    @duzina.setter
    def duzina(self, value):
        if value <= 0:
            raise ValueError("Vrednost za duzinu mora biti veca od 0")
        self.__duzina = value

    @property
    def sirina(self):
        return self.__sirina

    @sirina.setter
    def sirina(self, value):
        if value <= 0:
            raise ValueError("Vrednost za sirinu mora biti veca od 0")
        self.__sirina = value

    @property
    def visina(self):
        return self.__visina

    @visina.setter
    def visina(self, value):
        if value <= 0:
            raise ValueError("Vrednost za visinu mora biti veca od 0")
        self.__visina = value

    def __str__(self):
        return "{} {} {}".format(self.duzina, self.sirina, self.visina)
    
    
class Robot(Identifikacija):
    '''
    Definisanje klase robot koja nasledjuje klasu identifikacije
    '''
    def __init__(self, oznaka, opis, proizvodjac):
        super().__init__(oznaka=oznaka, opis=opis)
        self.proizvodjac = proizvodjac
        
    def __str__(self, *args, **kwargs):
        return "{} {}".format(super().__str__(), self.proizvodjac)
    
    
class Deo(Identifikacija,Dimenzije):
    '''
    Definisanje klase deo koja nasledjuje klase identifikacije i dimenzija
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, robot):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina)
        self.robot = robot
        
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.oznaka, self.opis, self.duzina, self.sirina, self.visina, self.robot)
    

class MehanickiDeo(Deo):
    '''
    Definisanje klase mehanicki deo koja nasledjuje klasu deo
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, tezina, robot):
        super().__init__(oznaka, opis, duzina, sirina, visina, robot)
        self.tezina = tezina
        
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.oznaka, self.opis, self.duzina, self.sirina, self.visina, self.tezina, self.robot)


class ElektricniDeo(Deo):
    '''
    Definisanje klase elektricni deo koja nasledjuje klasu deo
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, robot):
        super().__init__(oznaka, opis, duzina, sirina, visina, robot)
        
    def elektricna_potrosnja(self):
        return    
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.oznaka, self.opis, self.duzina, self.sirina, self.visina, self.robot)
 
 
class Okvir(MehanickiDeo):
    '''
    Definisanje klase okvir koja nasledjuje klasu mehanicki deo
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, tezina, tip_materijala, robot):
        super().__init__(oznaka, opis, duzina, sirina, visina, tezina, robot)
        self.tip_materijala = tip_materijala
        
    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.oznaka, self.opis, self.duzina, self.sirina, self.visina, self.tezina, self.tip_materijala, self.robot)


class Motor(MehanickiDeo, ElektricniDeo):
    '''
    Definisanje klase motor koja nasledjuje klase mehanicki deo i elektricni deo
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, tezina, vreme_rada, obrtaja_u_minuti, potrosnja_po_obrtaju, robot):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina, tezina=tezina, robot=robot)
        self.vreme_rada = vreme_rada
        self.obrtaja_u_minuti = obrtaja_u_minuti
        self.potrosnja_po_obrtaju = potrosnja_po_obrtaju
        
    def elektricna_potrosnja(self):
        return self.vreme_rada * self.obrtaja_u_minuti * self.potrosnja_po_obrtaju
        
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {}".format(self.oznaka, self.opis, self.duzina, self.sirina, self.visina, self.tezina, self.vreme_rada, self.obrtaja_u_minuti, self.potrosnja_po_obrtaju, self.robot) 
    
    
class Senzor(ElektricniDeo):
    '''
    Definisanj klase senzor koja nasledjuje klasu elektricni deo
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, tip, merna_jedinica, izmerena_vrednost, potrosnja_po_merenju, broj_merenja, robot):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina, robot=robot)
        self.tip = tip
        self.merna_jedinica = merna_jedinica
        self.izmerena_vrednost = izmerena_vrednost
        self.potrosnja_po_merenju = potrosnja_po_merenju
        self.broj_merenja = broj_merenja
        
    def elektricna_potrosnja(self):
        return self.potrosnja_po_merenju * self.broj_merenja
        
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {}".format(self.oznaka, self.opis, self.duzina, self.sirina, self.visina, self.tip, self.merna_jedinica, self.izmerena_vrednost, self.potrosnja_po_merenju, self.broj_merenja, self.robot)    
    
    
if __name__ == '__main__':
    pass