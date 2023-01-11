"""Description.

Module permettant de modéliser le problème du berger, loup, mouton, chou en python.
"""
from enum import Enum
from dataclasses import dataclass


class Rive(Enum):
    GAUCHE = "gauche"
    DROITE = "droite"


# frozen pour pouvoir utiliser un Etat comme clef de dictionnaire
@dataclass(frozen=True)
class Etat:
    berger: Rive
    loup: Rive
    mouton: Rive
    chou: Rive


DEPART = Etat(
    berger=Rive.GAUCHE,
    loup=Rive.GAUCHE,
    mouton=Rive.GAUCHE,
    chou=Rive.GAUCHE,
)

ARRIVEE = Etat(
    berger=Rive.DROITE,
    loup=Rive.DROITE,
    mouton=Rive.DROITE,
    chou=Rive.DROITE,
)

etats = list()
for cote_berger in (Rive.GAUCHE, Rive.DROITE):
    for cote_loup in (Rive.GAUCHE, Rive.DROITE):
        for cote_mouton in (Rive.GAUCHE, Rive.DROITE):
            for cote_chou in (Rive.GAUCHE, Rive.DROITE):
                etats.append(
                    Etat(
                        berger=cote_berger,
                        loup=cote_loup,
                        mouton=cote_mouton,
                        chou=cote_chou,
                    )
                )


def est_valide(etat: Etat) -> bool:
    if etat.loup == etat.mouton and etat.loup != etat.berger:
        return False
    if etat.mouton == etat.chou and etat.mouton != etat.berger:
        return False
    return True


SOMMETS = [etat for etat in etats if est_valide(etat)]


def sont_relies(etat1: Etat, etat2: Etat) -> bool:
    if etat1.berger == etat2.berger:
        return False
    nombre_changements = 0
    if etat1.loup != etat2.loup:
        nombre_changements = nombre_changements + 1
    if etat1.mouton != etat2.mouton:
        nombre_changements = nombre_changements + 1
    if etat1.chou != etat2.chou:
        nombre_changements = nombre_changements + 1
    if nombre_changements < 2:
        return True
    else:
        return False


ARRETES = [
    (sommet1, sommet2)
    for sommet1 in SOMMETS
    for sommet2 in SOMMETS
    if sont_relies(sommet1, sommet2)
]
