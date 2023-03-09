#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Script effectuant la répartition des sujets au élèves.
"""
import random as rd
from rich.console import Console

GROUPES = (
    ("Guillaume Devant", "Hassan Tilki"),
    ("Aybuké Bicat", "Corentin Ducloux"),
    ("Albéric D’herbais", "Jean-Hugues Blanchard"),
    ("Simon Blanchard", "Adam Belamiri"),
    ("Sebastien Tolojanahary", "Stephen Guitter"),
    ("Karl Sondeji", "Pierre Jean"),
    ("Nazifou Afolabi", "Charbel Ahouandokoun"),
    ("Cyprien De Clercq", "Basma Ghaffour"),
    ("Youssef Dir",),
)

SUJETS = [f"{numero+1:02}" for numero in range(1, 14)]
rd.seed(2023)
rd.shuffle(SUJETS)

CS = Console()

AFFECTATION = {eleve: sujet for eleve, sujet in zip(GROUPES, SUJETS)}
CS.print(AFFECTATION)
