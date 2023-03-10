# Affectation des sujets

## Groupes

1. Guillaume Devant, Hassan Tilki
2. Aybuké Bicat, Corentin Ducloux
3. Albéric D’herbais, Jean-Hugues Blanchard
4. Simon Blanchard, Adam Belamiri
5. Sebastien Tolojanahary, Stephen Guitter
6. Karl Sondeji, Pierre Jean
7. Nazifou Afolabi, Charbel Ahouandokoun
8. Cyprien De Clercq, Basma Ghaffour
9. Youssef Dir

## Affectation

On lancera le script `affectation.py` pour faire correspondre sujet et groupe.

## Consignes

Les sujets sont constitués d'un _exemple_ de problème.

On commencera évidemment par le résoudre.
Dans un second temps, il faudra _le généraliser_.
On fournira finalement un projet python complet permettant à des utilisateurs
de résoudre des problèmes du type de l'exemple.

## Projet complet

On devra avoir en particulier:

- Une gestion des dépendances pour garantir la portabilité entre machines.
  On pourra utiliser `poetry` pour ceci.
- Une librairie typée/testée/documentée.
  On pourra entre autre utiliser `mypy`, `pytest` (et `pytest-cov` pour la couverture).
  On suggère fortement d'utiliser un linter tel que `ruff` pour éviter les bogues.
- Une interface en ligne de commande (via `typer`).
  On pourra faire une démonstration via un fichier `README.md`.
  Par exemple, en utilisant l'interface pour résoudre le problème exemple.
  Les personnes ambitieuses pourront chercher à proposer une interface TUI avec `textual`.

On pourra aussi s'inspirer de l'exemple présenté lors du dernier cours.
