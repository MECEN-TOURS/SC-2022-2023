"""Description.

Librairie pour résolution de Sudoku à 9 lignes et 9 colonnes.

TODO: documenter l'interface publique
"""
from typing import Generator
from dataclasses import dataclass


@dataclass
class Grille:
    r"""Grille partiellement remplie de Sudoku.

    0 représente une case vide."""

    cases: list[int]

    def __post_init__(self):
        if len(self.cases) != 81:
            raise ValueError("Il doit y avoir exactement 81 cases.")
        if any(case < 0 or case > 9 for case in self.cases):
            raise ValueError("Les valeurs permises sont 0, 1, 2, ... 9!")

    @classmethod
    def from_str(cls, code: str) -> "Grille":
        """Crée une grille à partir d'une chaine de caractères.

        x représente une case vide.
        """
        cases = list()
        for ligne in code.strip().splitlines():
            for car in ligne.strip():
                if car == "x":
                    cases.append(0)
                else:
                    cases.append(int(car))
        return cls(cases)

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
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
|{}|{}|{}|{}|{}|{}|{}|{}|{}|
-------------------
""".format(
            *cases
        )
        return resultat


def _detecte_probleme_ligne(grille: Grille) -> bool:
    """Détecte la répétition sur une ligne."""
    for i in range(0, 81, 9):
        for valeur in range(1, 10):
            if grille.cases[i : i + 9].count(valeur) > 1:
                return True
    return False


def _detecte_probleme_colonne(grille: Grille) -> bool:
    """Détecte la répétition sur une colonne."""
    for i in range(10):
        for valeur in range(1, 10):
            if grille.cases[i::9].count(valeur) > 1:
                return True
    return False


def _detecte_probleme_bloc(grille: Grille) -> bool:
    """Détecte la répétition sur un bloc."""
    for i in (0, 3, 6, 27, 30, 33, 54, 57, 60):
        for valeur in range(1, 10):
            if [grille.cases[i + j] for j in (0, 1, 2, 9, 10, 11, 18, 19, 20)].count(
                valeur
            ) > 1:
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
    """Renvoie les 9 façons de remplir la première case."""
    nouvelle_cases = [case for case in grille.cases]
    try:
        position_zero = nouvelle_cases.index(0)  # attention peut planter
    except ValueError:
        raise ValueError("La grille est déjà remplie.")
    for remplissage in range(1, 10):
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
