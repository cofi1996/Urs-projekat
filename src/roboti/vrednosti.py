# -*- coding: UTF-8 -*-
roboti = []
okviri = []
motori = []
senzori = []


def robot_po_oznaci(oznaka):
    '''
    Trazi robote po oznaci
    :param oznaka:
    '''
    for r in roboti:
        if r.oznaka == oznaka:
            return r


def okvir_po_oznaci(oznaka):
    '''
    Trazi okvire po oznaci
    :param oznaka:
    '''
    for o in okviri:
        if o.oznaka == oznaka:
            return o

    
def motor_po_oznaci(oznaka):
    '''
    Trazi motor po oznaci
    :param oznaka:
    '''
    for m in motori:
        if m.oznaka == oznaka:
            return m


def senzor_po_oznaci(oznaka):
    '''
    Trazi senzore po oznaci
    :param oznaka:
    '''
    for s in senzori:
        if s.oznaka == oznaka:
            return s
        

if __name__ == '__main__':
    pass