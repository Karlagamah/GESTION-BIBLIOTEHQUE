def afficher_menu():
    print("\n===== BIBLIOTHEQUE =====")
    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Ajouter un membre")
    print("6. Afficher les membres")
    print("7. Emprunter un livre")
    print("8. Retourner un livre")
    print("9. Afficher les emprunts en cours")
    print("0. Quitter")
    choix = int(input("Votre choix : "))
    return choix


def demander_texte(message):
    texte = input(message)
    return texte


def demander_nombre(message):
    nombre = int(input(message))
    return nombre


def afficher_message(message):
    print(message)


def afficher_livres(liste_livres):
    if len(liste_livres) == 0:
        print("Aucun livre trouvé.")
    for livre in liste_livres:
        if livre[3] == 1:
            etat = "disponible"
        else:
            etat = "emprunté"
        print(livre[0], "|", livre[1], "|", livre[2], "|", etat)


def afficher_membres(liste_membres):
    if len(liste_membres) == 0:
        print("Aucun membre trouvé.")
    for membre in liste_membres:
        print(membre[0], "|", membre[1], "|", membre[2])


def afficher_emprunts(liste_emprunts):
    if len(liste_emprunts) == 0:
        print("Aucun emprunt en cours.")
    for emprunt in liste_emprunts:
        print(emprunt[0], "| emprunté par", emprunt[1], emprunt[2], "le", emprunt[3])