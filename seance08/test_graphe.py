"""Description.

Tests du module lib_graphe.
"""
import pytest
from lib_graphe import GraphePondere


def test_init():
    """Vérifie qu'on peut générer un objet."""
    sommets = list("ABCDEF")
    arretes = [
        ("A", "B", 1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("D", "A", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
        ("F", "D", 1),
    ]
    gp = GraphePondere(sommets=sommets,arretes=arretes)
    assert isinstance(gp, GraphePondere)
    
def test_validation():
    sommets = list("ABCDEF")
    arretes = [
        ("a", "B", 1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("D", "A", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
        ("F", "d", 1),
    ]
    with pytest.raises(ValueError):
        gp = GraphePondere(sommets=sommets, arretes=arretes)
        
    sommets = list("ABCDEF")
    arretes = [
        ("A", "B", -1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("D", "A", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
        ("F", "D", 1),
    ]
    with pytest.raises(ValueError):
        gp = GraphePondere(sommets=sommets, arretes=arretes)
    

def test_egalite():
    """Teste que l'égalité ne dépend pas de l'ordre dans les sommets/arretes."""
    sommets1 = list("ABCDEF")
    arretes1 = [
        ("A", "B", 1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("D", "A", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
        ("F", "D", 1),
    ]
    gp1 = GraphePondere(sommets=sommets1,arretes=arretes1)
    sommets2 = list("ABDEFC")
    arretes2 = [
        ("D", "A", 5),
        ("A", "B", 1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("F", "D", 1),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
    ]
    gp2 = GraphePondere(sommets=sommets2,arretes=arretes2)
    assert gp1 == gp2
    
    
def test_constructeur():
    sommets = list("ABCDEF")
    arretes_s = [
        ("A", "B", 1),
        ("A", "C", 2),
        ("A", "D", 5),
        ("B", "E", 1),
        ("C", "D", 2),
        ("D", "E", 1),
        ("D", "F", 1),
    ]
    gps = GraphePondere.symetrique(sommets=sommets, arretes=arretes_s)
    assert isinstance(gps, GraphePondere)
    arretes_o = [
        ("A", "B", 1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("D", "A", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
        ("F", "D", 1),
    ]
    gpo = GraphePondere(sommets=sommets, arretes=arretes_o)
    assert gpo == gps
    
def test_voisinage():
    sommets = list("ABCDEF")
    arretes = [
        ("A", "B", 1),
        ("B", "A", 1),
        ("A", "C", 2),
        ("C", "A", 2),
        ("A", "D", 5),
        ("D", "A", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 2),
        ("D", "C", 2),
        ("D", "E", 1),
        ("E", "D", 1),
        ("D", "F", 1),
        ("F", "D", 1),
    ]
    gp = GraphePondere(sommets=sommets, arretes=arretes)
    it = gp.voisinage("D")
    assert next(it) == ("A", 5)
    assert next(it) == ("C", 2)
    assert next(it) == ("E", 1)
    assert next(it) == ("F", 1)
    with pytest.raises(StopIteration):
        next(it)