from datetime import date

from models.database import connecter


def creer_emprunt(id_livre, id_membre):
    date_du_jour = str(date.today())
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO emprunts (id_livre, id_membre, date_emprunt) VALUES (?, ?, ?)",
        (id_livre, id_membre, date_du_jour)
    )
    connexion.commit()
    connexion.close()


def enregistrer_retour(id_livre):
    date_du_jour = str(date.today())
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "UPDATE emprunts SET date_retour = ? "
        "WHERE id_livre = ? AND date_retour IS NULL",
        (date_du_jour, id_livre)
    )
    connexion.commit()
    connexion.close()


def lister_emprunts_en_cours():
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT livres.titre, membres.nom, membres.prenom, emprunts.date_emprunt "
        "FROM emprunts, livres, membres "
        "WHERE emprunts.id_livre = livres.id "
        "AND emprunts.id_membre = membres.id "
        "AND emprunts.date_retour IS NULL"
    )
    liste_emprunts = curseur.fetchall()
    connexion.close()
    return liste_emprunts