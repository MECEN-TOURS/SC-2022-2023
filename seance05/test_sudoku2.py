"""Description.

Tests de lib_sudoku
"""
from lib_sudoku2 import (
    Grille,
    _est_valide,
    _est_remplie,
    _genere_voisines,
    resoud_sudoku,
    PasDeSolution,
)
import pytest

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

def test_alternatif():
    """Construction alternative de Grille."""
    entree = """
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
    sortie = Grille.from_str(entree)
    attendue = Grille(
        cases=[
            1,2,3,4,5,6,7,8,9,
            4,5,6,7,8,9,1,2,3,
            7,8,9,1,2,3,4,5,6,
            2,3,1,5,6,4,8,9,7,
            5,6,4,8,9,7,2,3,1,
            8,9,7,2,3,1,5,6,4,
            3,1,2,6,4,5,9,7,8,
            6,4,5,9,7,8,3,1,2,
            9,7,8,3,1,2,6,4,5,
        ]
    )
    assert attendue == sortie
    
        
@pytest.mark.xfail
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
        
@pytest.mark.xfail
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

@pytest.mark.xfail
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

@pytest.mark.xfail
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

@pytest.mark.xfail
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


