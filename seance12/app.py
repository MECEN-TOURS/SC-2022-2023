"""Description.

Module contenant l'interface utilisateur de la librairie.
"""
import typer
from rich import print
from rich.table import Table
from rich.columns import Columns
import lib_sncf as ls
import lib_format as lf

app = typer.Typer()

@app.command()
def gares():
    """Affiche les gares desservies."""
    print(lf.format_gares(ls.CARTE_FRANCE))
    
@app.command()
def connexions():
    """Affiche les connexions de la carte."""
    print(lf.format_connexions(ls.CARTE_FRANCE))
        
    
@app.command()
def trajet(depart: str, arrivee: str):
    """Calcule un trajet optimal entre les gares."""
    try:
        resultat = ls.determine_trajet(
            depart=ls.Gare(nom=depart),
            arrivee=ls.Gare(nom=arrivee),
            carte=ls.CARTE_FRANCE,
        )
    except ls.PasDeChemin as e:
        print(e)
    except ls.GareInconnue as e:
        print(e)
    else:
        print(lf.format_itineraire(resultat))
        
        
        
    
if __name__ == "__main__":
    app()