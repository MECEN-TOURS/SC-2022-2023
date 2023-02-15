"""Description.

Formattage des objets de lib_sncf vers des objets rich.
"""
from rich.table import Table
from rich.columns import Columns
import lib_sncf as ls

def format_itineraire(itineraire: ls.Itineraire) -> Table:
    resultat = Table(title="Trajet")
    resultat.add_column("Gare")
    resultat.add_column("Instant")
    instant = 0
    it_res = iter(itineraire.etapes)
    g1 = next(it_res)
    resultat.add_row(g1.nom, str(instant))
    for g2 in it_res:
        for depart, arrivee, duree in ls.CARTE_FRANCE.connexions:
            if depart == g1 and arrivee == g2:
                instant = instant + duree
                break
            if depart == g2 and arrivee == g1:
                instant = instant + duree
                break
        resultat.add_row(g2.nom, str(instant))
        g1 = g2
    return resultat

def format_connexions(carte: ls.Carte) -> Table:
    resultat = Table(title="Connexions existantes")
    resultat.add_column("Depart")
    resultat.add_column("Arrivée")
    resultat.add_column("Durée")
    for g1, g2, duree in carte.connexions:
        resultat.add_row(g1.nom, g2.nom, str(duree))
        resultat.add_row(g2.nom, g1.nom, str(duree))
    return resultat

def format_gares(carte) -> Columns:
    return Columns([gare.nom for gare in carte.gares])