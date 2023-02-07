"""Description.

Classe permettant de représenter un graphe pondéré.
On devra articuler cette classe avec l'algorithme de Bellman-Ford.
"""
from dataclasses import dataclass
from typing import Generator


@dataclass
class GraphePondere:
    sommets: list[str]
    arretes: list[tuple[str, str, float]]

    def __post_init__(self):
        sommets_a_tester = set(self.sommets)
        for depart, arrivee, poids in self.arretes:
            if poids < 0:
                raise ValueError("Les poids doivent être positifs ou nuls!")
            if depart not in sommets_a_tester or arrivee not in sommets_a_tester:
                raise ValueError("Les arrêtes doivent relier des sommets valables.")

    @classmethod
    def symetrique(cls, sommets, arretes):
        doublees = list()
        for depart, arrivee, poids in arretes:
            doublees.append((depart, arrivee, poids))
            doublees.append((arrivee, depart, poids))
        return cls(sommets=sommets, arretes=doublees)

    def __eq__(self, autre) -> bool:
        if type(autre) != type(self):
            print("type")
            return False
        if set(self.sommets) != set(autre.sommets):
            print("sommets")
            return False
        if set(self.arretes) != set(autre.arretes):
            print("arretes")
            return False
        return True
    
    def voisinage(self, sommet: str) -> Generator[tuple[str, float], None, None]:
        for depart, arrivee, poids in self.arretes:
            if sommet == depart:
                yield (arrivee, poids)
