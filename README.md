# OC_P7_Back
Version finale du back end allégé (10k lignes par DataFrames) du P7 (FastAPI)

Cet API sert de ressource pour le Dashboard puisqu'elle contient l'ensemble des fonctions qui seront utilisés dans celui-ci.

Arborescence:
    > Le dossier data contient l'ensemble des prérequis externe generé par le notebook initial (csv, pkl etc...)
    > Le dossier tab contient l'ensemble des fonctions de l'API (prédictions, intepratibilité etc...)
    > Le dossier tests contients les pytest étant vérifié lors d'un push vers github
    >A la racine du projet se trouve le fichier main contenant l'accès aux differentes fonctions de tab, ainsi que des fichiers annexes nécéssaires au bon déroulement de l'API ou à son déploiement (imports, requirements etc...)