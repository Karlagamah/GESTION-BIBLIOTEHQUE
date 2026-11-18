# Gestion d'une bibliothèque

Application en Python pour gérer une bibliothèque : livres, membres et emprunts.
Le projet est organisé selon l'architecture MVC.

## Fonctionnalités

- Ajouter, afficher, rechercher et supprimer un livre
- Ajouter et afficher des membres
- Emprunter un livre (un livre emprunté n'est plus disponible)
- Retourner un livre
- Afficher les emprunts en cours
- Des livres sont déjà enregistrés au premier lancement

## Structure du projet


GESTION BIBLIOTHEQUE
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── models
│   ├── database.py
│   ├── livre_model.py
│   ├── membre_model.py
│   └── emprunt_model.py
├── views
│   └── menu_view.py
└── controllers
    └── bibliotheque_controller.py


## Architecture MVC

- **Modèle** : contient les requêtes SQL et communique avec la base de données.
- **Vue** : affiche les menus et les résultats, et demande les saisies à l'utilisateur.
- **Contrôleur** : relie la vue et le modèle, et vérifie les règles (livre existant, livre disponible...).

## Lancer le programme

Ouvrir un terminal dans le dossier du projet, puis taper :


py main.py


## Utilisation

Un menu s'affiche dans le terminal :


1. Ajouter un livre
2. Afficher les livres
3. Rechercher un livre
4. Supprimer un livre
5. Ajouter un membre
6. Afficher les membres
7. Emprunter un livre
8. Retourner un livre
9. Afficher les emprunts en cours
0. Quitter


Pour emprunter un livre, il faut d'abord ajouter un membre (option 5), puis
utiliser l'ID du livre (option 2) et l'ID du membre (option 6).

