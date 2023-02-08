"""Description.

Classe permettant de représenter un graphe pondéré.
On devra articuler cette classe avec l'algorithme de Bellman-Ford.
"""
from dataclasses import dataclass
from typing import Generator
from pathlib import Path
import subprocess as sp


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
                
    def to_dot(self) -> str:
        lignes = ["\ndigraph gp {"]
        for sommet in self.sommets:
            lignes.append(f"{sommet};")
        for depart, arrivee, poids in self.arretes:
            lignes.append(f"{depart} -> {arrivee} [label={poids}];")
        lignes.append("}\n")
        return "\n".join(lignes)
    
    def to_svg(self, nom: str):
        """Crée un fichier nom.svg contenant une image du graphe.
        
        Délègue à graphviz le dessin.
        """
        if nom[-3:] != "svg":
            nom = nom + ".svg"
        rep = Path(".").resolve()
        # TODO: si jamais on a un fichier temp.dot préexistant, on l'écrase puis on le supprime
        # c'est à corriger soit en créant des noms de fichier aléatoire grâce au module random
        # soit en utilisant le module tempfile
        fichier_dot = rep / "temp.dot"
        fichier_dot.touch()
        fichier_dot.write_text(self.to_dot(), encoding="utf8")
        commande = sp.run(["dot", "temp.dot", "-T", "svg", "-o", nom])
        if commande.returncode != 0:
            raise ValueError("Impossible d'exécuter dot!")
        fichier_dot.unlink()
            
        
        
