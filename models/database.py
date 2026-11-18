import sqlite3

from config import NOM_BASE_DE_DONNEES


def connecter():
    connexion = sqlite3.connect(NOM_BASE_DE_DONNEES)
    return connexion


def creer_tables():
    connexion = connecter()
    curseur = connexion.cursor()

    curseur.execute(
        "CREATE TABLE IF NOT EXISTS livres ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "titre TEXT, "
        "auteur TEXT, "
        "disponible INTEGER)"
    )

    curseur.execute(
        "CREATE TABLE IF NOT EXISTS membres ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nom TEXT, "
        "prenom TEXT)"
    )

    curseur.execute(
        "CREATE TABLE IF NOT EXISTS emprunts ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "id_livre INTEGER, "
        "id_membre INTEGER, "
        "date_emprunt TEXT, "
        "date_retour TEXT)"
    )

    connexion.commit()
    connexion.close()


def ajouter_livres_par_defaut():
    connexion = connecter()
    curseur = connexion.cursor()

    livres_par_defaut = [
        ("Le Petit Prince", "Antoine de Saint-Exupéry"),
        ("Les Misérables", "Victor Hugo"),
        ("L'Étranger", "Albert Camus"),
        ("Germinal", "Émile Zola"),
        ("Bel-Ami", "Guy de Maupassant"),
        ("Les Soleils des indépendances", "Ahmadou Kourouma"),
        ("Allah n'est pas obligé", "Ahmadou Kourouma"),
        ("Une vie de boy", "Ferdinand Oyono"),
        ("Sous l'orage", "Seydou Badian"),
        ("Le Rouge et le Noir", "Stendhal"),
    ]

    for livre in livres_par_defaut:
        titre = livre[0]
        auteur = livre[1]

        curseur.execute(
            "SELECT COUNT(*) FROM livres WHERE titre = ? AND auteur = ?",
            (titre, auteur)
        )
        nombre_trouve = curseur.fetchone()[0]

        if nombre_trouve == 0:
            curseur.execute(
                "INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, 1)",
                (titre, auteur)
            )

    connexion.commit()
    connexion.close()