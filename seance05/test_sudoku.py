"""Description.

Tests de lib_sudoku
"""
from lib_sudoku import (
    Grille,
    _est_valide,
    _est_remplie,
    _genere_voisines,
    resoud_sudoku,
    PasDeSolution,
)
import pytest


def test_init_grille():
    with pytest.raises(ValueError):
        Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    with pytest.raises(ValueError):
        Grille(cases=[-1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    with pytest.raises(ValueError):
        Grille(cases=[5, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_validite_grille():
    assert (
        _est_valide(
            grille=Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        )
        is True
    )

    assert (
        _est_valide(
            grille=Grille(cases=[1, 2, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        )
        is False
    )

    assert (
        _est_valide(
            grille=Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
        )
        is False
    )

    assert (
        _est_valide(
            grille=Grille(cases=[1, 2, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        )
        is False
    )


def test_remplissage():
    assert (
        _est_remplie(
            grille=Grille(cases=[1, 2, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        )
        is False
    )

    assert (
        _est_remplie(
            grille=Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
        )
        is True
    )


def test_voisinage():
    it = _genere_voisines(
        grille=Grille(
            cases=[0, 2, 3, 4, 3, 0, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
        )
    )
    assert next(it) == Grille(
        cases=[1, 2, 3, 4, 3, 0, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
    )
    assert next(it) == Grille(
        cases=[2, 2, 3, 4, 3, 0, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
    )
    assert next(it) == Grille(
        cases=[3, 2, 3, 4, 3, 0, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
    )
    assert next(it) == Grille(
        cases=[4, 2, 3, 4, 3, 0, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
    )
    with pytest.raises(StopIteration):
        next(it)


def test_resolution():
    assert resoud_sudoku(
        grille=Grille(
            cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
        )
    ) == Grille(
        cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
    )

    assert resoud_sudoku(
        grille=Grille(
            cases=[0, 2, 3, 4, 3, 0, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
        )
    ) == Grille(
        cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
    )
    with pytest.raises(PasDeSolution):
        resoud_sudoku(
            grille=Grille(
                cases=[2, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1],
            )
        )


def test_affichage():
    entree = Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 0])
    sortie = str(entree)
    attendue = """
---------
|1|2|3|4|
---------
|3|4|1|2|
---------
|2|1|4|3|
---------
|4|3|2| |
---------
"""
    assert attendue == sortie
