"""Description.

Librairie pour résolution de Sudoku.

TODO:
X Identifier l'interface publique de la librairie.
X Ajouter une fonction pretty_print faisant un affichage plus "sympathique" d'une grille de Sudoku.
X convertir la fonction en méthode __str__ du datamodel python
X Documenter la librairie: ajouter des exemples pour l'interface publique.
- Adapter la librairie pour résoudre des sudoku 3x3.
- Rajouter topo sur destructuration et *
- Rajouter topo sur __str__ et datamodel
"""
from typing import Generator
from dataclasses import dataclass


@dataclass
class Grille:
    r"""Grille partiellement remplie de Sudoku.

        0 représente une case vide.

        Exemples:
    >>> Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> print(Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

    ---------
    |1|2| | |
    ---------
    |3| | | |
    ---------
    | | | | |
    ---------
    | | | | |
    ---------

    >>> Grille(cases=[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 4, in __init__
      File "C:\Users\perrollaz\Documents\sc05\lib_sudoku.py", line 29, in __post_init__
        raise ValueError("Il doit y avoir exactement 16 cases.")
    ValueError: Il doit y avoir exactement 16 cases.
    >>> Grille(cases=[-1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 4, in __init__
      File "C:\Users\perrollaz\Documents\sc05\lib_sudoku.py", line 31, in __post_init__
        raise ValueError("Les valeurs permises sont 0,1,2,3 ou 4!")
    ValueError: Les valeurs permises sont 0,1,2,3 ou 4!
    """

    cases: list[int]

    def __post_init__(self):
        if len(self.cases) != 16:
            raise ValueError("Il doit y avoir exactement 16 cases.")
        if any(case < 0 or case > 4 for case in self.cases):
            raise ValueError("Les valeurs permises sont 0,1,2,3 ou 4!")

    def __str__(self) -> str:
        """Affiche une grille plus proprement."""
        # cases = [case if case != 0 else " " for case in grille.cases]
        cases = list()
        for case in self.cases:
            if case == 0:
                cases.append(" ")
            else:
                cases.append(str(case))
        resultat = """
---------
|{}|{}|{}|{}|
---------
|{}|{}|{}|{}|
---------
|{}|{}|{}|{}|
---------
|{}|{}|{}|{}|
---------
""".format(
            *cases
        )
        return resultat


def _detecte_probleme_ligne(grille: Grille) -> bool:
    """Détecte la répétition sur une ligne."""
    for i in (0, 4, 8, 12):
        for valeur in (1, 2, 3, 4):
            if grille.cases[i : i + 4].count(valeur) > 1:
                return True
    return False


def _detecte_probleme_colonne(grille: Grille) -> bool:
    """Détecte la répétition sur une colonne."""
    for i in (0, 1, 2, 3):
        for valeur in (1, 2, 3, 4):
            if grille.cases[i::4].count(valeur) > 1:
                return True
    return False


def _detecte_probleme_bloc(grille: Grille) -> bool:
    """Détecte la répétition sur un bloc."""
    for i in (0, 2, 8, 10):
        for valeur in (1, 2, 3, 4):
            if [grille.cases[i + j] for j in (0, 1, 4, 5)].count(valeur) > 1:
                return True
    return False


def _est_valide(grille: Grille) -> bool:
    """Détecte les répétition lignes/colonnes/sousgrilles."""
    if _detecte_probleme_ligne(grille):
        return False
    if _detecte_probleme_colonne(grille):
        return False
    if _detecte_probleme_bloc(grille):
        return False
    return True


def _est_remplie(grille: Grille) -> bool:
    """Détecte l'absence de case vide."""
    return grille.cases.count(0) == 0


class PasDeSolution(Exception):
    """Représente l'absence de solution au Sudoku."""

    pass


def _genere_voisines(grille: Grille) -> Generator[Grille, None, None]:
    """Renvoie les 4 façons de remplir la première case."""
    nouvelle_cases = [case for case in grille.cases]
    try:
        position_zero = nouvelle_cases.index(0)  # attention peut planter
    except ValueError:
        raise ValueError("La grille est déjà remplie.")
    for remplissage in (1, 2, 3, 4):
        nouvelle_cases[position_zero] = remplissage
        yield Grille(cases=nouvelle_cases)


def resoud_sudoku(grille: Grille) -> Grille:
    r"""Resoud le sudoku correspondant à grille au départ.

        Genere PasDeSolution s'il le problème n'est pas soluble.
        Exemples:
    >>> print(resoud_sudoku(Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])))

    ---------
    |1|2|3|4|
    ---------
    |3|4|1|2|
    ---------
    |2|1|4|3|
    ---------
    |4|3|2|1|
    ---------

    >>> print(resoud_sudoku(Grille([0, 2, 3, 0, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 0, 1])))

    ---------
    |1|2|3|4|
    ---------
    |3|4|1|2|
    ---------
    |2|1|4|3|
    ---------
    |4|3|2|1|
    ---------

    >>> print(resoud_sudoku(Grille([0, 2, 3, 3, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 0, 1])))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\Users\perrollaz\Documents\sc05\lib_sudoku.py", line 136, in resoud_sudoku
        "Renvoie les 4 façons de remplir la première case."
    __main__.PasDeSolution
    """
    if _est_remplie(grille):
        if _est_valide(grille):
            return grille
        else:
            raise PasDeSolution
    else:
        for voisine in _genere_voisines(grille):
            if _est_valide(voisine):
                try:
                    solution = resoud_sudoku(voisine)
                except PasDeSolution:
                    pass
                else:
                    return solution
        raise PasDeSolution