"""Description.

Tests du module lib_bellman.
"""
import pytest
from lib_graphe import GraphePondere
from lib_bellman import determine_chemin_minimal, itere_distance, determine_distance

@pytest.fixture
def gp():
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
    return GraphePondere(sommets=sommets, arretes=arretes)
    

def test_itere_distance(gp):
    d0 = {
        "A": (float("inf"), None),
        "B": (float("inf"), None),
        "C": (float("inf"), None),
        "D": (float("inf"), None),
        "E": (float("inf"), None),
        "F": (0, "F"),
    }
    d1 = {
        "A": (float("inf"), None),
        "B": (float("inf"), None),
        "C": (float("inf"), None),
        "D": (1, "F"),
        "E": (float("inf"), None),
        "F": (0, "F"),
    }
    assert itere_distance(dist=d0, gp=gp) == d1
    d2 = {
        "A": (6, "D"),
        "B": (float("inf"), None),
        "C": (3, "D"),
        "D": (1, "F"),
        "E": (2, "D"),
        "F": (0, "F"),
    }
    assert itere_distance(dist=d1, gp=gp) == d2
    d3 = {
        "A": (5, "C"),
        "B": (3, "E"),
        "C": (3, "D"),
        "D": (1, "F"),
        "E": (2, "D"),
        "F": (0, "F"),
    }
    assert itere_distance(dist=d2, gp=gp) == d3
    d4 = {
        "A": (4, "B"),
        "B": (3, "E"),
        "C": (3, "D"),
        "D": (1, "F"),
        "E": (2, "D"),
        "F": (0, "F"),
    }
    assert itere_distance(dist=d3, gp=gp) == d4
    assert itere_distance(dist=d4, gp=gp) == d4
    
def test_determine_distance(gp):
    attendue = {
        "A": (4, "B"),
        "B": (3, "E"),
        "C": (3, "D"),
        "D": (1, "F"),
        "E": (2, "D"),
        "F": (0, "F"),
    } 
    assert determine_distance(arrivee="F", gp=gp) == attendue

@pytest.mark.xfail
def test_chemin(gp):
    
    assert determine_chemin_minimal(depart="A", arrivee="B", gp=gp) == ["A", "B", "E", "D", "F"]