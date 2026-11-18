from models import emprunt_model, livre_model, membre_model
from views import menu_view


def ajouter_un_livre():
    titre = menu_view.demander_texte("Titre : ")
    auteur = menu_view.demander_texte("Auteur : ")
    livre_model.ajouter_livre(titre, auteur)
    menu_view.afficher_message("Livre ajouté.")


def afficher_les_livres():
    liste_livres = livre_model.lister_livres()
    menu_view.afficher_livres(liste_livres)


def rechercher_un_livre():
    mot_cle = menu_view.demander_texte("Mot-clé (titre ou auteur) : ")
    liste_livres = livre_model.rechercher_livres(mot_cle)
    menu_view.afficher_livres(liste_livres)


def supprimer_un_livre():
    id_livre = menu_view.demander_nombre("ID du livre à supprimer : ")
    livre = livre_model.obtenir_livre(id_livre)

    if livre is None:
        menu_view.afficher_message("Ce livre n'existe pas.")
    elif livre[3] == 0:
        menu_view.afficher_message("Ce livre est emprunté, impossible de le supprimer.")
    else:
        livre_model.supprimer_livre(id_livre)
        menu_view.afficher_message("Livre supprimé.")


def ajouter_un_membre():
    nom = menu_view.demander_texte("Nom : ")
    prenom = menu_view.demander_texte("Prénom : ")
    membre_model.ajouter_membre(nom, prenom)
    menu_view.afficher_message("Membre ajouté.")


def afficher_les_membres():
    liste_membres = membre_model.lister_membres()
    menu_view.afficher_membres(liste_membres)


def emprunter_un_livre():
    id_livre = menu_view.demander_nombre("ID du livre : ")
    id_membre = menu_view.demander_nombre("ID du membre : ")

    livre = livre_model.obtenir_livre(id_livre)
    membre = membre_model.obtenir_membre(id_membre)

    if livre is None:
        menu_view.afficher_message("Ce livre n'existe pas.")
    elif membre is None:
        menu_view.afficher_message("Ce membre n'existe pas.")
    elif livre[3] == 0:
        menu_view.afficher_message("Ce livre est déjà emprunté.")
    else:
        emprunt_model.creer_emprunt(id_livre, id_membre)
        livre_model.changer_disponibilite(id_livre, 0)
        menu_view.afficher_message("Emprunt enregistré.")


def retourner_un_livre():
    id_livre = menu_view.demander_nombre("ID du livre à retourner : ")
    livre = livre_model.obtenir_livre(id_livre)

    if livre is None:
        menu_view.afficher_message("Ce livre n'existe pas.")
    elif livre[3] == 1:
        menu_view.afficher_message("Ce livre n'est pas emprunté.")
    else:
        emprunt_model.enregistrer_retour(id_livre)
        livre_model.changer_disponibilite(id_livre, 1)
        menu_view.afficher_message("Retour enregistré.")


def afficher_les_emprunts():
    liste_emprunts = emprunt_model.lister_emprunts_en_cours()
    menu_view.afficher_emprunts(liste_emprunts)