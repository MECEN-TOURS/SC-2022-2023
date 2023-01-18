"""Description.

Tests du module lib_probleme.
"""
from lib_probleme import (
    DEPART,
    ARRIVEE,
    SOMMETS,
    ARRETES,
    _est_valide,
    _sont_relies,
    Rive,
    Etat,
    pretty_print,
)


def test_est_valide():
    assert _est_valide(etat=DEPART)
    assert _est_valide(etat=ARRIVEE)

    probleme = Etat(
        berger=Rive.GAUCHE,
        loup=Rive.DROITE,
        mouton=Rive.DROITE,
        chou=Rive.GAUCHE,
    )
    assert not _est_valide(etat=probleme)


def test_sont_relies():
    assert not _sont_relies(
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
    assert _sont_relies(
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


def test_pretty():
    assert (
        pretty_print(DEPART)
        == """B L M C
-------
X X X X"""
    )
    assert (
        pretty_print(ARRIVEE)
        == """X X X X
-------
B L M C"""
    )
    assert (
        pretty_print(
            Etat(
                berger=Rive.GAUCHE,
                loup=Rive.DROITE,
                mouton=Rive.GAUCHE,
                chou=Rive.DROITE,
            )
        )
        == """B X M X
-------
X L X C"""
    )
