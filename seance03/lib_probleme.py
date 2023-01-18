"""Description.

Module permettant de modéliser le problème du berger, loup, mouton, chou en python.

TODO: 
- Ajouter une fonction pretty_print pour avoir un affichage plus lisible des etats et sommets.
- Compléter la documentation des fonctions publique avec des exemples
"""
from enum import Enum
from dataclasses import dataclass


class Rive(Enum):
    """Représente les deux côtés possibles de la rivière."""

    GAUCHE = "gauche"
    DROITE = "droite"


# frozen pour pouvoir utiliser un Etat comme clef de dictionnaire
@dataclass(frozen=True)
class Etat:
    """Représente la disposition des personnages de chaque côté de la rivière.

    Exemple:
    >>> Etat(
    ...     berger=Rive.GAUCHE,
    ...     loup=Rive.GAUCHE,
    ...     mouton=Rive.GAUCHE,
    ...     chou=Rive.GAUCHE,
    ... )
    Etat(berger=<Rive.GAUCHE: 'gauche'>, loup=<Rive.GAUCHE: 'gauche'>, mouton=<Rive.GAUCHE: 'gauche'>, chou=<Rive.GAUCHE: 'gauche'>)
    >>> Etat(
    ...     berger=Rive.DROITE,
    ...     loup=Rive.DROITE,
    ...     mouton=Rive.DROITE,
    ...     chou=Rive.DROITE,
    ... )
    Etat(berger=<Rive.DROITE: 'droite'>, loup=<Rive.DROITE: 'droite'>, mouton=<Rive.DROITE: 'droite'>, chou=<Rive.DROITE: 'droite'>)"""

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

_etats = list()
for cote_berger in (Rive.GAUCHE, Rive.DROITE):
    for cote_loup in (Rive.GAUCHE, Rive.DROITE):
        for cote_mouton in (Rive.GAUCHE, Rive.DROITE):
            for cote_chou in (Rive.GAUCHE, Rive.DROITE):
                _etats.append(
                    Etat(
                        berger=cote_berger,
                        loup=cote_loup,
                        mouton=cote_mouton,
                        chou=cote_chou,
                    )
                )


def _est_valide(etat: Etat) -> bool:
    """Vérifie le respect de la règle de surveillance."""
    if etat.loup == etat.mouton and etat.loup != etat.berger:
        return False
    if etat.mouton == etat.chou and etat.mouton != etat.berger:
        return False
    return True


SOMMETS = [etat for etat in _etats if _est_valide(etat)]


def _sont_relies(etat1: Etat, etat2: Etat) -> bool:
    """Vérifie si on passe en une traversée entre les etats."""
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
    if _sont_relies(sommet1, sommet2)
]
