#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Test d'intégration de l'application.
"""
from subprocess import run


def test_commande_gare():
    resultat = run(["python", "app.py", "gares"], capture_output=True)
    assert resultat.stdout.decode("utf8") == (
        "Paris      Tours Bordeaux Lyon Montpellier Toulouse Lille Nice Marseille\n"
        "Strasbourg Brest Nantes   Pau  Rennes                                   \n"
    )


def test_commande_connexions():
    resultat = run(["python", "app.py", "connexions"], capture_output=True)
    assert resultat.stdout.decode("utf8") == (
        "        Connexions existantes        \n"
        "┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┓\n"
        "┃ Depart      ┃ Arrivée     ┃ Durée ┃\n"
        "┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━┩\n"
        "│ Paris       │ Tours       │ 1     │\n"
        "│ Tours       │ Paris       │ 1     │\n"
        "│ Tours       │ Bordeaux    │ 2     │\n"
        "│ Bordeaux    │ Tours       │ 2     │\n"
        "│ Bordeaux    │ Toulouse    │ 4     │\n"
        "│ Toulouse    │ Bordeaux    │ 4     │\n"
        "│ Toulouse    │ Montpellier │ 4     │\n"
        "│ Montpellier │ Toulouse    │ 4     │\n"
        "│ Montpellier │ Lyon        │ 2     │\n"
        "│ Lyon        │ Montpellier │ 2     │\n"
        "│ Lyon        │ Paris       │ 2     │\n"
        "│ Paris       │ Lyon        │ 2     │\n"
        "└─────────────┴─────────────┴───────┘\n"
    )


def test_commande_trajet():
    resultat = run(
        ["python", "app.py", "trajet", "Bordeaux", "Montpellier"], capture_output=True
    )
    assert resultat.stdout.decode("utf8") == (
        "         Trajet          \n"
        "┏━━━━━━━━━━━━━┳━━━━━━━━━┓\n"
        "┃ Gare        ┃ Instant ┃\n"
        "┡━━━━━━━━━━━━━╇━━━━━━━━━┩\n"
        "│ Bordeaux    │ 0       │\n"
        "│ Tours       │ 2       │\n"
        "│ Paris       │ 3       │\n"
        "│ Lyon        │ 5       │\n"
        "│ Montpellier │ 7       │\n"
        "└─────────────┴─────────┘\n"
    )
