#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests du module lib_format
"""
import pytest
from lib_format import format_gares, format_itineraire, format_connexions
from lib_sncf import Carte, Gare


@pytest.fixture
def simple() -> Carte:
    paris = Gare(nom="Paris")
    tours = Gare(nom="Tours")
    return Carte(gares=[paris, tours], connexions=[(paris, tours, 1.5)])


def test_gares(simple):
    calcule = format_gares(simple)
    assert list(calcule.renderables) == ["Paris", "Tours"]


# TODO: implémenter après modification de format_itineraire
def test_itineraire(simple):
    ...


def test_connexions(simple):
    calcule = format_connexions(simple)
    c1, c2, c3 = calcule.columns
    assert c1.header == "Depart"
    assert c2.header == "Arrivée"
    assert c3.header == "Durée"
    assert next(c1.cells) == "Paris"
    assert next(c2.cells) == "Tours"
    assert next(c3.cells) == "1.5"
