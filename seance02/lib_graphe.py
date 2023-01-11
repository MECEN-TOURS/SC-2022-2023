"""Description.

Implémentation des algorithmes de parcours de graphes génériques.
"""

from typing import TypeVar

Sommet = TypeVar("Sommet")


def recupere_voisins(sommet: Sommet, arretes: list[tuple[Sommet, Sommet]]) -> list[Sommet]:
    resultat = list()
    for sommet1, sommet2 in arretes:
        if sommet1 == sommet:
            resultat.append(sommet2)
    return resultat


def sont_connectes(
    depart: Sommet,
    arrivee: Sommet,
    sommets: list[Sommet],
    arretes: list[tuple[Sommet, Sommet]],
    debug: bool = False,
) -> bool:
    a_visiter = [depart]
    visites: list[Sommet] = []
    while a_visiter:
        if debug:
            print(f"{a_visiter=}")
            print(f"{visites=}")
            print()
        sommet_courant = a_visiter.pop()
        visites.append(sommet_courant)
        for voisin in recupere_voisins(sommet=sommet_courant, arretes=arretes):
            if voisin not in visites:
                a_visiter.append(voisin)
        if sommet_courant == arrivee:
            return True
    return False


def determine_chemin(
    depart: Sommet, arrivee: Sommet, vu_en_premier_par: dict[Sommet, Sommet | None]
) -> list[Sommet]:
    resultat_intermediaire = list()
    sommet_courant: Sommet | None = arrivee
    while sommet_courant is not None:
        resultat_intermediaire.append(sommet_courant)
        sommet_courant = vu_en_premier_par[sommet_courant]
    return [sommet for sommet in reversed(resultat_intermediaire)]


class PasDeChemin(Exception):
    ...


def cherche_chemin(
    depart: Sommet,
    arrivee: Sommet,
    sommets: list[Sommet],
    arretes: list[tuple[Sommet, Sommet]],
    debug: bool = False,
) -> list[Sommet]:
    a_visiter = [depart]
    visites: list[Sommet] = []
    vu_en_premier_par: dict[Sommet, Sommet | None] = dict()
    vu_en_premier_par[depart] = None
    while a_visiter:
        if debug:
            print(f"{a_visiter=}")
            print(f"{visites=}")
            print()
        sommet_courant = a_visiter.pop()
        visites.append(sommet_courant)
        for voisin in recupere_voisins(sommet=sommet_courant, arretes=arretes):
            if voisin not in visites:
                a_visiter.append(voisin)
                vu_en_premier_par[voisin] = sommet_courant
        if sommet_courant == arrivee:
            return determine_chemin(
                depart=depart, arrivee=arrivee, vu_en_premier_par=vu_en_premier_par
            )
    raise PasDeChemin
