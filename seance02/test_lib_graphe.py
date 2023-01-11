"""Description.

Tests automatiques de la librairie lib_graphe.
"""
import pytest
from lib_graphe import (
    recupere_voisins,
    sont_connectes,
    determine_chemin,
    cherche_chemin,
    PasDeChemin,
)


def test_recupere_voisins():
    assert recupere_voisins(sommet=1, arretes=[(1, 2), (3, 1)]) == [2]
    assert recupere_voisins(
        sommet=2,
        arretes=[(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)],
    ) == [3, 5]


def test_sont_connectes():
    sommets = [1, 2, 3, 4, 5, 6, 7, 8]
    arretes = [(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)]
    assert sont_connectes(depart=1, arrivee=7, sommets=sommets, arretes=arretes)
    assert not sont_connectes(depart=1, arrivee=8, sommets=sommets, arretes=arretes)


def test_determine_chemin():
    assert determine_chemin(
        depart=1, arrivee=7, vu_en_premier_par={1: None, 2: 1, 3: 2, 5: 2, 6: 5, 7: 6}
    ) == [1, 2, 5, 6, 7]


def test_cherche_chemin():
    sommets = [1, 2, 3, 4, 5, 6, 7, 8]
    arretes = [(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)]
    assert cherche_chemin(depart=1, arrivee=7, sommets=sommets, arretes=arretes) == [
        1,
        2,
        5,
        6,
        7,
    ]
    with pytest.raises(PasDeChemin):
        cherche_chemin(depart=1, arrivee=8, sommets=sommets, arretes=arretes)
