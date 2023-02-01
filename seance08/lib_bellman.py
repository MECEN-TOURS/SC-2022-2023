"""Description.

Implémentation de Bellman-Ford pour GraphePondere.

TODO:
- prendre en compte les cas impossibles!
"""
from lib_graphe import GraphePondere

def itere_distance(dist: dict[str, tuple[float, str | None]], gp: GraphePondere) -> dict[str, tuple[float, str | None]]:
    resultat = dict()
    for sommet in dist:
        if dist[sommet] == 0.:
            resultat[sommet] = 0.
        else:
            resultat[sommet] = min(poids + dist[voisin] for voisin, poids in gp.voisinage(sommet))
    return resultat

def determine_distance(arrivee: str, gp: GraphePondere) -> dict[str, tuple[float | None]]:
    d_ini = {sommet: (float("inf"), None) for sommet in gp.sommets}
    d_ini[arrivee] = (0., arrivee)
    d_suite = itere_distance(dist=d_ini, gp=gp)
    while d_ini != d_suite:
        d_ini, d_suite = d_suite, itere_distance(dist=d_suite, gp=gp)
    return d_ini

def determine_chemin_minimal(depart: str, arrivee: str, gp: GraphePondere) -> list[str]:
    """Détermine un chemin minimal allant de depart à arrivee dans gp."""
    ...