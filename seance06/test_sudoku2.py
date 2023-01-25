"""Description.

Tests de lib_sudoku
"""
from lib_sudoku2 import (
    Grille,
    _detecte_probleme_ligne,
    _detecte_probleme_colonne,
    _detecte_probleme_bloc,
    _est_valide,
    _est_remplie,
    _genere_voisines,
    resoud_sudoku,
    PasDeSolution,
)
import pytest


@pytest.fixture
def incomplete():
    tableau = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 5, 6, 4, 8, 9, 0],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [8, 9, 7, 0, 3, 1, 5, 6, 4],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [6, 4, 5, 9, 7, 8, 3, 1, 2],
        [9, 7, 8, 3, 1, 2, 6, 4, 5],
    ]
    return Grille(cases=[case for ligne in tableau for case in ligne])


@pytest.fixture
def complete():
    tableau = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 5, 6, 4, 8, 9, 7],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [8, 9, 7, 2, 3, 1, 5, 6, 4],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [6, 4, 5, 9, 7, 8, 3, 1, 2],
        [9, 7, 8, 3, 1, 2, 6, 4, 5],
    ]
    return Grille(cases=[case for ligne in tableau for case in ligne])


def test_init_grille():
    valide = Grille(cases=[0 for _ in range(81)])
    assert isinstance(valide, Grille)

    with pytest.raises(ValueError):
        cases = [0 for _ in range(81)]
        cases.append(0)
        Grille(cases=cases)

    with pytest.raises(ValueError):
        cases = [0 for _ in range(81)]
        cases[0] = -1
        Grille(cases=cases)

    with pytest.raises(ValueError):
        cases = [0 for _ in range(81)]
        cases[0] = 10
        Grille(cases=cases)


def test_alternatif(complete, incomplete):
    """Construction alternative de Grille."""
    entree1 = """
123456789
456789123
789123456
231564897
564897231
897231564
312645978
645978312
978312645
"""
    sortie1 = Grille.from_str(entree1)
    assert complete == sortie1
    entree2 = """
    
    
    
123456789
 456789123
789123456
23156489x
564897231
897x31564
312645978
645978312
978312645  


"""
    sortie2 = Grille.from_str(entree2)
    assert incomplete == sortie2


def test_affichage(complete):
    sortie = str(complete)
    attendue = """
-------------------
|1|2|3|4|5|6|7|8|9|
-------------------
|4|5|6|7|8|9|1|2|3|
-------------------
|7|8|9|1|2|3|4|5|6|
-------------------
|2|3|1|5|6|4|8|9|7|
-------------------
|5|6|4|8|9|7|2|3|1|
-------------------
|8|9|7|2|3|1|5|6|4|
-------------------
|3|1|2|6|4|5|9|7|8|
-------------------
|6|4|5|9|7|8|3|1|2|
-------------------
|9|7|8|3|1|2|6|4|5|
-------------------
"""
    assert attendue == sortie


def test_validite_colonne():
    cases = [0 for _ in range(81)]
    cases[0] = 9
    cases[27] = 9
    assert _detecte_probleme_colonne(grille=Grille(cases)) is True


def test_validite_ligne():
    cases = [0 for _ in range(81)]
    cases[0] = 9
    cases[4] = 9
    assert _detecte_probleme_ligne(grille=Grille(cases)) is True


def test_validite_bloc():
    cases = [0 for _ in range(81)]
    cases[0] = 9
    cases[10] = 9
    assert _detecte_probleme_bloc(grille=Grille(cases)) is True


def test_validite_grille(complete):
    assert _est_valide(grille=complete) is True


def test_remplissage(incomplete, complete):
    assert _est_remplie(incomplete) is False

    assert _est_remplie(complete) is True


def test_voisinage(incomplete):
    tableau = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 5, 6, 4, 8, 9, 0],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [8, 9, 7, 0, 3, 1, 5, 6, 4],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [6, 4, 5, 9, 7, 8, 3, 1, 2],
        [9, 7, 8, 3, 1, 2, 6, 4, 5],
    ]
    it = _genere_voisines(Grille(cases=[case for ligne in tableau for case in ligne]))
    for valeur in range(1, 10):
        cases = [case for ligne in tableau for case in ligne]
        cases[35] = valeur
        assert next(it) == Grille(cases)
    with pytest.raises(StopIteration):
        next(it)


def test_resolution(incomplete, complete):
    assert resoud_sudoku(complete) == complete
    assert resoud_sudoku(incomplete) == complete

    with pytest.raises(PasDeSolution):
        resoud_sudoku(Grille(cases=[9 for _ in range(81)]))
