"""Description.

Tests du module lib_sncf
"""
import pytest
import networkx as nx
from lib_sncf import (
    Gare,
    Itineraire,
    Carte,
    determine_trajet,
    _convertit_en_nx,
    PasDeChemin,
    GareInconnue,
)


def test_connexion():
    with pytest.raises(ValueError):
        Carte(
            gares=[Gare("Paris"), Gare("Tours")],
            connexions=[(Gare("Paris"), Gare("Tours"), -1.0)],
        )


def test_gare():
    with pytest.raises(ValueError):
        Carte(
            gares=[Gare("Paris"), Gare("Tours")],
            connexions=[(Gare("Paris"), Gare("Tour"), 1.0)],
        )


def test_conversion():
    pa, ly, to = Gare("Paris"), Gare("Lyon"), Gare("Tours")
    carte = Carte(
        gares=[pa, ly, to],
        connexions=[(pa, to, 1.0), (pa, ly, 2.0)],
    )
    calcule = _convertit_en_nx(carte)
    attendu = nx.Graph()
    attendu.add_nodes_from([pa, ly, to])
    attendu.add_edges_from(
        [
            (pa, to, {"duree": 1.0}),
            (pa, ly, {"duree": 2.0}),
        ]
    )
    assert nx.utils.graphs_equal(calcule, attendu)


def test_trajet():
    pa, to, bo, ly, mo, tls = gares = [
        Gare(nom="Paris"),
        Gare(nom="Tours"),
        Gare(nom="Bordeaux"),
        Gare(nom="Lyon"),
        Gare(nom="Montpellier"),
        Gare(nom="Toulouse"),
    ]
    carte_simple = Carte(
        gares=gares,
        connexions=[
            (pa, to, 1),
            (to, bo, 2),
            (bo, tls, 4),
            (tls, mo, 4),
            (mo, ly, 2),
            (ly, pa, 2),
        ],
    )
    attendu = Itineraire(etapes=[bo, to, pa, ly, mo])
    calcule = determine_trajet(depart=bo, arrivee=mo, carte=carte_simple)
    assert attendu == calcule


def test_pas_de_trajet():
    carte_elementaire = Carte(
        gares=[Gare("Paris"), Gare("Tours"), Gare("Nice")],
        connexions=[(Gare("Paris"), Gare("Tours"), 1.0)],
    )
    with pytest.raises(PasDeChemin):
        determine_trajet(
            depart=Gare("Paris"), arrivee=Gare("Nice"), carte=carte_elementaire
        )


def test_mauvaise_gare():
    carte_elementaire = Carte(
        gares=[Gare("Paris"), Gare("Tours"), Gare("Nice")],
        connexions=[(Gare("Paris"), Gare("Tours"), 1.0)],
    )
    with pytest.raises(GareInconnue):
        determine_trajet(
            depart=Gare("Paris"), arrivee=Gare("Lyon"), carte=carte_elementaire
        )
    with pytest.raises(GareInconnue):
        determine_trajet(
            depart=Gare("Lyon"), arrivee=Gare("Paris"), carte=carte_elementaire
        )
