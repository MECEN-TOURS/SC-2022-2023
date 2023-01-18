"""Description.

Tests automatiques de la librairie lib_graphe.
"""
import pytest
from lib_graphe import (
    _recupere_voisins,
    sont_connectes,
    _determine_chemin,
    cherche_chemin,
    PasDeChemin,
)


def test_recupere_voisins():
    assert _recupere_voisins(sommet=1, arretes=[(1, 2), (3, 1)]) == [2]
    assert _recupere_voisins(
        sommet=2,
        arretes=[(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)],
    ) == [3, 5]


def test_sont_connectes():
    arretes = [(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)]
    assert sont_connectes(depart=1, arrivee=7, arretes=arretes)
    assert not sont_connectes(depart=1, arrivee=8, arretes=arretes)


def test_determine_chemin():
    assert _determine_chemin(
        arrivee=7, vu_en_premier_par={1: None, 2: 1, 3: 2, 5: 2, 6: 5, 7: 6}
    ) == [1, 2, 5, 6, 7]


def test_cherche_chemin():
    arretes = [(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)]
    assert cherche_chemin(depart=1, arrivee=7, arretes=arretes) == [
        1,
        2,
        5,
        6,
        7,
    ]
    with pytest.raises(PasDeChemin):
        cherche_chemin(depart=1, arrivee=8, arretes=arretes)
