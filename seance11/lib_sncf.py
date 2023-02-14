"""Description.

Calcule les trajets optimaux entre gares SNCF.
"""
import networkx as nx
from dataclasses import dataclass


@dataclass(frozen=True)
class Gare:
    """Représente un endroit desservi par le réseau."""

    nom: str


@dataclass
class Itineraire:
    """Représente un voyage effectué par l'utilisateur."""

    etapes: list[Gare]


@dataclass
class Carte:
    """Représentation de la carte de France pour les utilisateurs."""

    gares: list[Gare]
    connexions: list[tuple[Gare, Gare, float]]

    def __post_init__(self):
        if any(poids <= 0 for _, _, poids in self.connexions):
            raise ValueError("Les durées sont forcément positives!")

        for depart, arrivee, _ in self.connexions:
            if depart not in self.gares:
                raise ValueError(f"{depart} n'est pas dans la liste des gares!")
            if arrivee not in self.gares:
                raise ValueError(f"{arrivee} n'est pas dans la liste des gares!")


def _convertit_en_nx(carte: Carte) -> nx.Graph:
    """Crée un graphe symmétrique à partir de la carte."""
    resultat = nx.Graph()
    resultat.add_nodes_from(carte.gares)
    resultat.add_edges_from(
        (depart, arrivee, {"duree": poids})
        for depart, arrivee, poids in carte.connexions
    )
    return resultat


class PasDeChemin(Exception):
    pass


def determine_trajet(depart: Gare, arrivee: Gare, carte: Carte) -> Itineraire:
    """Détermine le trajet le plus court possible de depart à arrivee."""
    graphe = _convertit_en_nx(carte)
    try:
        resultat_nx = nx.shortest_path(
            graphe, source=depart, target=arrivee, weight="duree"
        )
    except nx.exception.NetworkXNoPath:
        raise PasDeChemin(f"{depart} et {arrivee} ne sont pas connectées!")
    return Itineraire(etapes=resultat_nx)
