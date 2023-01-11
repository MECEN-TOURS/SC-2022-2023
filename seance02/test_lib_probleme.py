"""Description.

Tests du module lib_probleme.
"""
from lib_probleme import (
    DEPART,
    ARRIVEE,
    SOMMETS,
    ARRETES,
    est_valide,
    sont_relies,
    Rive,
    Etat,
)


def test_est_valide():
    assert est_valide(etat=DEPART)
    assert est_valide(etat=ARRIVEE)

    probleme = Etat(
        berger=Rive.GAUCHE,
        loup=Rive.DROITE,
        mouton=Rive.DROITE,
        chou=Rive.GAUCHE,
    )
    assert not est_valide(etat=probleme)


def test_sont_relies():
    assert not sont_relies(
        etat1=Etat(
            berger=Rive.GAUCHE,
            loup=Rive.GAUCHE,
            mouton=Rive.GAUCHE,
            chou=Rive.GAUCHE,
        ),
        etat2=Etat(
            berger=Rive.GAUCHE,
            loup=Rive.GAUCHE,
            mouton=Rive.GAUCHE,
            chou=Rive.GAUCHE,
        ),
    )
    assert sont_relies(
        etat1=Etat(
            berger=Rive.GAUCHE,
            loup=Rive.GAUCHE,
            mouton=Rive.GAUCHE,
            chou=Rive.GAUCHE,
        ),
        etat2=Etat(
            berger=Rive.DROITE,
            loup=Rive.GAUCHE,
            mouton=Rive.DROITE,
            chou=Rive.GAUCHE,
        ),
    )


def test_constantes():
    assert len(SOMMETS) == 10
    assert len(ARRETES) == 20
