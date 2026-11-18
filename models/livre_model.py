from models.database import connecter


def ajouter_livre(titre, auteur):
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, 1)",
        (titre, auteur)
    )
    connexion.commit()
    connexion.close()


def lister_livres():
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, titre, auteur, disponible FROM livres")
    liste_livres = curseur.fetchall()
    connexion.close()
    return liste_livres


def rechercher_livres(mot_cle):
    connexion = connecter()
    curseur = connexion.cursor()
    motif = "%" + mot_cle + "%"
    curseur.execute(
        "SELECT id, titre, auteur, disponible FROM livres "
        "WHERE titre LIKE ? OR auteur LIKE ?",
        (motif, motif)
    )
    liste_livres = curseur.fetchall()
    connexion.close()
    return liste_livres


def obtenir_livre(id_livre):
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, titre, auteur, disponible FROM livres WHERE id = ?",
        (id_livre,)
    )
    livre = curseur.fetchone()
    connexion.close()
    return livre


def changer_disponibilite(id_livre, valeur):
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "UPDATE livres SET disponible = ? WHERE id = ?",
        (valeur, id_livre)
    )
    connexion.commit()
    connexion.close()


def supprimer_livre(id_livre):
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM livres WHERE id = ?", (id_livre,))
    connexion.commit()
    connexion.close()