from models.database import connecter


def ajouter_membre(nom, prenom):
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO membres (nom, prenom) VALUES (?, ?)",
        (nom, prenom)
    )
    connexion.commit()
    connexion.close()


def lister_membres():
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, nom, prenom FROM membres")
    liste_membres = curseur.fetchall()
    connexion.close()
    return liste_membres


def obtenir_membre(id_membre):
    connexion = connecter()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, nom, prenom FROM membres WHERE id = ?",
        (id_membre,)
    )
    membre = curseur.fetchone()
    connexion.close()
    return membre