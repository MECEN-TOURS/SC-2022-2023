"""Description.

Implémentation des algorithmes de parcours de graphes génériques.

TODO: 
- Reprendre la fonction cherche_chemin qui sont trop longues.
On pourrait "factoriser" la partie construction de vu_en_premier_par dans une autre fonction
- Compléter la documentation des fonctions publique avec des exemples
"""

from typing import TypeVar

Sommet = TypeVar("Sommet")


def _recupere_voisins(
    sommet: Sommet, arretes: list[tuple[Sommet, Sommet]]
) -> list[Sommet]:
    """Renvoie la liste des voisins à partir des arrêtes."""
    resultat = list()
    for sommet1, sommet2 in arretes:
        if sommet1 == sommet:
            resultat.append(sommet2)
    return resultat


def sont_connectes(
    depart: Sommet,
    arrivee: Sommet,
    arretes: list[tuple[Sommet, Sommet]],
    debug: bool = False,
) -> bool:
    """Détermine s'il y a un chemin reliant depart et arrivee via des arretes."""
    a_visiter = [depart]
    visites: list[Sommet] = []
    while a_visiter:
        if debug:
            print(f"{a_visiter=}")
            print(f"{visites=}")
            print()
        sommet_courant = a_visiter.pop()
        visites.append(sommet_courant)
        for voisin in _recupere_voisins(sommet=sommet_courant, arretes=arretes):
            if voisin not in visites:
                a_visiter.append(voisin)
        if sommet_courant == arrivee:
            return True
    return False


def _determine_chemin(
    arrivee: Sommet, vu_en_premier_par: dict[Sommet, Sommet | None]
) -> list[Sommet]:
    """Détermine le chemin de départ à arrivée en remontant la relation vu_en_premier_par.

    vu_en_premier_par associe None au somme de depart.
    """
    resultat_intermediaire = list()
    sommet_courant: Sommet | None = arrivee
    while sommet_courant is not None:
        resultat_intermediaire.append(sommet_courant)
        sommet_courant = vu_en_premier_par[sommet_courant]
    return [sommet for sommet in reversed(resultat_intermediaire)]


class PasDeChemin(Exception):
    """Erreur représentant l'absence de chemin."""

    ...


def cherche_chemin(
    depart: Sommet,
    arrivee: Sommet,
    arretes: list[tuple[Sommet, Sommet]],
    debug: bool = False,
) -> list[Sommet]:
    """Renvoie un chemin reliant depart et arrivee via les arretes.

    S'il n'y a pas de chemin on génère PasDeChemin.

    Exemples:
    >>> arretes = [(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (8, 6)]
    >>> cherche_chemin(depart=1, arrivee=7, arretes=arretes)
    [1, 2, 5, 6, 7]
    >>> cherche_chemin(depart=1, arrivee=8, arretes=arretes)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\\Users\\perrollaz\\Documents\\sc03\\lib_graphe.py", line 99, in cherche_chemin vu_en_premier_par[voisin] = sommet_courant
    __main__.PasDeChemin
    """
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
        for voisin in _recupere_voisins(sommet=sommet_courant, arretes=arretes):
            if voisin not in visites:
                a_visiter.append(voisin)
                vu_en_premier_par[voisin] = sommet_courant
        if sommet_courant == arrivee:
            return _determine_chemin(
                arrivee=arrivee, vu_en_premier_par=vu_en_premier_par
            )
    raise PasDeChemin
